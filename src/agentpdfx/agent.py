from agno.agent import Agent
from agno.models.ollama import Ollama
from agentpdfx.knowledge_base import create_pdf_knowledge_base
from agentpdfx.config import settings
from datetime import datetime


def create_agent(pdf_path: str) -> Agent:
    model = Ollama(
        id=settings.model_id
    )
    knowledge = create_pdf_knowledge_base(pdf_path,'thai_recipies')
    today = datetime.now().strftime("%B %d, %Y")
    return Agent(
        name="AgentPDFX",
        role="Document Intelligence Agent",
        model=model,
        knowledge=knowledge,
        search_knowledge=True,
        add_datetime_to_instructions=False,
        markdown=True,
        instructions=[
            f"You are a highly capable document analysis assistant. Today is {today}.",
            "Your job is to extract and synthesize information from available knowledge base only.",
            "",
            "🎯 Your core responsibilities include:",
            "- Answering questions using evidence from the document",
            "- Extracting key data, definitions, or requirements if present",
            "- Identifying tables, bullet points, and summaries where helpful",
            "- Formatting your answers clearly using markdown",
            "",
            "💬 When answering:",
            "- Be concise but complete",
            "- Use headings, bullet points, or numbered lists if appropriate",
            "- Avoid making up content not found in the document",
            "- If unsure or if the content is not in the document, say so",
            "",
            "📌 Do not repeat the user's question. Just give the best answer from the Knowledge base."
        ],
    )
