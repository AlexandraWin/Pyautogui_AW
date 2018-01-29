import pyautogui as pg
import time
import webbrowser 

points = 0 

answer = pg.prompt(
"""
Do you like waffles?
a) yes
b) no
c) a little
"""
    )

if answer == 'a':
    points +=1
elif answer == 'b':
    points +=2
elif answer == 'c':
    points +=3

answer = pg.prompt(
"""
Who is your hairstyle icon?
a) Steve
b) Eleven
c) Will
d) Dustin
"""
    )
if answer == 'a':
    points +=1
elif answer == 'b':
    points +=2
elif answer == 'c':
    points +=8
elif answer == 'd':
    points -=2


answer = pg.prompt(
"""
Hawkins AV club
a) Cool
b)Drool

"""
    )
if answer == 'a':
    points +=5
elif answer == 'b':
    points -=5


answer = pg.prompt(
"""
Weapon of your choice
a) a trap
b) a gun
c) a bat with nails

"""
    )
if answer == 'a':
    points +=1
elif answer == 'b':
    points +=2
elif answer == 'c':
    points +=5

answer = pg.prompt(
"""
What would you dress up as for Hallowen?
a) a zombie
b) a demogorgan
c) ghostbusters

"""
    )
if answer == 'a':
    points -=1
elif answer == 'b':
    points +=3
elif answer == 'c':
    points +=5





#END OF SURVEY
pg.alert("Could you survive in the Upside Down? Click for the answer")

#YES
if points < 10:
    pg.alert("You would be able to survive in the Upside Down")
    webbrowser.open ("http://dorkshelf.com/wordpress/wp-content/uploads//2016/07/Stranger-Things-Nancy-Featured.jpg")
#NO
if points > 10:
    pg.alert ("You would not be able to surve the upside down")
    webbrowser.open ("https://vignette.wikia.nocookie.net/strangerthings8338/images/7/7a/WillUpsideDown.jpg/revision/latest?cb=20160819172152")
