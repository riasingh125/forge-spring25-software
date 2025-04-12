
from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")



# 1) Configure your API key
client = genai.Client(api_key=api_key)


def get_system_prompt(combined_plans_text, user_experience, question, user_info):
    prompt = f"""You are a healthcare plan assistant. Only use the text provided to answer user questions.
        Below is the text for multiple plans:
        {combined_plans_text}
        The user experience level is with healthcare plans is {user_experience}.
        Use the associated score to justify each plan and its ranking.
        The user experience level is {user_experience} and there info is {user_info}
        Answer the following question ONLY from the text above:
        Question: {question}
        """
    return prompt


def get_chatbot_response(question: str, history: dict) -> str:
    client = genai.Client(api_key=api_key)

    prompt = get_system_prompt(history["combined_plan_text"], history["experience"], question, str(history["user_info"]))

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt],
    )

    # Return the text response
    return response.text





