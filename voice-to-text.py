import speech_recognition as sr

# Initialize the recogonizer
r = sr.Recognizer()

def record_text():
    # Loop in case of error
    full_text = ""
    while(True):
        try:
            # use michrophone as input
            with sr.Microphone() as source2:
                # Prepare recognizer to receive input
                r.adjust_for_ambient_noise(source2, duration=0.2)
                # Listens for user input
                audio2 = r.listen(source2)
                # Use google to recognize the audio
                text = r.recognize_google(audio2) + " "
                if text == "stop ":
                    print("\nListening Stoped.")
                    return full_text
                full_text += text

        except sr.RequestError as e:
            print("Could not request results. " + e)
        except sr.UnknownValueError as e:
            print("Unknown error")

def create_text_file(text):
    with open("recording.txt", "w") as f:
        f.write(text)

if __name__ == "__main__":
    print("Listening...")
    text = record_text()
    create_text_file(text)
