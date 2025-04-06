
from langchain.text_splitter import RecursiveCharacterTextSplitter  # read more here: https://python.langchain.com/api_reference/text_splitters/character/langchain_text_splitters.character.RecursiveCharacterTextSplitter.html#recursivecharactertextsplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# pip install langchain openai faiss-cpu tiktoken python-dotenv

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

splitter = RecursiveCharacterTextSplitter(
    chunk_size = CHUNK_SIZE,
    chunk_overlap = CHUNK_OVERLAP,
    separators=["\n\n", "\n", ".", " "]
)

embeddings = OpenAIEmbeddings()

# Convert Textract into Documents for vector embedding
def get_documents(history):
    documents = []
    print('history is ')
    print(history)
    for plan in history['plans']:
        chunks = splitter.split_text(plan['text'])
        for chunk in chunks:
            documents.append(Document(
                page_content = chunk,
                metadata = {"plan_name": plan['name']}
            ))
    return documents


# Add the role to chatbot
system_message = SystemMessage(
    content="You are a healthcare plan assistant. Help users clearly understand plan details like deductibles, copays, and coverage. Be concise, accurate, and only use information from the provided documents."
)

custom_prompt = ChatPromptTemplate.from_messages([
    system_message,
    HumanMessage(content="{question}")
])

def get_chatbot_response(message: str, history):
    documents = get_documents(history)
    if  len(documents) == 0:
        return "Error: Cannot access PDF data"
    vectors = FAISS.from_documents(documents, embeddings)
    qa = RetrievalQA.from_chain_type(
        llm = ChatOpenAI(),
        retriever = vectors.as_retriever(),
        chain_type_kwargs = {"prompt": custom_prompt}
    )
    response = qa.run(message)
    return response







