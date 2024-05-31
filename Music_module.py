# This is an optimized version of code.
from ctypes import POINTER, cast
import os
import random
import Assistant_details as ad
import win32api
import win32con
import subprocess
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from Output_module import output


def play_random_music():
    if ad.is_window():
        music_files = [f for f in os.listdir(
            "C:/Users/Aftab/Music/Music/") if f.endswith('.mp3')]
        if music_files:
            file_path = os.path.join(
                "C:/Users/Aftab/Music/Music/", random.choice(music_files))
            try:
                # Launch Windows Media Player in a separate process
                subprocess.Popen(
                    ['C:/Program Files (x86)/Windows Media Player/wmplayer.exe', file_path])

                # Wait for a few seconds before returning control to the calling code
                time.sleep(0)

                return "Playing music."
            except Exception as e:
                print("Error playing music:", e)
                return "Error playing music."
        else:
            return "No music files found in directory: C:/Users/Aftab/Music/Music/."


def close_media_player():
    process_name = 'wmplayer.exe'

    try:
        # Use the taskkill command to kill any running instances of the process
        subprocess.run(
            ['taskkill', '/im', process_name, '/f', '/t'], check=True)
        return "Media player closed successfully."
    except subprocess.CalledProcessError as e:
        return f"Error occurred while closing media player: {e}"


def pause_media_player():
    # Pause playback
    win32api.keybd_event(win32con.VK_MEDIA_PLAY_PAUSE, 0,
                         win32con.KEYEVENTF_EXTENDEDKEY, 0)
    return "Song has been paused..."


def resume_media_player():
    # Pause playback
    win32api.keybd_event(win32con.VK_MEDIA_PLAY_PAUSE, 0,
                         win32con.KEYEVENTF_EXTENDEDKEY, 0)
    return "Song has been resumed."


def change_volume():
    output("Sir, I am able to control the volume level of the system in three levels.")
    output("Press 'M' for 0 percent volume (Mute)")
    output("Press 'L' for 50 percent volume (Low)")
    output("Press 'H' for 100 percent volume (High)")

    try:
        key = input(
            "\033[34mPress the corresponding key to change the volume: \033[0m")
        key = key.upper()
        if key == 'M':
            volume_level = -65.0
            message = 'I have changed the volume to 0%.'
        elif key == 'L':
            volume_level = -6.0206
            message = 'I have changed the volume to 50%.'
        elif key == 'H':
            volume_level = 0.0
            message = 'I have changed the volume to 100%.'
        else:
            return 'Invalid key. Please press a valid key.'

        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevel(volume_level, None)

        return message
    except Exception as e:
        return f'An error occurred while changing the volume: {e}'


'''---------------------------------------------------------------------------------------------------------'''
# import os
# import random
# import Assistant_details as ad
# import win32api
# import win32con
# import subprocess
# import time
# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
# from Output_moule import output

# def play_random_music():
#     if ad.is_window():
#         music_files = [f for f in os.listdir(
#             "C:/Users/manis/Music/") if f.endswith('.mp3')]
#         if music_files:
#             file_path = os.path.join(
#                 "C:/Users/manis/Music/", random.choice(music_files))
#             try:
#                 # Launch Windows Media Player in a separate process
#                 subprocess.Popen(
#                     ['C:/Program Files (x86)/Windows Media Player/wmplayer.exe', file_path])

#                 # Wait for a few seconds before returning control to the calling code
#                 time.sleep(0)

#                 return "Playing music."
#             except Exception as e:
#                 print("Error playing music:", e)
#                 return "Error playing music."
#         else:
#             return "No music files found in directory: C:/Users/manis/Music/."

# def close_media_player():
#     # Set the name of the process to kill
#     process_name = 'wmplayer.exe'

#     # Use the taskkill command to kill any running instances of the process
#     os.system(f'taskkill /im {process_name} /f /t > nul 2>&1')


