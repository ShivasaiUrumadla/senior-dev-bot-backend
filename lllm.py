from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_SECRET_KEY


supabase = create_client(
    SUPABASE_URL,
    SUPABASE_SECRET_KEY
)


from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_SECRET_KEY


supabase = create_client(
    SUPABASE_URL,
    SUPABASE_SECRET_KEY
)


def store_chunk(
    repo,
    commit_sha,
    file_path,
    chunk_index,
    content,
    embedding
):
    response = (
        supabase
        .table("code_chunks")
        .insert({
            "repo": repo,
            "commit_sha": commit_sha,
            "file_path": file_path,
            "chunk_index": chunk_index,
            "content": content,
            "embedding": embedding
        })
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
    commit_sha: str,
    match_count: int = 5
):
    response = (
        supabase
        .rpc(
            "match_code_chunks",
            {
                "query_embedding": query_embedding,
                "match_count": match_count,
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

from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_SECRET_KEY


supabase = create_client(
    SUPABASE_URL,
    SUPABASE_SECRET_KEY
)


def store_chunk(
    repo,
    commit_sha,
    file_path,
    chunk_index,
    content,
    embedding
):
    response = (
        supabase
        .table("code_chunks")
        .insert({
            "repo": repo,
            "commit_sha": commit_sha,
            "file_path": file_path,
            "chunk_index": chunk_index,
            "content": content,
            "embedding": embedding
        })
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
    commit_sha: str,
    match_count: int = 5
):
    response = (
        supabase
        .rpc(
            "match_code_chunks",
            {
                "query_embedding": query_embedding,
                "match_count": match_count,
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

from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_SECRET_KEY


supabase = create_client(
    SUPABASE_URL,
    SUPABASE_SECRET_KEY
)


def store_chunk(
    repo,
    commit_sha,
    file_path,
    chunk_index,
    content,
    embedding
):
    response = (
        supabase
        .table("code_chunks")
        .insert({
            "repo": repo,
            "commit_sha": commit_sha,
            "file_path": file_path,
            "chunk_index": chunk_index,
            "content": content,
            "embedding": embedding
        })
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
    commit_sha: str,
    match_count: int = 5
):
    response = (
        supabase
        .rpc(
            "match_code_chunks",
            {
                "query_embedding": query_embedding,
                "match_count": match_count,
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

from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_SECRET_KEY


supabase = create_client(
    SUPABASE_URL,
    SUPABASE_SECRET_KEY
)


def store_chunk(
    repo,
    commit_sha,
    file_path,
    chunk_index,
    content,
    embedding
):
    response = (
        supabase
        .table("code_chunks")
        .insert({
            "repo": repo,
            "commit_sha": commit_sha,
            "file_path": file_path,
            "chunk_index": chunk_index,
            "content": content,
            "embedding": embedding
        })
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
    commit_sha: str,
    match_count: int = 5
):
    response = (
        supabase
        .rpc(
            "match_code_chunks",
            {
                "query_embedding": query_embedding,
                "match_count": match_count,
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

from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_SECRET_KEY


supabase = create_client(
    SUPABASE_URL,
    SUPABASE_SECRET_KEY
)


def store_chunk(
    repo,
    commit_sha,
    file_path,
    chunk_index,
    content,
    embedding
):
    response = (
        supabase
        .table("code_chunks")
        .insert({
            "repo": repo,
            "commit_sha": commit_sha,
            "file_path": file_path,
            "chunk_index": chunk_index,
            "content": content,
            "embedding": embedding
        })
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
    commit_sha: str,
    match_count: int = 5
):
    response = (
        supabase
        .rpc(
            "match_code_chunks",
            {
                "query_embedding": query_embedding,
                "match_count": match_count,
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

from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_SECRET_KEY


supabase = create_client(
    SUPABASE_URL,
    SUPABASE_SECRET_KEY
)


def store_chunk(
    repo,
    commit_sha,
    file_path,
    chunk_index,
    content,
    embedding
):
    response = (
        supabase
        .table("code_chunks")
        .insert({
            "repo": repo,
            "commit_sha": commit_sha,
            "file_path": file_path,
            "chunk_index": chunk_index,
            "content": content,
            "embedding": embedding
        })
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
    commit_sha: str,
    match_count: int = 5
):
    response = (
        supabase
        .rpc(
            "match_code_chunks",
            {
                "query_embedding": query_embedding,
                "match_count": match_count,
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

from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_SECRET_KEY


supabase = create_client(
    SUPABASE_URL,
    SUPABASE_SECRET_KEY
)


def store_chunk(
    repo,
    commit_sha,
    file_path,
    chunk_index,
    content,
    embedding
):
    response = (
        supabase
        .table("code_chunks")
        .insert({
            "repo": repo,
            "commit_sha": commit_sha,
            "file_path": file_path,
            "chunk_index": chunk_index,
            "content": content,
            "embedding": embedding
        })
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
    commit_sha: str,
    match_count: int = 5
):
    response = (
        supabase
        .rpc(
            "match_code_chunks",
            {
                "query_embedding": query_embedding,
                "match_count": match_count,
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

from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_SECRET_KEY


supabase = create_client(
    SUPABASE_URL,
    SUPABASE_SECRET_KEY
)


def store_chunk(
    repo,
    commit_sha,
    file_path,
    chunk_index,
    content,
    embedding
):
    response = (
        supabase
        .table("code_chunks")
        .insert({
            "repo": repo,
            "commit_sha": commit_sha,
            "file_path": file_path,
            "chunk_index": chunk_index,
            "content": content,
            "embedding": embedding
        })
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
    commit_sha: str,
    match_count: int = 5
):
    response = (
        supabase
        .rpc(
            "match_code_chunks",
            {
                "query_embedding": query_embedding,
                "match_count": match_count,
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

from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_SECRET_KEY


supabase = create_client(
    SUPABASE_URL,
    SUPABASE_SECRET_KEY
)


def store_chunk(
    repo,
    commit_sha,
    file_path,
    chunk_index,
    content,
    embedding
):
    response = (
        supabase
        .table("code_chunks")
        .insert({
            "repo": repo,
            "commit_sha": commit_sha,
            "file_path": file_path,
            "chunk_index": chunk_index,
            "content": content,
            "embedding": embedding
        })
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
    commit_sha: str,
    match_count: int = 5
):
    response = (
        supabase
        .rpc(
            "match_code_chunks",
            {
                "query_embedding": query_embedding,
                "match_count": match_count,
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
from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_SECRET_KEY


supabase = create_client(
    SUPABASE_URL,
    SUPABASE_SECRET_KEY
)


def store_chunk(
    repo,
    commit_sha,
    file_path,
    chunk_index,
    content,
    embedding
):
    response = (
        supabase
        .table("code_chunks")
        .insert({
            "repo": repo,
            "commit_sha": commit_sha,
            "file_path": file_path,
            "chunk_index": chunk_index,
            "content": content,
            "embedding": embedding
        })
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
    commit_sha: str,
    match_count: int = 5
):
    response = (
        supabase
        .rpc(
            "match_code_chunks",
            {
                "query_embedding": query_embedding,
                "match_count": match_count,
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
from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_SECRET_KEY


supabase = create_client(
    SUPABASE_URL,
    SUPABASE_SECRET_KEY
)


def store_chunk(
    repo,
    commit_sha,
    file_path,
    chunk_index,
    content,
    embedding
):
    response = (
        supabase
        .table("code_chunks")
        .insert({
            "repo": repo,
            "commit_sha": commit_sha,
            "file_path": file_path,
            "chunk_index": chunk_index,
            "content": content,
            "embedding": embedding
        })
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
    commit_sha: str,
    match_count: int = 5
):
    response = (
        supabase
        .rpc(
            "match_code_chunks",
            {
                "query_embedding": query_embedding,
                "match_count": match_count,
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
from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_SECRET_KEY


supabase = create_client(
    SUPABASE_URL,
    SUPABASE_SECRET_KEY
)


def store_chunk(
    repo,
    commit_sha,
    file_path,
    chunk_index,
    content,
    embedding
):
    response = (
        supabase
        .table("code_chunks")
        .insert({
            "repo": repo,
            "commit_sha": commit_sha,
            "file_path": file_path,
            "chunk_index": chunk_index,
            "content": content,
            "embedding": embedding
        })
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
    commit_sha: str,
    match_count: int = 5
):
    response = (
        supabase
        .rpc(
            "match_code_chunks",
            {
                "query_embedding": query_embedding,
                "match_count": match_count,
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
from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_SECRET_KEY


supabase = create_client(
    SUPABASE_URL,
    SUPABASE_SECRET_KEY
)


def store_chunk(
    repo,
    commit_sha,
    file_path,
    chunk_index,
    content,
    embedding
):
    response = (
        supabase
        .table("code_chunks")
        .insert({
            "repo": repo,
            "commit_sha": commit_sha,
            "file_path": file_path,
            "chunk_index": chunk_index,
            "content": content,
            "embedding": embedding
        })
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
    commit_sha: str,
    match_count: int = 5
):
    response = (
        supabase
        .rpc(
            "match_code_chunks",
            {
                "query_embedding": query_embedding,
                "match_count": match_count,
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
from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_SECRET_KEY


supabase = create_client(
    SUPABASE_URL,
    SUPABASE_SECRET_KEY
)


def store_chunk(
    repo,
    commit_sha,
    file_path,
    chunk_index,
    content,
    embedding
):
    response = (
        supabase
        .table("code_chunks")
        .insert({
            "repo": repo,
            "commit_sha": commit_sha,
            "file_path": file_path,
            "chunk_index": chunk_index,
            "content": content,
            "embedding": embedding
        })
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
    commit_sha: str,
    match_count: int = 5
):
    response = (
        supabase
        .rpc(
            "match_code_chunks",
            {
                "query_embedding": query_embedding,
                "match_count": match_count,
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
from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_SECRET_KEY


supabase = create_client(
    SUPABASE_URL,
    SUPABASE_SECRET_KEY
)


def store_chunk(
    repo,
    commit_sha,
    file_path,
    chunk_index,
    content,
    embedding
):
    response = (
        supabase
        .table("code_chunks")
        .insert({
            "repo": repo,
            "commit_sha": commit_sha,
            "file_path": file_path,
            "chunk_index": chunk_index,
            "content": content,
            "embedding": embedding
        })
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
    commit_sha: str,
    match_count: int = 5
):
    response = (
        supabase
        .rpc(
            "match_code_chunks",
            {
                "query_embedding": query_embedding,
                "match_count": match_count,
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
from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_SECRET_KEY


supabase = create_client(
    SUPABASE_URL,
    SUPABASE_SECRET_KEY
)


def store_chunk(
    repo,
    commit_sha,
    file_path,
    chunk_index,
    content,
    embedding
):
    response = (
        supabase
        .table("code_chunks")
        .insert({
            "repo": repo,
            "commit_sha": commit_sha,
            "file_path": file_path,
            "chunk_index": chunk_index,
            "content": content,
            "embedding": embedding
        })
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
    commit_sha: str,
    match_count: int = 5
):
    response = (
        supabase
        .rpc(
            "match_code_chunks",
            {
                "query_embedding": query_embedding,
                "match_count": match_count,
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

def store_chunk(
    repo,
    commit_sha,
    file_path,
    chunk_index,
    content,
    embedding
):
    response = (
        supabase
        .table("code_chunks")
        .insert({
            "repo": repo,
            "commit_sha": commit_sha,
            "file_path": file_path,
            "chunk_index": chunk_index,
            "content": content,
            "embedding": embedding
        })
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
    commit_sha: str,
    match_count: int = 5
):
    response = (
        supabase
        .rpc(
            "match_code_chunks",
            {
                "query_embedding": query_embedding,
                "match_count": match_count,
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
