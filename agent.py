from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.providers.ollama import OllamaProvider

provider = OllamaProvider(
    base_url="http://127.0.0.1:11434/v1"
)

model = OllamaModel(
    "qwen3:8b",
    provider=provider
)

agent = Agent(model)