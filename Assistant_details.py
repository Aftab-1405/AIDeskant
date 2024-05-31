import platform
from Database import get_name_from_database

"""------------------------------------------------------------------------------------------------------------------"""


def is_window():
    return 'Windows' in platform.system()


is_window()

name = get_name_from_database()


def about_assistant():
    return f"I am {name}. An AI assistant created by ABN Group. My purpose is to assist and converse with you on a variety of topics. I have a limited knowledge base, but I'm constantly learning to improve. How can I assist you today?"
