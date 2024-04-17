import os
from dotenv import load_dotenv

import google.generativeai as genai


def main():
    load_dotenv()
    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

    model = genai.GenerativeModel('gemini-pro')

    user_question = "You are a professional ecologist and biologist. Don't say you're a professional ecologist and biologist. I need 3 promising sectors in the SDGs. Keep it professional and text in a readable way which sectors are best to look into. Briefly describe each sector. Do not say you are a professional ecologist and biologist."
    
    response = model.generate_content(user_question)

    if user_question:
        return response.text



if __name__ == "__main__":
    main()
