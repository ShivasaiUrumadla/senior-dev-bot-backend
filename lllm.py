from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_SECRET_KEY


supabase = create_client(
        .execute()
    )

    return response

def store_chunks(rows):
    response = (
        supabase
        .table("code_chunks")
        .insert(rows)
        .execute()
    )

    return response

def search_similar_chunks(
    query_embedding,
    repo: str,
    commit_sha: unt": match_count,
                "filter_repo": repo,
                "filter_commit_sha": commit_sha
            }
        )
        .execute()
    )

    return response.data

def is_repository_indexed(repo: str, commit_sha: str):
    response = (
        supabase
        .table("code_chunks")
        .select("id")
        .eq("repo", repo)
        .eq("commit_sha", commit_sha)
        .limit(1)
        .execute()
    )

    return len(response.data) > 0
