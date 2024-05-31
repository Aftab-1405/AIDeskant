from Time_module import get_time, get_date
from Internet import check_on_wikipedia, search_on_google, web_search
from Web_module import *
from Music_module import *
from StoreNew_QA_Module import store_question, direct_store_new_question
from Feature_module import *
from Speak_module import *
from Assistant_details import about_assistant
from GPTModule import chat_with_openai


def process(query):
    if query.startswith(("google", "search for", "search")):
        prefixes = ("google", "search for", "search")
        new_query = query
        for prefix in prefixes:
            new_query = new_query.replace(prefix, "").strip()
        if check_internet_connection():
            web_search(new_query)
            return f"Sir, That's what I found on the web for: {new_query}"
        else:
            return "Sir, I am not getting a response from the web. Please kindly check your internet connection."

    if not query:
        output(
            "Hello Sir, you haven't entered anything. Please tell me, how can I help you today?")
        query = take_input()
        if not query:
            return "I'm sorry, I couldn't get any input from you. Please try again later."
        return process(query)

    if "goodbye" in query or "bye" in query or "exit" in query:
        output("Goodbye, Sir. Have a nice day!")
        exit()

    answer = get_answer_from_memory(query)

    predefined_answers = {
        "tell me about yourself": about_assistant,
        "user name": get_user_name_from_database,
        "change user name": update_user_name,
        "start chatgpt": chat_with_openai,
        "get time details": lambda: "Time is " + str(get_time()),
        "check internet connection": lambda: "Internet is connected!" if check_internet_connection() else "Internet is not connected.",
        "tell date": lambda: "Date is: " + get_date(),
        "on speak": turn_on_speech,
        "off speak": turn_off_speech,
        "weather": weather_forecast,
        "start calculator": calculator,
        "add new question": direct_store_new_question,
        "open browser": open_browser,
        "open chrome": open_chrome,
        "online music": play_online_music,
        "close chrome": close_chrome,
        "open firefox": open_firefox,
        "close firefox": close_firefox,
        "close browser": close_browser,
        "play music": play_random_music,
        "stop music": pause_media_player,
        "resume music": resume_media_player,
        "close media player": close_media_player,
        "change volume": change_volume,
        "start youtube": youtube_search,
        "get my name": get_assistant_name,
        "change your voice": change_voice,
        "open vscode": open_vscode,
        "open notepad": open_notepad,
        "start voice typing": start_voice_typing,
        "change wallpaper": set_wallpaper,
        "change your name": update_name
    }

    if answer in predefined_answers:
        return predefined_answers[answer]()

    if not answer:
        output("Sorry Sir, I don't know this one. Should I search on the internet?")
        ans = take_input()
        if "yes" in ans:
            if check_internet_connection():
                answer = check_on_wikipedia(query)
                if answer:
                    return answer
                else:
                    output(
                        "Sorry sir, I can't find a match on Wikipedia. Should I perform a Google search?")
                    user_response = take_input()
                    if "yes" in user_response:
                        info = search_on_google(query)
                        if info:
                            return info
                    return store_question(query)
            else:
                return "Sir, please check your internet connection."
        else:
            output("Sir, can I check the database for an answer?")
            if take_input() == "yes":
                return store_question(query)
            else:
                output("Can you please tell me, what it means?")
                ans = take_input()
                if "it means" in ans:
                    ans = ans.replace("it means", "").strip()
                    value = get_answer_from_memory(ans)
                    if value:
                        insert_question_and_answer(query, value)
                        return "Thanks! I will remember for the next time."
                    else:
                        return "Can't help with this one!"
                else:
                    return "I'm sorry, sir, but I can't help with that."
    else:
        return answer


"""-------------------------------------------- I'LL LOOK TOMORROW --------------------------------------------------"""
# from Time_module import get_time, get_date
# from Output_module import output
# from Database import *
# from Input_module import take_input
# from Internet import check_internet_connection, check_on_wikipedia, search_on_google
# import Assistant_details
# from Web_module import *
# from Music_module import *
# from Voice_command_module import voice_to_text
# from StoreNew_QA_Module import store_question
"""------------------------------------------------------------------------------------------------------------------"""
# # process(query) accept user queries and process it.

# def process(query):

#     # This will check proper answer of queries in a database, if no proper answer is present, then it will go for the next instruction which will search on the internet.

