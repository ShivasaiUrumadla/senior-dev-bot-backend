from fastapi import FastAPI, Request, BackgroundTasks
from openai import models
from pydantic import BaseModel
from groq import Groq
from openai import OpenAI
import requests
from dotenv import load_dotenv
import os
from app.services.github_service import get_pr_diff, comment, get_pr_context,build_retrieval_query
from app.services.llm_service import llm
from app.services.github_app_service import generate_installation_token
from app.services.embedding_service import create_embedding
from app.services.vector_store_service import (
    is_repository_indexed,
    search_similar_chunks
)
from app.services.indexing_service import index_repository



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#.env
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



app=FastAPI()



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# functions
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------












#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Routes
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



@app.get("/")
async def hello():

    return "fast api working perfectly"


@app.post("/webhook")
async def github_webhook(request: Request, background_tasks: BackgroundTasks):
    data = await request.json()

    action = data.get("action")

    if action not in ["opened", "reopened", "synchronize"]:
        print("Ignoring action:", action)
        return {"status": "ignored"}

    # Start the heavy work in the background
    background_tasks.add_task(process_pr_review, data)

    # Respond to GitHub immediately
    return {
        "status": "accepted",
        "message": "PR review started"
    }

async def process_pr_review(data):
    try:
        repository = data.get("repository", {})
        repo_name = repository.get("full_name")

        pull_request = data.get("pull_request", {})
        pr_number = pull_request.get("number")

        head = pull_request.get("head", {})
        head_sha = head.get("sha")

        base = pull_request.get("base", {})
        base_sha = base.get("sha")

        print("Repository:", repo_name)
        print("PR Number:", pr_number)
        print("Head SHA:", head_sha)
        print("Base SHA:", base_sha)

        installation = data.get("installation", {})
        installation_id = installation.get("id")

        print("Installation ID:", installation_id)

        if not installation_id:
            print("No installation ID")
            return

        print("Action:", data.get("action"))

        installation_token = generate_installation_token(
            installation_id
        )

        base_indexed = is_repository_indexed(
            repo=repo_name,
            commit_sha=base_sha
        )

        print("Base snapshot indexed:", base_indexed)

        if not base_indexed:
            print("Indexing base snapshot...")

            total_chunks = index_repository(
                repo=repo_name,
                token=installation_token,
                ref=base_sha
            )

            print("Total chunks indexed:", total_chunks)

        diff = get_pr_diff(
            repo_name,
            pr_number,
            installation_token
        )

        print("PR Diff:", diff)

        if not diff.strip():
            print("No PR diff found. Skipping review.")
            return

        retrieval_query = build_retrieval_query(diff)

        print("Retrieval Query:")
        print(retrieval_query)

        query_embedding = create_embedding(retrieval_query)

        results = search_similar_chunks(
            query_embedding=query_embedding,
            repo=repo_name,
            commit_sha=base_sha,
            match_count=5
        )

        print("Retrieved chunks:")

        for result in results:
            print("\n----------------")
            print("File:", result["file_path"])
            print("Chunk:", result["chunk_index"])
            print("Similarity:", result["similarity"])
            print(result["content"])

        context_parts = []

        for result in results:
            context_parts.append(
                f"""
File: {result["file_path"]}
Chunk: {result["chunk_index"]}

{result["content"]}
"""
            )

        context = "\n\n".join(context_parts)

        prompt = f"""
You are an AI code reviewer assisting a senior developer.

Review only issues introduced by this PR.
Use the repository context to understand dependencies and expected behavior.

Report only high-confidence:
- bugs
- incorrect behavior
- security issues
- breaking changes

Ignore pre-existing issues and general code-quality suggestions.

Keep the review concise.
Return at most 2 findings.

For each finding:
Issue: <what is wrong>
Impact: <why it matters>
Fix: <how to fix it>

If no significant issue exists, return exactly:
No significant issues found.

PR Diff:
{diff}

Repository Context:
{context}
"""

        print("Sending PR to LLM...")

        review = await llm(prompt=prompt)

        print("Review:")
        print(review)

        comment(
            review=review,
            repo_name=repo_name,
            pr_number=pr_number,
            installation_token=installation_token
        )

        print("Review posted successfully.")

    except Exception as e:
        print("PR review failed:", repr(e))
