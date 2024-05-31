import webbrowser
import subprocess
import winsound
import requests
from bs4 import BeautifulSoup
from Output_module import output
import ctypes
import random
from win32api import GetSystemMetrics
from Input_module import take_input
from Internet import check_internet_connection
import pyautogui
import os
from sympy import *
"""----------------------------------------- FEATURE NO : 01 (BASIC CALCULATION) -------------------------------------------------"""

# Here I have used sympy math library which can help to perform adnaced mathematical operations along with the basic calculations.


def calculator():
    output("Sir, I have started calculator mode.")
    output("Please enter your calculation below:")

    while True:
        # Get input from user
        query = input("\033[1m\033[32m>>> \033[0m")

        # Exit calculator mode if user says "stop"
        if query.lower() == "stop":
            break

        try:
            # Define symbols for mathematical variables
            x, y, z = symbols('x y z')

            # Parse the user's input as a mathematical expression
            expression = parse_expr(query, evaluate=False)

            # Evaluate the expression
            # Substitute values if needed
            result = expression.evalf(subs={x: 1, y: 2, z: 3})

            # Display the result
            output(f"The result of ({query}) is: {result}")
        except Exception as e:
            # Display an error message if the input is invalid
            output("Sorry Sir, I could not perform the calculation.")

        output("Please enter your calculation below (or say 'stop' to exit):")

    return "Exiting calculator mode."


'''--------------------------- FEATURE NO : 02 (DESKTOP WALLPAPER) -----------------------------'''


def set_wallpaper():
    # Get the size of the display
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)

    # Image paths for different resolutions
    image_paths_4k = [
        "C:/Users/Aftab/Pictures/Saved Pictures/pexels-pixabay-36717.jpg",
        "C:/Users/Aftab/Pictures/Saved Pictures/pexels-george-desipris-1028637.jpg"
        # Add more paths for 4K resolution
    ]

    image_paths_1080p = [
        "C:/Users/Aftab/Pictures/Saved Pictures/pexels-eberhard-grossgasteiger-640781.jpg",
        "C:/Users/Aftab/Pictures/Saved Pictures/pexels-eberhard-grossgasteiger-443446.jpg",
        # Add more paths for 1080p resolution
    ]

    # Choose an image path based on the size of the display
    if width >= 3840 and height >= 2160:
        image_paths = image_paths_4k
    elif width >= 1920 and height >= 1080:
        image_paths = image_paths_1080p
    else:
        image_paths = image_paths_1080p  # Use 1080p images as fallback

    # Select a random image path from the chosen list
    selected_image_path = random.choice(image_paths)

    # Set the selected image as the wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, selected_image_path, 3)


'''---------------------------------- FEATURE NO: 03 (WEATHER) --------------------------------------------'''


def weather_forecast():
    if check_internet_connection():
        output(
            "Sure Sir, I'd be happy to help you find the temperature for a specific city.\n Which city would you like to know the temperature for?")
        city = take_input()
        if city == "":
            search = "Temperature in " + "kolhapur"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            return f"Current {search} is: {temp}."
        else:
            search = "Temperature in " + city
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            return f"Current {search} is: {temp}."
    else:
        return "Sir, Please kindly check your internet connection."


'''-------------------------------------- FEATURE NO: O4 (VOICE TYPING) --------------------------------------'''


def open_vscode():
    output("Opening VsCode, Please wait!")
    os.system('code')


def open_notepad():
    try:
        subprocess.Popen(['notepad.exe'])
        return "Notepad opened successfully."
    except FileNotFoundError:
        return "Notepad is not found on your system."


def start_voice_typing():
    # Play a sound
    winsound.PlaySound("path_to_sound_file.wav", winsound.SND_FILENAME)
    # Press Win + H to start voice recognition
    pyautogui.hotkey('win', 'h')
    return "Sir, I have started voice typing function."


"""-------------------------------------------------------------------------------------------------------------"""



def play_online_music():
    # Ask the user for the song to play
    song = input("What song would you like to play? ")

    # Construct the YouTube URL for the song
    youtube_url = f"https://www.youtube.com/results?search_query={song}"

    # Open the YouTube URL in a web browser
    webbrowser.open(youtube_url)

    # Print a message indicating that the song is playing
    return f"Now streaming: {song} on YouTube."


""" SPOTIFY FUNCTION """
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# from Input_module import take_input
# from Output_module import output

# def play_music():
#     # Ask the user for the song to play
#     output("What song would you like to play?")
#     song = take_input()

#     # Initialize the Spotify client
#     sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-read-playback-state"))

#     # Search for the song on Spotify
#     results = sp.search(q=song, type="track", limit=1)

#     if results["tracks"]["items"]:
#         track_uri = results["tracks"]["items"][0]["uri"]

#         # Play the song on Spotify
#         sp.start_playback(uris=[track_uri])
#         return f"Now playing: {song} on Spotify."
#     else:
#         return f"Sorry, could not find the song: {song} on Spotify."


# if __name__ == "__main__":
#     # calculator()

# """------------------------------------------------------------------------------------------------------------------------------"""
# import subprocess
# import winsound
# import requests
# from bs4 import BeautifulSoup
# from Output_module import output
# import ctypes
# import random
# from win32api import GetSystemMetrics
# from Input_module import take_input
# from Internet import check_internet_connection
# import pyautogui
# import os
# # import pywhatkit

# """----------------------------------------- FEATURE NO : 01 (BASIC CALCULATION) -------------------------------------------------"""