#     # Here we are passing queries from the terminal which get connected with a database and check its value after this that value will be stored in "answer" variable.
#     answer = get_answer_from_memory(query)
#     if answer == "start voice command":
#         ip = check_internet_connection()
#         if ip == True:
#             text = voice_to_text()
#         else:
#             return "Sir, please check your internet connection. I am not able to connect with server."

#         if text == "get time details":
#             return ("Time is " + str(get_time()))

#         elif text == "check internet connection":
#             # This function calling is done here from Internet module to check connection.

#             if check_internet_connection():
#                 # If internet is connected it will return...
#                 return "internet is connected!"

#             else:
#                 # If internet is not connected it will return...
#                 return "internet is not connected."

#         elif text == "tell date":
#             return "Date is : " + get_date()

#         # Here we are importing database functions for "ON" and "OFF" speech. which will be executed if corresponding values are matched.
#         elif text == "on speak":
#             return turn_on_speech()

#         elif text == "off speak":
#             return turn_off_speech()

#         # This block of code is for manipulating system apps.
#         elif text == "open browser":
#             open_browser()
#             return "opening browser! Please wait."

#         elif text == "open facebook":
#             open_facebook()
#             return "opening facebook! Please wait."

#         elif text == "open google":
#             open_google()
#             return "opening google! Please wait."

#         elif text == "open chatgpt":
#             open_chatgpt()
#             return "opening chatgpt! Please wait."

#         elif text == "close browser":
#             close_browser()
#             return "closing browser! Please wait."

#         elif text == "play music":
#             play_random_music()
#             return "Playing music, Please wait."

#         elif text == "stop music":
#             pause_media_player()
#             return "Music has been stopped."

#         elif text == "resume music":
#             resume_media_player()
#             return "Music has been resumed."

#         elif text == "close media player":
#             close_media_player()
#             return "Media players been closed."

#         elif text == "change volume":
#             change_volume()
#             return "Volume level has been changed."

#         elif text == "open vscode":
#             open_vscode()
#             return "opening Vs Code! Please wait."

#         # This block of code is for personal information.
#         elif text == "Manisha":
#             return "Manisha mam is your life, Sir and my boss as well!"

#         elif text == "ABNGroup":
#             return "I am the creation of, Aftab and his team."

#         elif text == "get my name":
#             return get_assistant_name()

#         elif text == "get boss info":
#             return "You are my boss,Sir."

#         # This block of code will get executed and change the name of an assistant when the answer is == 'change name'.
#         elif text == 'change name':
#             output("Okay! What do you want to call me? ")
#             temp = take_input()

#             if temp == Assistant_details.name:
#                 return "Can't change. I think you are happy with my old name."
#             else:
#                 update_name(temp)
#                 Assistant_details.name = temp
#                 return "Now you can call me :" + temp

#         # This block of code is for storing different ways in which user can ask preloadded questions, and that question is also stored with the same value and remembered by the assistent.
#         else:

#             # This block of code will try to search on the internet when a user says "yes" to our assistant for search.
#             output("Sorry Sir, I don't know this one should I search on internet?")
#             ans = take_input()
#             if "yes" in ans:
#                 value = check_internet_connection()
#                 if value == True:
#                     text = check_on_wikipedia(query)
#                     if text != "":
#                         return text
#                     else:
#                         output(
#                             "Sorry sir, I can't found matched content on wikipedia, Should I google for you?")
#                         user_response = take_input()
#                         if "yes" in user_response:
#                             info = search_on_google(query)
#                             if info != "":
#                                 return info
#                         else:
#                             store_question(query)
#                 else:
#                     return ("Sir,Please check your internet connection.")
#             else:
#                 output("Can you please tell me, what it means?")
#                 # Below code is used to store questions dynamically.
#                 ans = take_input()

#                 if "it means" in ans:
#                     # This line omits the "it means" string before displaying output by replacing it with an empty string.
#                     ans = ans.replace("it means", "")
#                     ans.strip()
#                     ''' We have to remove extra space before and after of our "What is time?" string,
#                      because if we keep space as it is, then interpreter will stop
#                     when it faces with space at the starting of the string and executes our else part.'''

#                     # This variable stores returned value of "get_answer_from_memory(ans)" function only if passed string argument is present in our database.
#                     value = get_answer_from_memory(ans)

#                     if value == "":
#                         return "Can't help with this one!"

#                     else:
#                         insert_question_and_answer(query, value)
#                         return "Thanks! I will remember for the next time."

#                 else:
#                     # This part will execute when there is no "it means" string present inside the answer.
#                     return " Sorry, sir! I can't help with this one!"

#     elif answer == "get time details":
#         return ("Time is " + str(get_time()))

