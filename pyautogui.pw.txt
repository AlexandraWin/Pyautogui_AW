Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pyautogui as pg
>>> pg.position
<function position at 0x000001445699F048>
>>> pg.position ()
(65, 195)
>>> pg.moveTo (65,195, 3)
>>> pg.hotkey ('winleft','ctrl','d')
