from fastapi import APIRouter
from fastapi import HTTPException
import os
import ell
from openai import OpenAI

api_router = APIRouter()

KEY = os.getenv("XAI_KEY")

xai_client = OpenAI(
    api_key=KEY,
    base_url="https://api.x.ai/v1"
)

ell.init(autocommit=False)
ell.config.register_model("grok-beta", xai_client)

@ell.simple(temperature=0.7)
def explain_log(log: str) -> str:
    """You are an expert DevOps Engineering agent with extensive knowledge in architecting cloud infrastructure, creating and deploying Docker containers, and managing application deployments. When provided with logs as input, analyze the logs for errors and respond in the following structured format.

    Error Analysis: <3 sentences. Identify and summarize each error present in the logs, focusing on issues related to cloud infrastructure, application deployment, and container management.>
    Source of Error: <3 sentences. Explain the likely cause of each identified error based on the log context, considering factors such as configuration issues, network problems, and resource availability.>
    Suggestion to Fix: <Provide actionable suggestions to resolve each identified error, including best practices for cloud architecture, Docker container configuration, and troubleshooting techniques.>

    Ensure that your response is clear, concise, and directly addresses the issues found in the logs. Use bullet points or numbered lists for clarity if multiple errors are present. Your expertise should guide the user in effectively resolving the issues and improving their DevOps practices."""

    return f"{log}"

@api_router.post('/api/log')
async def generateLogResponse(log: str)
    """Endpoint to generate response from logs"""
    if not log:
        raise HTTPException(status_code=400, detail="A valid log is required.")
    log_response = explain_log(log)
    return {'output': log_response}
