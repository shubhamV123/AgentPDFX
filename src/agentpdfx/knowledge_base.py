from asyncore import readwrite

from agno.document.chunking.document import DocumentChunking
from agno.document.reader.pdf_reader import PDFReader
from agno.knowledge.pdf import PDFKnowledgeBase
from agentpdfx.utils.vector_db import VectorDb, VectorDBConfig

def create_pdf_knowledge_base(pdf_path: str, file_name: str) -> PDFKnowledgeBase:
    vector_config = VectorDBConfig(
        db_type='chroma',
        index_name=f'{file_name}_document'
    )

    vector_store = VectorDb(vector_config)
    
    knowledge_base = PDFKnowledgeBase(
        path=pdf_path,
        vector_db=vector_store.db,
        reader=PDFReader(chunk=True),
        chunking_strategy=DocumentChunking()
    )

    knowledge_base.load(recreate=False)

    return knowledge_base
