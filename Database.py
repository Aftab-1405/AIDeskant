import pyttsx3
import sqlite3
from Internet import check_internet_connection
import random


def create_connection():
    connection = sqlite3.connect("memory.db")
    return connection


def get_name_from_database():
    con = create_connection()
    cur = con.cursor()
    query = "SELECT value FROM memory WHERE name = 'assistant_name'"
    cur.execute(query)
    return cur.fetchone()[0]


def get_assistant_name():
    assistant_name = get_name_from_database()
    return f"Hello sir, My name is {assistant_name}. How can I help you?"


def update_name(new_name):
    con = create_connection()
    cur = con.cursor()
    query = "UPDATE memory SET value = ? WHERE name = 'assistant_name'"
    cur.execute(query, (new_name,))
    con.commit()


def update_voice(voice_id):
    con = create_connection()
    cur = con.cursor()
    query = "UPDATE memory SET value = ? WHERE name = 'assistant_voice'"
    cur.execute(query, (voice_id,))
    con.commit()


def set_default_voice():
    con = create_connection()
    cur = con.cursor()
    query = "SELECT value FROM memory WHERE name = 'assistant_voice'"
    cur.execute(query)
    result = cur.fetchone()
    if result is not None:
        tts = pyttsx3.init()
        tts.setProperty('voice', result[0])
        return tts
    else:
        return "Sir, I don't have that voice."


def turn_on_speech():
    if check_internet_connection():
        con = create_connection()
        cur = con.cursor()
        query = "UPDATE memory SET value = 'on' WHERE name = 'speech'"
        cur.execute(query)
        con.commit()
        return "Okay sir, I will speak now."
    else:
        return "Sir, Please turn on the internet first."


def turn_off_speech():
    con = create_connection()
    cur = con.cursor()
    query = "UPDATE memory SET value = 'off' WHERE name = 'speech'"
    cur.execute(query)
    con.commit()
    return "Okay, I won't speak."


def speak_is_on():
    con = create_connection()
    cur = con.cursor()
    query = "SELECT value FROM memory WHERE name = 'speech'"
    cur.execute(query)
    ans = str(cur.fetchone()[0])
    return ans == "on"


def get_question_and_answers():
    con = create_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM QuestionsAndAnswers")
    return cur.fetchall()


def insert_question_and_answer(question, answer):
    con = create_connection()
    cur = con.cursor()
    query = "INSERT INTO QuestionsAndAnswers VALUES (?, ?)"
    cur.execute(query, (question, answer))
    con.commit()


def get_answer_from_memory(question):
    rows = get_question_and_answers()
    options = []
    for row in rows:
        if row[0].lower() in question.lower():
            options.append(row[1])

    if options:
        return random.choice(options)
    else:
        return ""


def updates_last_seen(last_seen_date):
    con = create_connection()
    cur = con.cursor()
    query = "UPDATE memory SET value = ? WHERE name = 'last_seen_date'"
    cur.execute(query, (str(last_seen_date),))
    con.commit()


def get_last_seen():
    con = create_connection()
    cur = con.cursor()
    query = "SELECT value FROM memory WHERE name = 'last_seen_date'"
    cur.execute(query)
    return str(cur.fetchone()[0])


def get_user_name_from_database():
    con = create_connection()
    cur = con.cursor()
    query = "SELECT value FROM memory WHERE name = 'user_name'"
    cur.execute(query)
    user_name = cur.fetchone()[0]
    return f"Hello sir, Your name is {user_name}. Please tell me, how can I help you?"


def update_user_name():
    con = create_connection()
    cur = con.cursor()
    query = "SELECT value FROM memory WHERE name = 'user_name'"
    cur.execute(query)
    result = cur.fetchone()
    current_name = result[0]
    new_name = input(
        "\033[1m\033[34m" + "ENTER YOUR NEW NAME OR PRESS ENTER TO KEEP THE CURRENT NAME: " + "\033[0m").strip().capitalize()
    if new_name and new_name != current_name:
        query = "UPDATE memory SET value = ? WHERE name = 'user_name'"
        cur.execute(query, (new_name,))
        con.commit()
        return "Your name has been updated to " + new_name + ", Sir."
    else:
        return "Your name is still " + current_name + ", Sir."


