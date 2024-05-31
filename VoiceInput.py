import speech_recognition as sr


def take_input():
    r = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 100
            audio = r.listen(source, phrase_time_limit=5)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"You said: {query}")
            query = str(query)
            if query.strip():  # Check if the query is not empty
                return query.lower()
            else:
                print("No input detected. Listening again...")
        except sr.UnknownValueError:
            print("Sir, I could not understand audio. Please say it again.")
        except sr.RequestError:
            print("Sir, please kindly check your internet.")


print(take_input())