# def pause_media_player():
#     # Pause playback
#     win32api.keybd_event(win32con.VK_MEDIA_PLAY_PAUSE, 0,
#                          win32con.KEYEVENTF_EXTENDEDKEY, 0)


# def resume_media_player():
#     # Pause playback
#     win32api.keybd_event(win32con.VK_MEDIA_PLAY_PAUSE, 0,
#                          win32con.KEYEVENTF_EXTENDEDKEY, 0)

'''---------------------------------------------------------------------------------------------------------'''
# def change_volume():
#     output("Sir, i am able to controle volume of system in three levels.")
#     output("No.1: For 0 percent volume enter 0")
#     output("No.2: For 50 percent volume enter 5")
#     output("No.3: For 100 percent volume enter 10")

#     level = int(input("Enter volume level here:"))
#     if level == 0:
#         devices = AudioUtilities.GetSpeakers()
#         interface = devices.Activate(
#             IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
#         volume = cast(interface, POINTER(IAudioEndpointVolume))
#         volume.SetMasterVolumeLevel(-65.0, None)
#     elif level == 5:
#         devices = AudioUtilities.GetSpeakers()
#         interface = devices.Activate(
#             IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
#         volume = cast(interface, POINTER(IAudioEndpointVolume))
#         volume.SetMasterVolumeLevel(-6.0206, None)
#     elif level == 10:
#         devices = AudioUtilities.GetSpeakers()
#         interface = devices.Activate(
#             IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
#         volume = cast(interface, POINTER(IAudioEndpointVolume))
#         volume.SetMasterVolumeLevel(0.0, None)
#     else:
#         devices = AudioUtilities.GetSpeakers()
#         interface = devices.Activate(
#             IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
#         volume = cast(interface, POINTER(IAudioEndpointVolume))
#         currentVolumeDb = volume.GetMasterVolumeLevel()
#         volume.SetMasterVolumeLevel(currentVolumeDb + level, None)


'''---------------------------------------------------------------------------------------------------------'''
# THIS ALSO WORK CORRECTLY
# def start_music_default_media_player():
#     # Get a list of all music files in the specified folder
#     music_files = glob.glob(os.path.join( "C:/Users/manis/Music/", '*.mp3'))
#     # Start playing the first music file in the list with the default media player
#     os.startfile(music_files[0])
# # start_music_default_media_player()

# def pause_media_player():
#     # Pause playback
#     win32api.keybd_event(win32con.VK_MEDIA_PLAY_PAUSE, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
# # pause_media_player()

'''---------------------------------------------------------------------------------------------------------'''

# import Assistant_details as ad
# import subprocess
# def play_music():
#     if ad.is_window():
#         subprocess.call(
#           "C:/Program Files (x86)/Windows Media Player/wmplayer.exe /Music/Playlists")
#         return "Playing Music"
#     else:

#         return "Can't play right now!"
# play_music()

'''---------------------------------------------------------------------------------------------------------'''

# from pygame import mixer
# import time
# def play():
#     mixer.init() #Initialzing pyamge mixer

#     mixer.music.load("C:/Users/manis/Music/Kesariya_320(PagalWorld.com.se).mp3") #Loading Music File

#     mixer.music.play() #Playing Music with Pygame

#     time.sleep(100)
# play()
'''---------------------------------------------------------------------------------------------------------'''
# THIS FUNCTION LAUNCH MEDIA PLAYER AND PLAY SONG BUT NOT ALLOWS TO PLAY OTHER SONGS PRESENT IN DIRECTORY SO I SKIPPED IT AND CREATED FOLLOWING FUNCTION.
# def play_random_music():
#     if ad.is_window():
#         music_files = [f for f in os.listdir(
#             "C:/Users/manis/Music/") if f.endswith('.mp3')]
#         if music_files:
#             file_path = os.path.join(
#                 "C:/Users/manis/Music/", random.choice(music_files))
#             os.startfile(file_path)
#             return "Playing music."
#         else:
#             return ("No music files found in directory: " + "C:/Users/manis/Music/" + ".")
'''---------------------------------------------------------------------------------------------------------'''