"""--------------------------------------------------------------------------------------------------------------------------------------------"""
# import pyttsx3
# import sqlite3  # This instruction importing sqlite3 built-in package.
# from Internet import check_internet_connection
# import random

# """"-------------------------------------- DATABASE CONNECTIVITY FUNCTION -------------------------------------------"""


# # This function is basically trying to connect without a database called as "memory.db".


# def create_connection():
#     connection = sqlite3.connect("memory.db")
#     return connection


# # create_connection() ---------> use to check database connectivity by uncommenting it.


# """------------------------------------------- ASSISTANT NAME FUNCTION ----------------------------------------------"""


# # get_name() function is used to store new name given by the user to change the name of assistant.


# def get_name_from_database():
#     con = create_connection()
#     cur = con.cursor()
#     query = "select value from memory where name = 'assistant_name'"
#     cur.execute(query)
#     return cur.fetchall()[0][0]


# # Here I am using get_name() function connect to a database and retrieve the name of assistant.
# def get_assistant_name():
#     assistant_name = get_name_from_database()
#     return f"Hello sir, My name is {assistant_name}. How can I help you?"


# def update_name(new_name):
#     con = create_connection()
#     cur = con.cursor()
#     query = "update memory set value = '" + \
#             new_name + "' where name = 'assistant_name'"
#     cur.execute(query)
#     con.commit()


# """-------------------------------------------- VOICE FUNCTION ------------------------------------------------------"""


# # This function will store voice id into a database if user changes voice of an assistant.


# def update_voice(voice_id):
#     con = create_connection()
#     cur = con.cursor()
#     query = "update memory set value = '" + \
#             voice_id + "' where name = 'assistant_voice'"
#     cur.execute(query)
#     con.commit()


# # Set default voice to the one stored in the database


# def set_default_voice():
#     con = create_connection()
#     cur = con.cursor()
#     query = "select value from memory where name = 'assistant_voice'"
#     cur.execute(query)
#     result = cur.fetchone()
#     if result is not None:
#         tts = pyttsx3.init()
#         tts.setProperty('voice', result[0])
#         return tts
#     else:
#         return "Sir, I don't have that voice."


# """"--------------------------------------- SPEECH FUNCTIONS FOR ON/OFF SPEECH --------------------------------------"""


# def turn_on_speech():
#     if check_internet_connection:
#         con = create_connection()
#         cur = con.cursor()
#         query = "update memory set value = 'on' where name = 'speech'"
#         cur.execute(query)
#         con.commit()
#         # This sms will be displayed if speech is turned on by the user only if the internet is connected.
#         return "Okay sir, I will speak now."
#     else:
#         return "Sir,Please turn on internet first..."


# def turn_off_speech():
#     con = create_connection()
#     cur = con.cursor()
#     query = "update memory set value = 'off' where name = 'speech'"
#     cur.execute(query)
#     con.commit()
#     return "Okay, I won't speak."


# def speak_is_on():
#     con = create_connection()
#     cur = con.cursor()
#     query = "select value from memory where name = 'speech'"
#     cur.execute(query)
#     ans = str(cur.fetchall()[0][0])

#     if ans == "on":
#         return True
#     else:
#         return False


# """"------------------------------------- DATABASE INSERT/UPDATE/SELECT FUNCTIONS -----------------------------------"""


# def get_question_and_answers():
#     con = create_connection()
#     cur = con.cursor()  # Creating a cursor.(Cursor is useful to execute queries for database.)
#     # Passing queries to the sqlite database with the help of cursor named as 'cur'.
#     cur.execute("SELECT * FROM QuestionsAndAnswers")
#     # The "fetchall()" function fetches all the data at a time using cur.
#     return cur.fetchall()


