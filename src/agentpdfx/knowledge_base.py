from asyncore import readwrite

from agno.document.reader.pdf_reader import PDFReader
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.vectordb.chroma import ChromaDb
from agno.embedder.ollama import OllamaEmbedder


def create_pdf_knowledge_base(pdf_path: str, file_name: str) -> PDFKnowledgeBase:
    embedding_model = OllamaEmbedder(id='mxbai-embed-large',dimensions=1024)
    vector_store = ChromaDb(
        collection=f'{file_name}_document',
        embedder=embedding_model,
    )
    
    knowledge_base = PDFKnowledgeBase(
        path=pdf_path,
        vector_db=vector_store,
        reader=PDFReader(chunk=True)
    )

    knowledge_base.load(recreate=False)

    return knowledge_base
