# ver. Sun/17/Dec/2023
#
# Made by: CyberCoral
# ------------------------------------------------
# Github:
# https://www.github.com/CyberCoral
#

###
### Download VLC: https://www.videolan.org/vlc/index.es.html
###

###
### Download Python3: https://www.python.org/downloads/
###

##  Steps to use this:
##    -Step 1: Open VLC
##    -Step 2: Click on the VLC window.
##    -Step 3: Click on IDLE/Shell
##    -Step 4: Enter VLC_auto_player(settings you want to use)
##              VLC_auto_player(loops = True || False, txt_files = [...], right_s = 1 (don't change))
##    -Step 5: Enjoy :D

###
### Import modules.
###

# built-in
import os, sys, subprocess, platform, re

with open("requirements.txt","r") as f:
    a =[f.readlines()][0]
    a = [(lambda b,c: c[b][::-1][1:][::-1] if b != len(c) - 1 else c[b])(i, a) for i in range(len(a))]

    import importlib
    for i in range(len(a)):
        loader = importlib.util.find_spec(a[i])
        if loader == None:
            os.system(f"python -m pip install {a[i]}")
    
import pyautogui, pyperclip
import pyscreenshot

# not in modules
from imagesearch import *

# built-in
import time
import keyboard

import Automated_Error_Checks as AEC

###
### The functions themselves.
###

def determine_position(interval: int = 3):
    '''
    This program determines the
    position of the mouse and it loops
    until you press Ctrl-C.
    You can determine the interval of
    coordinate printing with interval.
    '''
    AEC.AutomatedErrorTypeFinder([interval],["1"])
    AEC.AutomatedConditionCheck([interval],["var > 0"],[2])
    
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr,"\n\n")
            time.sleep(interval)
    except KeyboardInterrupt:
        print('\n')

def hold_and_press(hold: list = ["shift"], press: list = ["v"]):
    '''
    It performs pyautogui.hold() and
    pyautogui.press() but good.
    '''
    AEC.AutomatedErrorTypeFinder([hold, press],["00001","00001"])
    AEC.AutomatedConditionCheck([hold, press],["len(var) >= 0","len(var) >= 0"],[2,2])

    for i in hold:
        pyautogui.keyDown(i)

    pyautogui.press(press)

    for i in hold[::-1]:
        pyautogui.keyUp(i)

##  Steps to use this:
##    -Step 1: Open VLC
##    -Step 2: Click on the VLC window.
##    -Step 3: Click on IDLE/Shell
##    -Step 4: Enter VLC_auto_player(...)
##    -Step 5: Enjoy :D
        
def VLC_auto_player(loop: bool = True,*,txt_files: str = ['music_for_vlc.txt'], right_s: int = 1):
    '''
    It autoplays the urls of a specific file
    or files (if txt_files has 2 strings or more)
    (default being ['music_for_vlc.txt']).
    Steps to use this:
    -Step 1: Open VLC
    -Step 2: Click on the VLC window.
    -Step 3: Click on IDLE/Shell/IDE
    -Step 4: Enter VLC_auto_player(...)
    -Step 5: Enjoy :D
    '''
    s_prime = []
    
    def put_new_song(s_prime):
        for i in range(len(s_prime)):
            loaded = s_prime[i]
            pyperclip.copy(loaded)

            pyautogui.hotkey("ctrl","n")
            time.sleep(0.3)
            pyautogui.hotkey("ctrl","v")
            pyautogui.hotkey("enter")

            image=pyscreenshot.grab(bbox=(0, 0, 1500, 45))
            time.sleep(2)
            image.save(f'blank.png')         
            time.sleep(3) 
        
            while True:
                pos = imagesearch(f'blank.png')
                if pos == [-1,-1]:
                    break

            os.remove("blank.png")
                
    try:
        AEC.AutomatedErrorTypeFinder([loop, right_s, txt_files],["1","1","00001"])
        AEC.AutomatedConditionCheck([right_s,txt_files,[txt_files[i][::-1][:4][::-1] == '.txt' for i in range(len(txt_files))], [isinstance(txt_files[i], str) == True for i in range(len(txt_files))]],["var >= 0","len(var) >= 1","var.count(False) == 0","var.count(False) == 0"],[2,2,2,2])
        for i in range(len(txt_files)):
            try:
                with open(txt_files[i], "r") as f:
                    s_prime.append(f.readlines())
            except FileNotFoundError:
                open(sys.argv[0][::-1][:12][::-1].replace("\\","/")+"/"+txt_files[i],"w")
                print("File created at {}.".format(txt_files[i]))
                return 0

        print("There are {} songs in your playlist.".format(len(s_prime)))

        print("You can stop the program to loop itself with Ctrl+C.")

        time.sleep(2)

        if right_s != 0:
            hold_and_press(["alt","tab"],["right"*(right_s-1)])

        time.sleep(0.4)

        if loop != True:
            for i in range(len(txt_files)):
                put_new_song(s_prime[i])         

        else:
            while True:
                for i in range(len(txt_files)):
                    put_new_song(s_prime[i])         

    except KeyboardInterrupt:
        print("Thanks for using this program, goodbye user :D")
        time.sleep(2)
    
    os.remove("blank.png")
    
    exit(0)

