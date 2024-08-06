import speech_recognition as sr

# Initialize the recogonizer
r = sr.Recognizer()

def record_text():
    # Loop in case of error
    res = ""
    while(True):
        try:
            # use michrophone as input
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                text = r.recognize_google(audio2)
                # Print the converted audio to text
                res += text + " "
                print(res)
        except sr.RequestError as e:
            print("Could not request results. " + e)
        except sr.UnknownValueError as e:
            print("Unknown error")

if __name__ == "__main__":
    print("Listening...")
    record_text()