import webbrowser
import os
from Output_module import output
from Input_module import take_input
from Database import get_assistant_name

"""------------------------------------------------------------------------------------------------------------------"""


# This script simply opens up the default browser for a system. In my case, it is brave.


def open_browser():
    # Open the default browser to the specified URL.
    os.system(f"start brave.exe /f")
    return "Browser has been successfully opened."

# This script simply closes the default browser for a system. In my case, it is brave.


def close_browser():
    os.system(f"taskkill /f /im brave.exe > nul 2>&1")
    return "Browser has been successfully closed."


""""-----------------------------------------------------------------------------------------------------------------"""


# Script for opening different browser as if user wishes.
def open_chrome():
    try:
        os.system(f"start chrome.exe /f")
    except FileNotFoundError:
        return "Chrome is not installed on your system."


def close_chrome():
    try:
        os.system(f"taskkill /f /im chrome.exe nul 2>&1")
    except Exception as e:
        return f"Error closing Chrome: {e}"


def open_firefox():
    try:
        os.system(f"start firefox.exe /f")
    except FileNotFoundError:
        return "Firefox is not installed on your system."


def close_firefox():
    try:
        os.system("TASKKILL /F /IM firefox.exe >nul 2>&1")
        return "Firefox has been closed."
    except Exception as e:
        return f"An error occurred: {e}"


""""-----------------------------------------------------------------------------------------------------------------"""


def youtube_search():
    output("Sir, Please enter what would you like to watch on youtube.")
    subject = take_input()
    subject = subject.replace(get_assistant_name(), "")
    subject = subject.replace("youtube search", "")
    output(f"Sir you have entered following subject: {subject}.")
    # Here if we pass query by calling name of assistant then name of assistant will be replaced with empty string.
    url = "https://www.youtube.com/results?search_query=" + subject
    webbrowser.open(url)
    return "Playing the top result on YouTube"


""""-----------------------------------------------------------------------------------------------------------------"""


# This function uses os module's function for killing running default browser, but shows implementation details.so we will not use it.
# Def close_browser("taskkill /im brave.exe /f"):
#     os.system()
"""------------------------------------------------------------------------------------------------------------------"""

# WE CAN SEE IT LATTER
# import subprocess

# def close_vscode():
#     subprocess.Popen(["taskkill", "/im", "code.exe", "/f"])

# close_vscode()

""""-----------------------------------------------------------------------------------------------------------------"""