# # This function simply stores new instances of already stored questions which will be appeared in a database with the same answer.
# def insert_question_and_answer(question, answer):
#     con = create_connection()
#     cur = con.cursor()  # Creating a cursor.(Cursor is useful to execute queries for database.)

#     # Passing queries to the sqlite database with the help of cursor named as 'cur'.
#     cur.execute("SELECT * FROM QuestionsAndAnswers")
#     # The "fetchall()" function fetches all the data at a time using cur.
#     # Database INSERT query.
#     query = "INSERT INTO QuestionsAndAnswers values('" + \
#             question + "','" + answer + "')"
#     cur.execute(query)
#     con.commit()


# def get_answer_from_memory(question):
#     # Variable "rows" will store all the data returned by "get_question_and_answers()" function in it.
#     rows = get_question_and_answers()
#     # Empty string is created to return empty string when the associated answer of question is not present in a database of rake.
#     answer = ""
#     options = []
#     for row in rows:
#         if row[0].lower() in question.lower():
#             options.append(row[1])

#     if options:
#         answer = random.choice(options)

#     return answer


# """THIS FUNCTION WAS ABLE TO SELECT ONLY ONE INSTANT OR FIXED ANSWER OF QUESTION AND NOT ABLE TO SELECT RANDOM ANSWERS
# SO I HAVE CREATED ABOVE FUNCTION"""

# # def get_answer_from_memory(question):
# #     # Variable "rows" will store all the data returned by "get_question_and_answers()" function in it.
# #     rows = get_question_and_answers()
# #     # Empty string is created to return empty string when the associated answer of question is not present in database of rake.
# #     answer = ""
# #     for row in rows:
# #         if row[0].lower() in question.lower():
# #             answer = row[1]
# #             break

# #     return answer

# #     print(row[0]) # This will print only the first part of returned tuple by the "get_question_and_answers()".


# """"---------------------------------------- LAST SEEN UPDATE FUNCTIONS USING TIMEDATE ------------------------------"""


# # This function update date into a database whenever our assistant activated.


# def updates_last_seen(last_seen_date):
#     con = create_connection()
#     cur = con.cursor()
#     query = "update memory set value = '" + \
#             str(last_seen_date) + "' where name = 'last_seen_date'"
#     cur.execute(query)
#     con.commit()


# # This function will fetch the last seen date from a database whenever our assistant is activated.


# def get_last_seen():
#     con = create_connection()
#     cur = con.cursor()
#     query = "select value from memory where name = 'last_seen_date'"
#     cur.execute(query)
#     return str(cur.fetchall()[0][0])


# # updates_last_seen("65676366") # It is used to reset stored time in a database with an empty string.


# """------------------------------------------ USER DETAILS FUNCTION -------------------------------------------------"""


# def get_user_name_from_database():
#     con = create_connection()
#     cur = con.cursor()
#     query = "select value from memory where name = 'user_name'"
#     cur.execute(query)
#     user_name = cur.fetchall()[0][0]
#     return f"Hello sir, Your name is {user_name}. Please tell me, How can i help you?"


# def update_user_name():
#     con = create_connection()
#     cur = con.cursor()
#     query = "SELECT value FROM memory WHERE name = 'user_name'"
#     cur.execute(query)
#     result = cur.fetchone()
#     current_name = result[0]
#     new_name = input(
#         "\033[1m\033[34m" + "ENTER YOUR NEW NAME OR PRESS ENTER TO KEEP THE CURRENT NAME: " + "\033[0m").strip().capitalize()
#     if new_name and new_name != current_name:
#         query = "UPDATE memory SET value = '{}' WHERE name = 'user_name'".format(
#             new_name)
#         cur.execute(query)
#         con.commit()
#         return "Your name has been updated to " + new_name + ", Sir."
#     else:
#         return "Your name is still " + current_name + ", Sir."


# """------------------------------------------------------------------------------------------------------------------"""
