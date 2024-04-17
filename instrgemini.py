
from dotenv import load_dotenv

import os
import google.generativeai as genai

def main():
    load_dotenv()

    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
    model = genai.GenerativeModel('gemini-pro')
    user_question = """ Talk about three eco tools that can help the environment. Provide three different tools and application features designed to support an environmentally responsible approach. These include, for example, a carbon footprint calculator, analytical tools for assessing the environmental impact of companies, and other such tools that you will talk about for examples. Write it professionally and clearly."""
    response = model.generate_content(user_question)
    if user_question:
        return response.text

if __name__ == "__main__":
    main()
