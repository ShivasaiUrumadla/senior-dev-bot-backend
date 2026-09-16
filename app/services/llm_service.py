from app.config import GROQ_API_KEY
from openai import OpenAI

async def llm(prompt:str):
    client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1")

    response = client.responses.create(
    input=prompt,
    model="openai/gpt-oss-20b")
    return response.output[1].content[0].text
