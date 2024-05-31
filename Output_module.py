"""---------------------------- THIS FUNCTION WILL NOT SPEAK AND PRINT AT SAME TIME ---------------------------------"""
from Assistant_details import name
import sys
import time
import textwrap
import shutil
from Speak_module import speak


def get_terminal_width():
    try:
        # Get the terminal width using shutil.get_terminal_size()
        terminal_size = shutil.get_terminal_size(
            (80, 20))  # Default size if unable to determine
        return terminal_size.columns
    except Exception:
        pass

    # If unable to determine terminal size, fall back to a default width
    return 80  # Default terminal width


# def output(o):
#     speak(o)
#     sys.stdout.write("\033[1m\033[31m" + name.upper() + ":\033[0m ")

#     # Wrap the output text based on the terminal width
#     terminal_width = get_terminal_width()
#     # Subtracting 11 to account for formatting characters and name length
#     wrapped_text = textwrap.wrap(str(o), width=terminal_width - 11)

#     # Print the wrapped text line by line
#     for i, line in enumerate(wrapped_text):
#         for letter in line:
#             sys.stdout.write("\033[31m" + letter.capitalize() + "\033[0m")
#             sys.stdout.flush()
#             time.sleep(0.02)
#         if i != len(wrapped_text) - 1:
#             # Add an extra line break between paragraphs
#             sys.stdout.write("\n")
#     sys.stdout.write("\n")  # Add a final line break


"""-------------------- THIS FUNCTION REMAINS SOME MODIFICATION -------------------------"""


def output(o):
    speak(o)
    sys.stdout.write("\033[1m\033[31m" + name.upper() + ":\033[0m ")

    # Convert the output text to string representation
    output_text = str(o)

    # Type the text letter by letter with a delay
    for letter in output_text:
        sys.stdout.write(letter.capitalize())
        sys.stdout.flush()
        time.sleep(0.001)  # we can change delay time of tyoing effect.

    sys.stdout.write("\n")  # Add a final line break

    # Flush the stdout buffer
    sys.stdout.flush()


"""------------------------------------------------------------------------------------------------------------------"""

# from Assistant_details import name
# from Speak_module import speak
# from Database import speak_is_on
# import pyttsx3

# def output(o):
#     if speak_is_on():
#         tts = pyttsx3.init()
#         tts.setProperty("rate", 160)
#         tts.say(o)
#         tts.runAndWait()

#     # Use ANSI escape codes to color the output
#     print("\033[1m" + name.upper() + ":\033[0m " + "\033[31m" + str(o).upper() + "\033[0m")
#     print()

'''---------------------------------------------------------------------------------------------------------'''

# from Assistant_details import name
# from Speak_module import speak
# from Database import speak_is_on


# def output(o):
#     if speak_is_on():
#         speak(o)

#     # Use ANSI escape codes to color the output
#     print("\033[1m" + name + ":\033[0m " + "\033[31m" + str(o) + "\033[0m")

#     print()

'''------------------------------------- IT DOESN'T HAVE TYPING EFFECT ---------------------------------------'''

# from Assistant_details import name
# from Speak_module import speak
# from Database import speak_is_on


# def output(o):
#     if speak_is_on():
#         speak(o)

#     # Use ANSI escape codes to color the output
#     print("\033[1m" + name.upper() + ":\033[0m " + "\033[31m" + str(o).upper() + "\033[0m")

#     print()

'''---------------------------- BELLOW FUNCTION WORKS PROPERLY BUT DON'T HAVE ANY COLOURS -----------------------'''

# import Assistant_details
# from Speak_module import speak
# from Database import speak_is_on


# def output(o):  # This is a Command line output function that displays output.

#     # This print function print name of assistent along with the passed query in process() function of Process_module.
#     if speak_is_on():
#         speak(o)

#     print(Assistant_details.name + " : " + str(o))
#     print()

'''--------------------------------------------------------------------------------------------------------'''

# from Assistant_details import name
# from Speak_module import speak
# from Database import speak_is_on


# def output(o):
#     if speak_is_on():
#         speak(o)

#     # Use ANSI escape codes to color the output
#     print("\033[1m" + name + ":\033[0m " + "\033[31m" + str(o) + "\033[0m")

#     # Add a separator line to make the output more visually appealing
#     print("\033[1m" + "-" * 70 + "\033[0m")

'''--------------------------------------------------------------------------------------------------------'''
