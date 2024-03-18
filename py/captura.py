import threading
import pygetwindow as gw
import time
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import wave
import pyaudio
import tkinter as tk
import os
import pygame
import sounddevice as sd
import pygame
import numpy as np
import time
import soundfile as sf
from scipy import signal
import pyaudio
import wave
import pygetwindow as gw
import time
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import wave
import pyaudio
import pyautogui



# Inicializa o pygame
pygame.init()

# Inicializa o joystick
pygame.joystick.init()

# Verifica se algum joystick está conectado
if pygame.joystick.get_count() == 0:
    print("Nenhum joystick detectado.")
    quit()

# Obtém o primeiro joystick conectado
joystick = pygame.joystick.Joystick(0)
joystick.init()

def write_file(f, value):    
    file_path = f"E:\shuffle_overlay\streamdeck_codigonatural\{f}.txt"
    content = str(value)
    if value < 9:
        content = f"0{value}"
    with open(file_path, "w") as file:
        # Write the variable's value to the file
        file.write(content)

trigger_button = False
overlay_button = False
team_a_count = 0
team_b_count = 0

#

print("Joystick conectado:", joystick.get_name())
while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:    
            if trigger_button:
                if event.button == 11: #soma a
                    team_a_count = team_a_count + 1
                    write_file('team_a_count', team_a_count)         
                if event.button == 12:#tira a
                    team_a_count = team_a_count - 1
                    write_file('team_a_count', team_a_count)         
                if event.button == 3: #soma b
                    team_b_count = team_b_count + 1                       
                    write_file('team_b_count', team_b_count)         
                if event.button == 0:#tira b
                    team_b_count = team_b_count - 1           
                    write_file('team_b_count', team_b_count)         
            if overlay_button:
                if event.button == 4:# botão share
                    pyautogui.hotkey('ctrl', '-', interval=0.25)                                        
                if event.button == 6:# botão option
                    pyautogui.hotkey('ctrl', '=', interval=0.25)                                        
            print("Botão pressionado:", event.button)
            trigger_button = event.button == 10
            overlay_button = event.button == 9
        elif event.type == pygame.JOYBUTTONUP:            
            print("Botão liberado:", event.button)        