import webbrowser
import pyautogui as pg

videos = ["https://www.youtube.com/watch?v=-RkaFw0QrRo&pbjreload=10"]

Music = ["https://www.youtube.com/watch?v=xpVfcZ0ZcFM", "https://www.youtube.com/watch?v=Wk008A"]

answer = pg.prompt (
"""

What videos do you want to do?
a) videos
b) music

"""
    )

if answer == "a":
    for i in videos:
         webbrowser.open(i)
elif answer == "b":
    for i in videos:
        webbrowser.open(i)
