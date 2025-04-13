from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")




def get_chatbot_response(question: str, session_history: dict) -> str:
    client = genai.Client(api_key=api_key)

    query = session_history["prompt"]

    # Prompting type
    query += f"""You are a healthcare plan assistant. Only use the text provided to answer user questions.
    Answer the following question ONLY from the text above:
    
    Question: {question}
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[query],
    )

    # 5) Return the text response
    return response.text





