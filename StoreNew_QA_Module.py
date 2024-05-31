from Output_module import output
from Internet import *
from Input_module import take_input
import sqlite3
import re


# Store the new question during looking in a database for answer.
def store_question(question, conn=sqlite3.connect("memory.db")):
    c = conn.cursor()

    output("Should I look up the answer to that question in my database? (yes or no)")
    lookup = take_input()

    if "stop" in lookup.strip().lower():
        # stop function execution if user says stop during the current running flow of function.
        return

    if lookup.strip().lower() == "yes":
        c.execute("SELECT * FROM QuestionsAndAnswers WHERE question=?", (question,))
        result = c.fetchone()

        if result is not None:
            answer = result[1]
            output(answer)
        else:
            output("Sir, I can't found answer related to this question in database as well. What's the answer to that question? If you want's to submit answer to me, Please kindly enter 'Yes'.")
            response = take_input()

            if "stop" in response.strip().lower():
                return  # stop function execution

            if response.strip().lower() == "yes":
                output(
                    "Sir, I am waiting for your answer. Please,Submit your answer below:")
                answer = take_input()

                if "stop" in answer.strip().lower():
                    # stop function execution
                    return

                if answer:
                    answer = re.sub(r'\bmy\b', 'your', answer)
                    answer = re.sub(r'\bmine\b', 'yours', answer)
                    answer = re.sub(r'\bi\b', 'you', answer)
                    answer = re.sub(r'\bam\b', 'are', answer)

                    output(
                        f"Thanks for the answer sir , Can I store the following answer? Please let me know. The answer is: '{answer}'")
                    store = take_input()

                    if "stop" in store.strip().lower():
                        # stop function execution
                        return

                    if store.strip().lower() == "yes":
                        connection = check_internet_connection()
                        if connection:
                            c.execute(
                                "INSERT INTO QuestionsAndAnswers (question, answer) VALUES (?, ?)", (question, answer))
                            conn.commit()
                            return "Okay, Thank you sir, I've stored that information."
                        else:
                            return "Sir, I am not getting response from database."
                    else:
                        return "Okay, I won't store that information."
            else:
                return "Sorry, I didn't catch the answer. Can you try again?"
    else:
        return "Okay, let me know if you have the answer."


'''------------------------------------------------------------------------------------------------------------------'''

# This function allows user to call directly through the terminal and store new questions and their corresponding answers in a database.


def direct_store_new_question():
    if check_internet_connection():
        conn = sqlite3.connect("memory.db")
        c = conn.cursor()
        # asking for new questions.
        output("What is the question you would like to store? (If you dont want to store any question, Please enter 'stop' to quit)")

        while True:
            output("Enter your question below.")
            question = take_input()

            if question.lower() == "stop":
                return "Okay, I'll stop now."

            c.execute(
                "SELECT * FROM QuestionsAndAnswers WHERE question=?", (question,))
            result = c.fetchone()

            if result is not None:
                output(
                    f"I already have an answer for that question. The answer is: {result[1]}. Would you like to update it? (yes or no)")
                update = take_input()

                if update.strip().lower() == "yes":
                    output("What is the updated answer to that question?")
                    answer = take_input()

                    if answer:

                        answer = re.sub(r'\bmy\b', 'your', answer)
                        answer = re.sub(r'\bmine\b', 'yours', answer)
                        answer = re.sub(r'\bi\b', 'you', answer)
                        answer = re.sub(r'\bam\b', 'are', answer)

                    output(
                        f"Sir, You have submitted the following answer: {answer}")
                    c.execute(
                        "UPDATE QuestionsAndAnswers SET answer=? WHERE question=?", (answer, question))
                    conn.commit()
                    output("Okay, I've updated that information.")

                else:
                    output("Okay, I won't update that information.")

            else:
                output("What is the answer to that question?")
                answer = take_input()

                if answer:
                    answer = re.sub(r'\bmy\b', 'your', answer)
                    answer = re.sub(r'\bmine\b', 'yours', answer)
                    answer = re.sub(r'\bi\b', 'you', answer)
                    answer = re.sub(r'\bam\b', 'are', answer)
                c.execute(
                    "INSERT INTO QuestionsAndAnswers (question, answer) VALUES (?, ?)", (question, answer))
                conn.commit()
                output(
                    f"Sir, You have submitted the following answer: {answer}. I am going to store it.")
                output("Okay, I've stored that information.")
    else:
        return "Sir, I am having connection error. Please check internet."


"""------------------------------------------------------------------------------------------------------------------"""

# def retrieve_answer(question):
#     # connect to the database
#     conn = sqlite3.connect("memory.db")
#     c = conn.cursor()

#     # check if the question is in the database
#     c.execute("SELECT * FROM QuestionsAndAnswers WHERE question=?", (question,))
#     result = c.fetchone()

#     if result is not None:
#         # if the question is in the database, fetch the answer and return it
#         answer = result[1]
#         output(f"The answer to '{question}' is: {answer}")
#     else:
#         # if the question is not in the database, return None
#         output("I'm sorry, I don't have an answer to that question.")

"""------------------------------------------------------------------------------------------------------------------"""


''' THIS FUNCTION IS ABLE TO ADD NEW QUESTIONS ENTERED BY THE USER IF IT IS NOT PRESENT IN DATABASE,
AND UNABLE TO IDENTIFY ALREADY STORED QUESTIONS IN DATABASE AND ALSO NOT RETURN THEIR CORRESPONDING ANSWER,
THAT'S WHY I HAVE CREATED UPDATED FUNCTION ABOVE. '''

# def store_question(question):
#     # connect to the database
#     conn = sqlite3.connect("memory.db")
#     c = conn.cursor()

#     # check if the question is already in the database
#     c.execute("SELECT * FROM QuestionsAndAnswers WHERE question=?", (question,))
#     result = c.fetchone()

#     if result is not None:
#         # if the question is already in the database, let the user know
#         output("That question is already in the database.")
#     else:
#         # if the question is not in the database, ask the user for the answer
#         output("Okay, what's the answer to that question?")
#         answer = input()

#         # check if the user provided an answer
#         if answer:
#             # ask the user if they want to store the new question and answer
#             output(f"Thanks for the answer. Can I store '{question}' means '{answer}'? (yes or no)")
#             store = input()

#             if store.lower() == "yes":
#                 # replace any instances of "my" in the answer with "your"
#                 answer = answer.replace("my", "your")
#                 answer = answer.replace("i am", "you are")
#                 answer = answer.replace("i", "you")
#                 answer = answer.replace("you", "i am")
#                 # store the new question and answer in the database
#                 c.execute("INSERT INTO QuestionsAndAnswers (question, answer) VALUES (?, ?)", (question, answer))
#                 conn.commit()
#                 output("Okay, I've stored that information.")
#             else:
#                 output("Okay, I won't store that information.")
#         else:
#             output("Sorry, I didn't catch the answer. Can you try again?")

""""-----------------------------------------------------------------------------------------------------------------"""
