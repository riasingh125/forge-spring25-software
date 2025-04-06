import google.generativeai as genai
from dotenv import load_dotenv
import os
# 1. Configure your API key

# load_dotenv()
# os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key='AIzaSyCuBim30wS6w5a03y_lKuQ8Ln6eW0_XAmA')

# 2. List all models available to your project
models = genai.list_models()

# 3. Print out each model's name and methods
for model in models:
    print(f"Model name: {model.name}")
    print(f"Supported generation methods: {model.supported_generation_methods}")
    print("-----")
