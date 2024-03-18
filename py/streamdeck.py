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
    file_path = f"E:\shuffle_overlay\overlay_streamdeck\{f}.txt"
    content = str(value)
    if value < 9:
        content = f"0{value}"
    with open(file_path, "w") as file:
        # Write the variable's value to the file
        file.write(content)

print("Joystick conectado:", joystick.get_name())
match_count = 0
team_a = 0
team_b = 0
trigger_pressed = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:                                                
            if trigger_pressed:
                if event.button == 4:                    
                    pyautogui.hotkey('ctrl', '-', interval=0.25)                    
                if event.button == 6:                    
                    pyautogui.hotkey('ctrl', '+', interval=0.25)                    
                if event.button == 11:
                    team_a += 1
                    print(team_a)
                    write_file("team_a_count", team_a)
                if event.button == 12:                    
                    team_a -= 1
                    write_file("team_a_count", team_a)
                if event.button == 3:
                    team_b += 1
                    write_file("team_b_count", team_b)
                if event.button == 0:
                    team_b -= 1
                    write_file("team_b_count", team_b)
                if event.button == 2:
                    match_count -= 1
                    write_file("match_count", match_count)
                if event.button == 1:
                    match_count += 1
                    write_file("match_count", match_count)
                if event.button == 9:                    
                    team_a = 0
                    team_b = 0
                    match_count = 0
                    write_file("team_a_count", team_a)
                    write_file("team_b_count", team_b)
                    write_file("match_count", match_count)
                print("Botão pressionado:", event.button)
            trigger_pressed = event.button == 10
        elif event.type == pygame.JOYBUTTONUP:
            trigger_pressed = False
            print("Botão liberado:", event.button)
        elif event.type == pygame.JOYAXISMOTION:
            if event.axis == 0:
                print("Eixo X:", event.value)
            elif event.axis == 1:
                print("Eixo Y:", event.value)
        elif event.type == pygame.JOYHATMOTION:
            print("Hat (direcional):", event.value)
