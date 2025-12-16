import os
import google.generativeai as genai

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY not found. Set it using: setx GEMINI_API_KEY \"your_key\""
    )

genai.configure(api_key=API_KEY)