from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Directly set the OpenAI API key
api_key = os.getenv("OPENAI_AP_KEY")  # Replace with your actual API key

ORG_ID = ''
client = OpenAI( organization= ORG_ID, api_key= api_key)

def refine(text):
    """ Creates a refines the text and returns it """
    response = client.chat.completions.create(
        model ="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Refine this speech and make it sound like a native speaker. If it is already correct and sounds like a native speaker just return CORRECT. "
            },
            {
            "role": "user",
            "content": text
            }
        ],
        stream=False
    )
    return response.choices[0].message.content