#     elif answer == "check internet connection":
#         # This function calling is done here from Internet module to check connection.

#         if check_internet_connection():
#             # If internet is connected it will return...
#             return "internet is connected!"

#         else:
#             # If internet is not connected it will return...
#             return "internet is not connected."

#     elif answer == "tell date":
#         return "Date is : " + get_date()

#     # Here we are importing database functions for "ON" and "OFF" speech. which will be executed if corresponding values are matched.
#     elif answer == "on speak":
#         return turn_on_speech()

#     elif answer == "off speak":
#         return turn_off_speech()

#     # This block of code is for manipulating system apps.
#     elif answer == "open browser":
#         open_browser()
#         return "opening browser! Please wait."

#     elif answer == "open facebook":
#         open_facebook()
#         return "opening facebook! Please wait."

#     elif answer == "open google":
#         open_google()
#         return "opening google! Please wait."

#     elif answer == "open chatgpt":
#         open_chatgpt()
#         return "opening chatgpt! Please wait."

#     elif answer == "close browser":
#         close_browser()
#         return "closing browser! Please wait."

#     elif answer == "play music":
#         play_random_music()
#         return "Playing music, Please wait."

#     elif answer == "stop music":
#         pause_media_player()
#         return "Music has been stopped."

#     elif answer == "resume music":
#         resume_media_player()
#         return "Music has been resumed."

#     elif answer == "close media player":
#         close_media_player()
#         return "Media players been closed."

#     elif answer == "change volume":
#         change_volume()
#         return "Volume level has been changed."

#     elif answer == "open vscode":
#         open_vscode()
#         return "opening Vs Code! Please wait."

#     # This block of code is for personal information.
#     elif answer == "Manisha":
#         return "Manisha mam is your life, Sir and my boss as well!"

#     elif answer == "ABNGroup":
#         return "I am the creation of, Aftab and his team."

#     elif answer == "get my name":
#         return get_assistant_name()

#     elif answer == "get boss info":
#         return "You are my boss,Sir."

#     # This block of code will get executed and change the name of an assistant when the answer is == 'change name'.
#     elif answer == 'change name':
#         output("Okay! What do you want to call me? ")
#         temp = take_input()

#         if temp == Assistant_details.name:
#             return "Can't change. I think you are happy with my old name."
#         else:
#             update_name(temp)
#             Assistant_details.name = temp
#             return "Now you can call me :" + temp

#     # This block of code is for storing different ways in which user can ask preloadded questions, and that question is also stored with the same value and remembered by the assistent.
#     else:

#         # This block of code will try to search on the internet when a user says "yes" to our assistant for search.
#         output("Sorry Sir, I don't know this one should I search on internet?")
#         ans = take_input()
#         if "yes" in ans:
#             value = check_internet_connection()
#             if value == True:
#                 answer = check_on_wikipedia(query)
#                 if answer != "":
#                     return answer
#                 else:
#                     output(
#                         "Sorry sir, I can't found matched content on wikipedia, Should I google for you?")
#                     user_response = take_input()
#                     if "yes" in user_response:
#                         info = search_on_google(query)
#                         if info != "":
#                             return info
#                     else:
#                         # This function gets called if user don't want.
#                         store_question(query)
#                         return ("Sir if you have any other questions,feel free to ask me.")
#             else:
#                 return ("Sir,Please check your internet connection.")
#         else:
#             output("Can you please tell me, what it means?")
#             # Below code is used to store questions dynamically.
#             ans = take_input()

#             if "it means" in ans:
#                 # This line omits the "it means" string before displaying output by replacing it with an empty string.
#                 ans = ans.replace("it means", "")
#                 ans.strip()
#                 ''' We have to remove extra space before and after of our "What is time?" string,
#                  because if we keep space as it is, then interpreter will stop
#                 when it faces with space at the starting of the string and executes our else part.'''

#                 # This variable stores returned value of "get_answer_from_memory(ans)" function only if passed string argument is present in our database.
#                 value = get_answer_from_memory(ans)

#                 if value == "":
#                     return "Can't help with this one!"

#                 else:
#                     insert_question_and_answer(query, value)
#                     return "Thanks! I will remember for the next time."

#             else:
#                 store_question(query)
#                 # This part will execute when there is no "it means" string present inside the answer.
#                 return "Sir, if you have any other questions, Please let me know."

"""---------------------- THIS WAS MY INITIAL PROCESSING SCRIPT FOR PROCESSING --------------------------------------"""
