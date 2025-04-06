
from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")





# 1) Configure your API key
client = genai.Client(api_key=api_key)





def get_chatbot_response(question: str, plans: list) -> str:
    client = genai.Client(api_key=api_key)
    # Combine plan textract stuff
    combined_plans_text = "\n".join(
        f"---\nPlan: {plan['name']}\n\n{plan['text']}"
        for plan in plans
    )

    # Prompting type
    prompt = f"""You are a healthcare plan assistant. Only use the text provided to answer user questions.

    Below is the text for multiple plans:
    {combined_plans_text}
    
    Answer the following question ONLY from the text above:
    
    Question: {question}
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt],
    )

    # 5) Return the text response
    return response.text





