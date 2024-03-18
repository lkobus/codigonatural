import threading
import pygetwindow as gw
import time
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import wave
import pyaudio
import tkinter as tk
import os
import pygame
import pyautogui

should_run = True

def play_audio(file_path):
    CHUNK = 1024

    wf = wave.open(file_path, 'rb')
    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    print("Playing audio...")

    data = wf.readframes(CHUNK)
    while data:
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()
    p.terminate()

def set_volume(application_name, volume_level):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == application_name:
            volume.SetMasterVolume(volume_level, None)
            return

def create_blank_window():
    window = tk.Tk()
    window.geometry("200x200")
    window.title("SoundBoard Python")

    # Define function for closing the window
    def close_window():
        should_run = False
        window.destroy()
        os._exit(0)
        quit()

    # Create a close button
    close_button = tk.Button(window, text="Close Window", command=close_window)
    close_button.pack(pady=10)

    return window

def joystick_handler():    
    audio_file = r'E:\shuffle_overlay\audios\movement-swipe-whoosh-2-186576.wav'
    trigger_button = False
    overlay_button = False
    audio_button = False
    summon_button = False
    team_a_count = 0
    team_b_count = 0
    while should_run:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:                                
                if event.button == 15: #soma a
                    play_audio(audio_file)                
                print("Botão pressionado:", event.button)
                trigger_button = event.button == 10
                overlay_button = event.button == 9
            elif event.type == pygame.JOYBUTTONUP:            
                if event.button == 10:
                    audio_button = False
                if event.button == 9:
                    summon_button = False
                print("Botão liberado:", event.button)        

def write_file(f, value):    
    file_path = f"E:\shuffle_overlay\streamdeck_codigonatural\{f}.txt"
    content = str(value)
    print("writing")
    if value < 9:
        content = f"0{value}"
    with open(file_path, "w") as file:
        # Write the variable's value to the file
        file.write(content)




program_name = "Joystick Streamdeck"
window = create_blank_window()
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
joystick_thread = threading.Thread(target=joystick_handler)
joystick_thread.start()
window.mainloop()
joystick_thread.join()
