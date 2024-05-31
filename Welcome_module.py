"""------------------------------------------------------------------------------------------------------------------"""
from Output_module import output
from Database import updates_last_seen, get_last_seen
from Time_module import get_hours, get_date
import random


def greet():
    previous_date = get_last_seen()
    today_date = get_date()
    updates_last_seen(today_date)

    if previous_date == today_date:
        welcome_msgs = [
            "Good to see you again, {name}!",
            "Hello, {name}! It's great to have you back.",
            "Hi {name}! Welcome back.",
            "Sir, it's good to have you back with me.",
            # Add more personalized welcome messages
        ]
        welcome_msg = random.choice(welcome_msgs).format(
            name="Sir")  # Replace "Sir" with user's name if available

        output(welcome_msg)
    else:
        hour = int(get_hours())
        greeting = ""

        if 4 <= hour < 12:
            greeting = "Good morning, Sir. Have you had your breakfast?"
        elif 12 <= hour < 18:
            greeting = "Good afternoon, Sir."
        elif 18 <= hour < 24:
            greeting = "Good evening, Sir."
        else:
            greeting = "Sir, it's too late. You should take some rest."

        output(greeting)


"""------------------------------------------------------------------------------------------------------------------"""
# def greet():
#     previous_date = get_last_seen()
#     today_date = get_date()
#     updates_last_seen(today_date)

#     if previous_date == today_date:
#         output("Welcome back, Sir.")
#     else:
#         hour = int(get_hours())

#         if hour >= 0 and hour <= 12:
#             url = "https://quotes.rest/qod?category=inspire"
#             response = requests.get(url)
#             json_data = json.loads(response.text)
#             quote = json_data['contents']['quotes'][0]['quote']
#             author = json_data['contents']['quotes'][0]['author']
#             output(
#                 f"\nGood morning, Sir! Here's a quote for you:\n\n{quote}\n\n- {author}\n")
#         elif hour > 12 and hour <= 18:
#             output("Good afternoon, Sir.")
#         elif hour > 18 and hour <= 24:
#             output("Good evening, Sir.")
#         else:
#             output("Sir, it's too late. You should take some rest.")

'''----- THIS IS A SECOND FUNCTION FOR GREETING WITH MORNING QUOTE BUT DIDN'T HAVE MULTIPLE INSTANCES OF GREET ------'''

# # Here we are importing get_hours() function which simply returns hours.
# from Time_module import get_hours, get_date
# from Output_module import output
# from Database import updates_last_seen, get_last_seen
# from datetime import date
# # The greet() function
# # basically greet to user according to the time and also says "Welcome Back" if the assistant is started the same day.
# # 1. Fetch the previous date from a database.
# # 2. Fetch today's date from a database.


# def greet():
#     # Here returned date by 'get_last_seen()' function of 'Database_module' is assigned to 'previous_date' variable.
#     previous_date = get_last_seen()

#     # This will store the current date.
#     today_date = get_date()
#     updates_last_seen(today_date)

#     if previous_date == today_date:
#         output("Welcome back, Sir")
#     else:
#         # Typecasting returned hour by function in an integer
#         hour = int(get_hours())

#         if hour >= 6 and hour <= 12:
#             output("Good Morning, Sir!")
#         elif hour > 12 and hour <= 15:
#             output("Good After Noon, Sir!")
#         elif hour > 15 and hour <= 24:
#             output("Good Evening, Sir")
#         else:
#             output("Sir,It's too late. You should take sleep.")

'''---------------------------- THIS IS A BASIC FUNCTION FIRSTLY CREATED BY ME --------------------------------------'''
