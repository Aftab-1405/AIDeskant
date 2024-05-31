"""------------------------------------------------- NEW -------------------------------------------------------------"""
from Output_module import output
from Assistant_details import name
import random
import speech_recognition as sr
import threading
import Assistant_details
from Assistant_details import about_assistant
from Feature_module import *
from GPTModule import chat_with_openai
from Internet import check_on_wikipedia, search_on_google
from Music_module import *
from Speak_module import *
from StoreNew_QA_Module import direct_store_new_question, store_question
from Time_module import get_time, get_date
from Web_module import *


def process(query):
    answer = get_answer_from_memory(query)
    predefined_answers = ["weather", "start chatgpt", "update user name", "user name", "tell me about yourself",
                          "change your voice", "start calculator", "close chrome", "close firefox", "start youtube",
                          "add new question", "change your name", "get my name", "start voice command",
                          "get time details", "check internet connection", "tell date", "on speak", "off speak",
                          "open browser", "open chrome", "open firefox", "close browser", "play music", "stop music",
                          "resume music", "close media player", "change volume", "open vscode", "change name",
                          "change wallpaper"]

    if answer in predefined_answers:

        if answer == "tell me about yourself":

            return about_assistant()

        elif answer == "user name":
            return get_user_name_from_database()

        elif answer == "update user name":
            return update_user_name()

        elif answer == "start chatgpt":
            return chat_with_openai()

        elif answer == "get time details":
            return "Time is " + str(get_time())

        elif answer == "check internet connection":
            if check_internet_connection():
                return "Internet is connected!"
            else:
                return "Internet is not connected."

        elif answer == "tell date":
            return "Date is: " + get_date()

        elif answer == "on speak":
            return turn_on_speech()

        elif answer == "off speak":
            return turn_off_speech()

        elif answer == "weather":
            return weather_forecast()

        elif answer == "start calculator":
            return calculator()

        elif answer == "add new question":
            return direct_store_new_question()

        elif answer == "open browser":
            t = threading.Thread(target=open_browser)
            t.start()
            return "Opening browser! Please wait."

        elif answer == "open chrome":
            t = threading.Thread(target=open_chrome)
            t.start()
            return "Opening chrome! Please wait."

        elif answer == "close chrome":
            return close_chrome()

        elif answer == "open firefox":
            t = threading.Thread(target=open_firefox)
            t.start()
            return "Opening firefox! Please wait."

        elif answer == "close firefox":
            return close_firefox()

        elif answer == "close browser":
            t = threading.Thread(target=close_browser)
            t.start()
            return "Closing browser! Please wait."

        elif answer == "play music":
            t = threading.Thread(target=play_random_music)
            t.start()
            return "Playing music, Please wait."

        elif answer == "stop music":
            t = threading.Thread(target=pause_media_player)
            t.start()
            return "Music has been stopped."

        elif answer == "resume music":
            t = threading.Thread(target=resume_media_player)
            t.start()
            return "Music has been resumed."

        elif answer == "close media player":
            t = threading.Thread(target=close_media_player)
            t.start()
            return "Media player has been closed."

        elif answer == "change volume":
            change_volume()
            return "Volume level has been changed."

        elif answer == "start youtube":
            return youtube_search()

        elif answer == "get my name":
            return get_assistant_name()

        elif answer == "change your voice":
            return change_voice()

        elif answer == "change wallpaper":
            set_wallpaper()
            return "Wallpaper has been changed."

        # Can I make a function for this? I will think about it.
        elif answer == "change your name":
            output("Okay! What do you want to call me? ")
            temp = take_input()

            if temp == Assistant_details.name:
                return "Can't change. I think you are happy with my old name."
            else:
                update_name(temp)
                Assistant_details.name = temp
                return "Now you can call me : " + temp

    database_answer = get_answer_from_memory(query)

    if database_answer != "":
        return database_answer
    else:
        if check_internet_connection():
            # Search on Wikipedia
            output(f"Sir, I'm searching on Wikipedia for {query}.")
            wiki_answer = check_on_wikipedia(query)
            if wiki_answer != "":
                return f"According to Wikipedia, {wiki_answer}"
            elif wiki_answer == "":
                # Search on Google
                output(
                    f"Couldn't get relevant information for {query}.\nSearching on the web for, Please wait for the results.")
                time.sleep(0.25)  # Wait for 0.25 seconds
                search_on_google(query)
                output(f"That's what I found on the web for: {query}")
                output(
                    f"Sir, If you wants to store your own answer for ({query}) then enter: (Yes)")
                command = take_input()
                if command == "yes":
                    store_question(query)
                else:
                    return "Okay Sir, I won't continue further."
        else:
            return "Sorry sir, I encountered an error while processing your request. Please kindly check your internet connection."


"""------------------------------------------------------------------------------------------------------------------"""


def take_input():
    # Initialize speech recognition
    r = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, phrase_time_limit=5)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"You said: {query}")
            query = str(query)
            return query.lower()

        except sr.UnknownValueError:
            return "Sir, I could not understand audio. Please say it again."
        except sr.RequestError:
            return "Sir, please kindly check your internet."


def text_input():
    while True:
        # Taking input from user
        i = input("\033[1m\033[32m>>> \033[32m")
        i = i.replace("who is", "")
        i = i.replace("tell me about", "")
        # Reset terminal color to default
        print("\033[0m", end="")

        # If the input is just the assistant name, greet them and prompt for input again
        if i.lower() == name.lower():
            assistant_responses = random.choice(["Yes, how can I assist you today?", "How may I be of help?",
                                                 "I'm here to assist you. What can I do for you?",
                                                 "Hello! What can I do for you today?",
                                                 "How can I be of service?", "At your service! What can I help you with?",
                                                 "Hi there! What can I do for you?", "What can I assist you with?",
                                                 "Hello! How can I be of assistance?", "What can I help you with today?",
                                                 "How may I assist you?", "Hello there! How can I help you today?",
                                                 "What can I do for you?", "Yes, how can I help you today?",
                                                 "What can I assist you with today?", "How can I be of service to you?",
                                                 "Hi there! How can I assist you?", "What do you need help with?",
                                                 "How may I assist you today?", "What can I do for you today?",
                                                 "Hello! How can I assist you?", "What can I help you with today?",
                                                 "How can I assist you?", "What can I do for you today?",
                                                 "How may I be of help?"])

            output(assistant_responses)
        # If the input includes the assistant's name and another input, remove it before returning the query
        elif i.lower().startswith(name.lower() + ' ') or i.lower().startswith(name.lower() + ',') or i.lower().startswith(
                name.lower() + '.') or i.lower().startswith(name.lower() + '!') or i.lower().startswith(name.lower() + '?'):
            query = i[len(name) + 1:].strip()
            # If the query is empty, just return an empty string
            if not query:
                return ""
            # Otherwise, return the query without the assistant name
            else:
                return query
        else:
            return i.lower()


def take_input_mode():
    while True:
        mode = input("Enter the input mode (text/voice): ")
        if mode.lower() == "text":
            return text_input
        elif mode.lower() == "voice":
            return take_input
        else:
            print("Invalid input. Please enter 'text' or 'voice'.")


def main():
    input_mode = take_input_mode()
    while True:
        query = input_mode()
        if query.lower() == "switch to chat mode":
            input_mode = text_input
        # Add more conditions for switching modes if desired
        else:
            # Process the query and perform appropriate actions
            # Your code for processing the query goes here
            pass


if __name__ == "__main__":
    main()
"""-------------------------------------------------------------------------------------------------------------"""
