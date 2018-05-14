import win32com.client as wincl
import pyautogui as pg

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak ("Do you like to watch vines?")

answer = pg.prompt("Enter if you like vines")

if answer == "yes":
    speak.Speak("OMG SAME!!! I love vines")

speak.Speak ("Ok, searching YouTube for best vine compliations

wb.open 
