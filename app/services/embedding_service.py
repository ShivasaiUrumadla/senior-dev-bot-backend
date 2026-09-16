import time

from google import genai
from app.config import GEMINI_API_KEY


client = genai.Client(api_key=GEMINI_API_KEY)


def create_embedding(text: str):
    result = client.models.embed_content(
        model="gemini-embedding-2",
        contents=text
    )
    return result.embeddings[0].values



def create_embeddings(texts: list[str]):
    max_retries = 5

    for attempt in range(max_retries):
        try:
            result = client.models.embed_content(
                model="gemini-embedding-2",
                contents=texts
            )

            return [embedding.values for embedding in result.embeddings]

        except Exception as e:
            error_text = str(e)

            print(f"Embedding request failed: {error_text}")

            # Daily quota won't be fixed by waiting a few seconds.
            if "RequestsPerDay" in error_text:
                print("Daily embedding quota exhausted.")
                raise

            if attempt == max_retries - 1:
                print("Maximum retries reached.")
                raise

            wait_time = 10 * (2 ** attempt)

            print(f"Retrying in {wait_time} seconds...")
            time.sleep(wait_time)


import math


def cosine_similarity(vector1, vector2):
    dot_product = sum(a * b for a, b in zip(vector1, vector2))

    magnitude1 = math.sqrt(sum(a * a for a in vector1))
    magnitude2 = math.sqrt(sum(b * b for b in vector2))

    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0

    return dot_product / (magnitude1 * magnitude2)  