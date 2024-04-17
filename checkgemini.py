from dotenv import load_dotenv

import os
import google.generativeai as genai

def main():
    load_dotenv()

    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
    model = genai.GenerativeModel('gemini-pro')
    user_question = """As an expert in environmental sustainability and development, you have in-depth knowledge of the key players in the cleantech and sustainability market. Your mission is to present up-and-coming leaders in the field, highlighting their contributions to environmental protection and green technology development. Keeping a professional and informative style, highlight three companies that are pioneers in their fields, focusing on their environmental responsibility and innovative developments. Emphasize how their activities contribute to creating a sustainable future without mentioning the investment aspects. Consider companies demonstrating leading practices in renewable energy, carbon reduction and sustainable product development. Include only the names of the companies and their core businesses, creating a narrative that inspires readers to think about the importance of environmental sustainability and support these leaders."""
    response = model.generate_content(user_question)
    if user_question:
        return response.text

if __name__ == "__main__":
    main()
