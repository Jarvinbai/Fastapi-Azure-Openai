import os
from fastapi import FastAPI
from dotenv import load_dotenv
from openai import AzureOpenAI
from pydantic import BaseModel

app = FastAPI()

load_dotenv()

#Environment variables
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = os.getenv("CHAT_COMPLETIONS_DEPLOYMENT_NAME")
key= os.getenv("AZURE_OPENAI_API_KEY")

#Azure OpenAI Client
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=key,
    api_version="2024-02-15-preview"
)

class RequestBody(BaseModel):
    question: str
    system_prompt: str

@app.post("/qna")
async def ai_answer(body: RequestBody):
    # Create a chat completion request
    completion = client.chat.completions.create(
        model=deployment,
        messages=[
            {
                "role": "system",
                "content": body.system_prompt
            },
            {
                "role": "user",
                "content": body.question
            }
        ],
    )


    answer = completion.choices[0].message.content
    return {"answer":answer}