def create_playlist(txt_file: str = "playlist_0.txt", *songs):
    '''
    It creates a playlist
    (file with links to songs or vids)
    automatically.
    Please put adequate links for you
    to use on this program.
    '''
    AEC.AutomatedErrorTypeFinder([txt_file],["0000001"])
    AEC.AutomatedConditionCheck([songs,txt_file, [songs[i][:8] == "https://" for i in range(len(songs))]],["len(var) >= 1","var[::-1][:4][::-1] == '.txt'","var.count(False) == 0"],[2,2,2])

    songs = list(songs)
    with open(txt_file,"a") as f:
        for i in range(len(songs)):
            songs[i] = songs[i].replace("https://","http://")
            f.write(f"{songs[i]}\n")

def file_auto_player(loops: bool = True,cmd_gen: bool = True,txt_: bool = False,*,files: list = [""]):
    '''
    It auto plays any file
    (mp3, mp4, avi...) on VLC,
    and it works for Windows 
    and Linux (WIP).
    '''
    AEC.AutomatedErrorTypeFinder([loops,cmd_gen,files, txt_],["1","1","00001","1"])
    AEC.AutomatedConditionCheck([[isinstance(files[i], str) for i in range(len(files))]],["var.count(False) == 0"],[2])

    os.chdir("/")
    folder = sys.argv[0].replace("\\","/")
    folder = folder[:re.search("VLC_player",folder).end()]+"/"
    os.chdir(folder)

    try:
        def windows_part(files, cmd_gen: bool = True, txt_: bool = False):
            s_prime = []
            if txt_ == True:
                for i in range(len(files)):
                    with open(files[i], "r") as f:
                        s_prime.append(f.readlines())
            else:
                s_prime=[list(files)]

            for j in range(len(s_prime)):
                files = s_prime[j]
                for i in range(len(files)):
                    try:
                        os.system(f'start /b cmd /k "%PROGRAMFILES%/VideoLAN/VLC/vlc.exe" {files[i]}')
                        time.sleep(1)
                        if cmd_gen == True:
                            hold_and_press(["alt","tab"],[])
                            pyautogui.hotkey("alt","f4")
                        
                        image=pyscreenshot.grab(bbox=(0, 0, 1500, 45))
                        time.sleep(2)
                        image.save(f'blank.png')         
                        time.sleep(3) 
                        while True:
                            pos = imagesearch(f'blank.png')
                            if pos == [-1,-1]:
                                break

                        pyautogui.hotkey("alt","f4")
                        
                    except FileNotFoundError:
                        pass

        def linux_part(files, txt_: bool = False):
            s_prime = []
            if txt_ == True:
                for i in range(len(files)):
                    with open(files[i], "r") as f:
                        s_prime.append(f.readlines())
            else:
                s_prime=[list(files)]

            for j in range(len(s_prime)):
                files = s_prime[j]            
                for i in range(len(files)):
                    try:             
                        subprocess.run(["vlc",files[i]])
                        
                        image=pyscreenshot.grab(bbox=(0, 0, 1500, 45))
                        time.sleep(2)
                        image.save(f'blank.png')         
                        time.sleep(3) 
                        while True:
                            pos = imagesearch(f'blank.png')
                            if pos == [-1,-1]:
                                break

                        pyautogui.hotkey("alt","f4")

                    except FileNotFoundError:
                        pass

        if platform.system() == "Windows":
            if loops != True:
                windows_part(files,cmd_gen, txt_)
            else:
                while True:
                    windows_part(files,cmd_gen, txt_)
            
        elif platform.system() == "Linux":
            if loops != True:
                linux_part(files, txt_)
            else:
                while True:
                    linux_part(files, txt_)

        else:
            raise OSError("OS {} is not supported.".format(platform.system()))

    except KeyboardInterrupt:  
        print("Thanks for using this program, goodbye user :D")
        time.sleep(2)

    os.remove('blank.png')

    exit(0)
