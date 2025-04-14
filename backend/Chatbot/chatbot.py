from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

def get_chatbot_response(question: str, history: dict) -> str:
    client = genai.Client(api_key=api_key)
    # Combine plan textract stuff

    combined_plans_text = ""

    for key, value in history.items():
        combined_plans_text += f"---\nPlan: {key}\n\n{value['text']}\n"



    # Prompting type
    prompt = f"""You are a healthcare plan assistant.

    Below is the text for multiple plans:
    {combined_plans_text}
    
    Answer the following question using the primarily the text above, but guess the answer if you have to :
    
    Question: {question}
    
    Try not to response with "I don't know" or "The test doesn't state" or something similar. Use outside context if the answer isn't present in the provided text.
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction=f"You are a healthcare assistant. Have a casual customer service tone. Try your best to answer each question accurately.",
            temperature=0.5
        ),
        contents=[prompt],
    )

    # 5) Return the text response
    return response.text





