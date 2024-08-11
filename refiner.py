from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Directly set the OpenAI API key
api_key = os.getenv("OPENAI_AP_KEY")  # Replace with your actual API key

ORG_ID = ''
client = OpenAI( organization= ORG_ID, api_key= api_key)

def refine_text(text):
    """ Creates a refines the text and returns it """
    response = client.chat.completions.create(
        model ="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Refine this speech and make it sound like a native speaker. At the end give a percentage about how native the speech initially was and give detailed feedback about what parts didn't sound like a native speaker and what the correct way of saying it is for next time."
            },
            {
            "role": "user",
            "content": text
            }
        ],
        stream=False
    )
    return response.choices[0].message.content


def voice_to_text(recording_path):
    """ Converts voice to text and returns it"""
    with open(recording_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file,
        language="en"
    )
    return transcription.text


def refine(transcript):
    " refines recording and returns the refined text "
    refined_text = refine_text(transcript)
    print(refined_text)
    return refined_text

def save_chat(recording_path, transcript, refined_text):
    """ Saved the chat in a text file"""
    chat_file_name = recording_path.rstrip(".mp3").lstrip("recordings/")
    chat = "USER:\n" + transcript + "\n\nREFINED:\n" + refined_text
    with open(f"chats/{chat_file_name}.txt", "w") as f:
        f.write(chat)
    return chat