from app.services.github_service import get_repository_files
from app.services.chunking_service import chunk_code
from app.services.embedding_service import create_embeddings
from app.services.vector_store_service import store_chunk, store_chunks


def index_repository(repo: str, token: str, ref: str):

    files = get_repository_files(
        repo=repo,
        token=token,
        ref=ref
    )
    print("chunking files:", len(files))
    all_chunks = []

    for file in files:
        file_path = file["path"]
        content = file["content"]

        chunks = chunk_code(content)

        for chunk_index, chunk in enumerate(chunks):
            all_chunks.append({
                "file_path": file_path,
                "chunk_index": chunk_index,
                "content": chunk
            })

    print("Total chunks to index:", len(all_chunks))


    batch_size = 10
    total_chunks = 0
    

    for start in range(0, len(all_chunks), batch_size):

        batch = all_chunks[start:start + batch_size]

        texts = [item["content"] for item in batch]

        embeddings = create_embeddings(texts)

        rows = []

        for item, embedding in zip(batch, embeddings):

            rows.append({
                "repo": repo,
                "commit_sha": ref,
                "file_path": item["file_path"],
                "chunk_index": item["chunk_index"],
                "content": item["content"],
                "embedding": embedding
            })

        store_chunks(rows)

        total_chunks += len(rows)

        print(
            f"Indexed {total_chunks}/{len(all_chunks)} chunks"
        )

    return total_chunks