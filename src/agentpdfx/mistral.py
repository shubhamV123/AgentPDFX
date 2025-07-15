import os

from agno.agent import Agent, RunResponse
from agno.models.mistral import MistralChat
from agentpdfx.config import settings
agent = Agent(
    model=MistralChat(
        id="mistral-medium-2505",
        api_key=settings.mistral_api_key,
    ),
    markdown=True,

)

# Print the response in the terminal
agent.print_response("What is stock price of RIL in NSE market?")