# def calculator():
#     output("Sir, I have started calculator mode.")
#     output("Please enter your calculation below:")

#     while True:
#         # Get input from user
#         query = input("\033[1m\033[32m>>> \033[0m")

#         # Exit calculator mode if user says "stop"
#         if query.lower() == "stop":
#             break

#         try:
#             # Replace trigonometric functions with their equivalent expressions in radians
#             query = query.replace("sin", "math.sin")
#             query = query.replace("cos", "math.cos")
#             query = query.replace("tan", "math.tan")
#             query = query.replace("asin", "math.asin")
#             query = query.replace("acos", "math.acos")
#             query = query.replace("atan", "math.atan")
#             query = query.replace("sqrt", "math.sqrt")
#             query = query.replace("log", "math.log10")
#             query = query.replace("ln", "math.log")
#             query = query.replace("^", "**")

#             # Evaluate the user's input
#             result = eval(query)
#             formatted_result = "{:.2f}".format(result)
#             # Display the result
#             print(
#                 "\033[34mTHE GENERATED RESULTS MIGHT BE WRONG FOR SOME SCENARIO, BECAUSE IT IS STILL IN DEVELOPING MODE.\033[0m")
#             output(f"The result of ({query}) is: {formatted_result}")
#         except Exception as e:
#             # Display an error message if the input is invalid
#             output(
#                 f"Sorry Sir, I could not perform the calculation.")

#         output("Please enter your calculation below (or say 'stop' to exit):")

#     return "Exiting calculator mode."


# '''--------------------------- FEATURE NO : 02 (DESKTOP WALLPAPER) -----------------------------'''

# # List of image file paths
# image_paths = ([

#     "C:/Users/Aftab/Pictures/Saved Pictures/pexels-eberhard-grossgasteiger-443446.jpg",
#     "C:/Users/Aftab/Pictures/Saved Pictures/pexels-eberhard-grossgasteiger-640781.jpg",
#     "C:/Users/Aftab/Pictures/Saved Pictures/pexels-pixabay-36717.jpg",
#     "C:/Users/Aftab/Pictures/Saved Pictures/pexels-george-desipris-1028637.jpg",
#     "C:/Users/Aftab/Pictures/Saved Pictures/uwp3548627.jpeg",
#     "C:/Users/Aftab/Pictures/Saved Pictures/pexels-pixabay-36717.jpg",
#     "C:/Users/Aftab/Pictures/Saved Pictures/IMG_20230413_214651.jpg",
#     "C:/Users/Aftab/Pictures/Saved Pictures/IMG_20230420_180200.jpg",
#     "C:/Users/Aftab/Pictures/Saved Pictures/licensed-image.jpeg"

# ])


# def set_wallpaper():
#     # Get the size of the display
#     width = GetSystemMetrics(0)
#     height = GetSystemMetrics(1)

#     # Choose an image path based on the size of the display
#     if width >= 3840 and height >= 2160:
#         selected_image_path = "C:/path/to/4K/wallpaper.jpg"
#     elif width >= 1920 and height >= 1080:
#         selected_image_path = "C:/path/to/1080p/wallpaper.jpg"
#     else:
#         selected_image_path = random.choice(image_paths)

#     # Set the selected image as the wallpaper
#     ctypes.windll.user32.SystemParametersInfoW(20, 0, selected_image_path, 3)


# '''---------------------------------- FEATURE NO: 03 (WEATHER) --------------------------------------------'''


# def weather_forecast():
#     if check_internet_connection():
#         output(
#             "Sure Sir, I'd be happy to help you find the temperature for a specific city.\n Which city would you like to know the temperature for?")
#         city = take_input()
#         if city == "":
#             search = "Temperature in " + "kolhapur"
#             url = f"https://www.google.com/search?q={search}"
#             r = requests.get(url)
#             data = BeautifulSoup(r.text, "html.parser")
#             temp = data.find("div", class_="BNeawe").text
#             return f"Current {search} is: {temp}."
#         else:
#             search = "Temperature in " + city
#             url = f"https://www.google.com/search?q={search}"
#             r = requests.get(url)
#             data = BeautifulSoup(r.text, "html.parser")
#             temp = data.find("div", class_="BNeawe").text
#             return f"Current {search} is: {temp}."
#     else:
#         return "Sir, Please kindly check your internet connection."


# '''-------------------------------------- FEATURE NO: O4 (VOICE TYPING) --------------------------------------'''


# # This function can launch vs code.


# def open_vscode():
#     output("Opening VsCode, Please wait!")
#     os.system('code')


# def open_notepad():
#     try:
#         subprocess.Popen(['notepad.exe'])
#         return "Notepad opened successfully."
#     except FileNotFoundError:
#         return "Notepad is not found on your system."


# # This function is used to for voice typing in any code editor.


# def start_voice_typing():
#     # Play a sound
#     winsound.PlaySound("path_to_sound_file.wav", winsound.SND_FILENAME)
#     # Press Win + H to start voice recognition
#     pyautogui.hotkey('win', 'h')
#     return "Sir, I have started voice typing function."


# # def create_new_file_in_vscode():
# #     # Create a new file
# #     pyautogui.hotkey('ctrl', 'n')


# """-------------------------------------------------------------------------------------------------------------"""


# # def play_music():
# #     # ask the user for the song to play
# #     output("What song would you like to play?")
# #     song = take_input()

# #     # use the pywhatkit.playonyt() function to play the song on YouTube
# #     pywhatkit.playonyt(song)

# #     # print a message indicating that the song is playing
# #     return f"Now playing: {song} on YouTube."
