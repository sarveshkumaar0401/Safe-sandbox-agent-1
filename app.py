from fastapi import FastAPI
from pydantic import BaseModel # useing BaseModel automatically validates the incoming request data and provides a structured way to define the expected data format. It also allows for easy serialization and deserialization of data, making it easier to work with JSON requests and responses.
from agent_tools import agent
from db import create_user_if_not_exists, save_message, get_user_history

app = FastAPI()

class Chat(BaseModel):
    user_id: str
    message: str


@app.post("/chat")
def chat(request: Chat):
    history = get_user_history(
    request.user_id
)
    result = agent.run_sync(request.message)
    context = ""

    for prompt, response in history:
        context += f"User: {prompt}\n"
        context += f"Assistant: {response}\n"

    context += f"User: {request.message}"

    result = agent.run_sync(context)

    create_user_if_not_exists(
    request.user_id
    )   
    usage = result.usage

    save_message(
    user_id=request.user_id,
    prompt=request.message,
    response=result.output,
    input_tokens=usage.input_tokens,
    cached_input_tokens=usage.cache_read_tokens,
    output_tokens=usage.output_tokens,
    cost_usd=0.0
)
    return {
        "response": result.output
    }