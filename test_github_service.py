# from app.services.github_app_service import generate_installation_token
# from app.services.github_service import get_file_content


# repo = "ShivasaiUrumadla/trial"
# installation_id = 159061250

# token = generate_installation_token(installation_id)

# content = get_file_content(
#     repo=repo,
#     file_path="main.py",   # change this to a real file in your repo
#     token=token,
#     ref="main"
# )

# print(content)



# from app.services.github_app_service import generate_installation_token
# from app.services.github_service import get_changed_files


# repo = "ShivasaiUrumadla/trial"
# installation_id = 159061250
# pr_number = 4   # change this to your actual PR number

# token = generate_installation_token(installation_id)

# files = get_changed_files(
#     repo=repo,
#     pr_number=pr_number,
#     token=token
# )

# for file in files:
#     print(file["filename"], "-", file["status"])






# from app.services.github_app_service import generate_installation_token
# from app.services.github_service import get_pr_context


# repo = "ShivasaiUrumadla/trial"
# installation_id = 159061250
# pr_number = 4
# ref = "update-1"

# token = generate_installation_token(installation_id)

# context = get_pr_context(
#     repo=repo,
#     pr_number=pr_number,
#     token=token,
#     ref=ref
# )

# print(context)
# from app.services.github_app_service import generate_installation_token
# from app.services.github_service import get_repository_files

# files = get_repository_files(
#     repo="ShivasaiUrumadla/trial",
#     token=generate_installation_token(159061250),
#     ref="15b00fa8be63b29dbd69d65f290fff769f2aa3b6"
# )

# print(files)

# from app.services.chunking_service import chunk_code


# code = """
# def calculate_total(product_price, quantity):
#     return product_price * quantity


# def create_order(db, user_id, product_price, quantity):
#     total = calculate_total(product_price, quantity)

#     payment_status = process_payment(user_id, total)

#     if payment_status:
#         return {
#             "user_id": user_id,
#             "total": total,
#             "status": "confirmed"
#         }
# """


# chunks = chunk_code(code)

# for i, chunk in enumerate(chunks):
#     print(f"\n--- CHUNK {i} ---")
#     print(chunk)

# from app.services.embedding_service import create_embedding


# code = """
# def calculate_total(product_price, quantity):
#     return product_price * quantity
# """

# embedding = create_embedding(code)

# print("Vector length:", len(embedding))
# print("First 10 values:", embedding[:10])


# from app.services.embedding_service import (
#     create_embedding,
#     cosine_similarity
# )


# code1 = """
# def calculate_total(price, quantity):
#     return price * quantity
# """

# code2 = """
# def get_total_cost(price, amount):
#     return price * amount
# """

# code3 = """
# def connect_database():
#     print("Connecting to database")
# """


# embedding1 = create_embedding(code1)
# embedding2 = create_embedding(code2)
# embedding3 = create_embedding(code3)

# print("code1 vs code2:", cosine_similarity(embedding1, embedding2))
# print("code1 vs code3:", cosine_similarity(embedding1, embedding3))


# from app.services.embedding_service import create_embedding
# from app.services.vector_store_service import store_chunk


# code = """
# def calculate_total(price, quantity):
#     return price * quantity
# """

# embedding = create_embedding(code)

# result = store_chunk(
#     repo="ShivasaiUrumadla/trial",
#     file_path="orders.py",
#     chunk_index=0,
#     content=code,
#     embedding=embedding
# )

# print(result)



# from app.services.github_app_service import generate_installation_token
# from app.services.indexing_service import index_repository


# installation_token = generate_installation_token(159061250)

# total = index_repository(
#     repo="ShivasaiUrumadla/trial",
#     token=installation_token,
#     ref="15b00fa8be63b29dbd69d65f290fff769f2aa3b6"
# )

# print("Total chunks indexed:", total)


# diff = """
# diff --git a/orders.py b/orders.py
# index 123..456
# --- a/orders.py
# +++ b/orders.py
# @@
#  def calculate_total(product_price, quantity):
# -    return product_price * quantity
# +    return product_price + quantity
# """
# from app.services.embedding_service import create_embedding
# from app.services.vector_store_service import search_similar_chunks


# query_embedding = create_embedding(diff)

# results = search_similar_chunks(
#     query_embedding=query_embedding,
#     repo="ShivasaiUrumadla/trial",
#     commit_sha="15b00fa8be63b29dbd69d65f290fff769f2aa3b6",
#     match_count=5
# )

# for result in results:
#     print("\n----------------")
#     print("File:", result["file_path"])
#     print("Chunk:", result["chunk_index"])
#     print("Similarity:", result["similarity"])
#     print("Content:")
#     print(result["content"])




#     total_characters = 0

#     for file in files:
#         total_characters += len(file["content"])

#     print("Total source files:", len(files))
#     print("Total characters:", total_characters)



#     total_chunks = 0

#     for file in files:
#         chunks = chunk_code(file["content"])
#         total_chunks += len(chunks)

#     print("Total chunks:", total_chunks)

# from app.services.embedding_service import create_embeddings


# texts = [
#     "def calculate_total(price, quantity): return price * quantity",
#     "def process_payment(user_id, amount): ...",
#     "def get_user(user_id): ...",
#     "def connect_db(): ...",
#     "def create_order(...): ...",
#     "def test_calculate_total(): ...",
#     "def test_payment(): ...",
#     "database connection logic",
#     "order processing logic",
#     "payment validation logic"
# ]

# embeddings = create_embeddings(texts)

# print("Number of embeddings:", len(embeddings))
# print("Vector length:", len(embeddings[0]))
# print("First 5 values:", embeddings[0][:5])


# from app.services.github_service import get_repository_files

# from app.services.chunking_service import chunk_code
# from app.services.github_app_service import generate_installation_token
# from app.services.indexing_service import index_repository
# if __name__ =="__main__":
#     installation_token = generate_installation_token(160253776)
#     repo_name = "Bhargavi-urumadla/shopsmart-ai"
#     pr_number = 24
#     base_sha = "ed821e6e48013f581b8a5d12826d8ca8d5875913"
#     index_repository(repo=repo_name, token=installation_token, ref=base_sha)


# from app.services.embedding_service import create_embedding


# if __name__ =="__main__":
#     embedding = create_embedding("hello world")
#     print(len(embedding))



from app.services.github_app_service import generate_installation_token

token = generate_installation_token(159061250)

print("Token generated:", token is not None)