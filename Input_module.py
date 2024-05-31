import random
from Assistant_details import name
from Output_module import output


def take_input():

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
        return take_input()
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

# import speech_recognition as sr


# def take_input():
#     r = sr.Recognizer()

#     while True:
#         with sr.Microphone() as source:
#             print("Listening...")
#             r.pause_threshold = 1
#             audio = r.listen(source, phrase_time_limit=5)

#         try:
#             print("Recognizing...")
#             query = r.recognize_google(audio, language="en-in")
#             print(f"You said: {query}")
#             query = str(query)
#             if query.strip():  # Check if the query is not empty
#                 return query.lower()
#             else:
#                 return "No input detected. Listening again..."
#         except sr.UnknownValueError:
#             return "Sir, I could not understand audio. Please say it again."
#         Except sr.RequestError:
#             return "Sir, please kindly check your internet."


'''------------------------------------------------------------------------------------------------------------------'''
# from Assistant_details import name
# def take_input():
#     # Use ANSI escape codes to color the output
#     print("\033[0m ", end="")

#     # Taking input from user.
#     i = input("\033[1m\033[32m>>> \033[32m")

#     # Reset terminal color to default
#     print("\033[0m", end=" ")

#     return i.lower() # This line indicates that this function returns user input in lower case irrespective of cases used by a user.

'''------------------------------------------------------------------------------------------------------------------'''
# def take_input():  # This function takes command line input from the user.
#     i = input("\033[1m>>> \033[0m")
#     return i.lower()
'''--------------------------------------- THE MOST IMP ELASTIC SEARCH ----------------------------------------------'''
# from Assistant_details import name
# from Output_module import output
# from elasticsearch import Elasticsearch

# # create an Elasticsearch client instance
# es = Elasticsearch(hosts=['localhost'])

# def take_input():
#     # Use ANSI escape codes to color the output
#     print("\033[0m ", end="")

#     # Taking input from user
#     i = input("\033[1m\033[32m>>> \033[32m")

#     # Reset terminal color to default
#     print("\033[0m", end=" ")

#     # Index the user input in Elasticsearch
#     es.index(index='user_input_index', body={'input': i})

#     # If the input is just the assistant name, greet them and prompt for input again
#     if i.lower() == name.lower():
#         output("Yes Sir! How can I assist you?")
#         return take_input()
#     # If the input includes the assistant's name and other input, remove it before returning the query
#     elif i.lower().startswith(name.lower()+' ') or i.lower().startswith(name.lower()+',') or i.lower().startswith(name.lower()+'.') or i.lower().startswith(name.lower()+'!') or i.lower().startswith(name.lower()+'?'):
#         query = i[len(name)+1:].strip()
#         # If the query is empty, just return an empty string
#         if not query:
#             return ""
#         # Otherwise, return the query without the assistant name
#         else:
#             return query
#     else:
#         return i.lower()
# take_input()
