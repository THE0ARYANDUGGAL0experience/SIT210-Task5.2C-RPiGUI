from tkinter import *
import tkinter.font
from gpiozero import LED as RLED
from gpiozero import LED as GLED
from gpiozero import LED as YLED
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

REDled = RLED(14)
GREENled = GLED(23)
YELLOWled = YLED(17)

win = Tk() #creating a window.
win.title("LED Toggler") #creating  the title of the window.
winFont = tkinter.font.Font(family = 'Helevetica', size = 12, weight = "bold") # defining custom font

#Button Functionality
def REDledToggle(): # for red led
    if REDled.is_lit:
        REDled.off()
        REDledButton["text"] = "Turn LED on"
    else:
        REDled.on() # only red led will glow others will be turned off.
        GREENled.off()
        YELLOWled.off()
        REDledButton["text"] = "Turn LED oFF"

def GREENledToggle(): # for green led
    if GREENled.is_lit:
        GREENled.off()
        GREENledButton()["text"] = "Turn LED on"
    else:
        GREENled.on() # only green led will glow others will be turned off.
        REDled.off()
        YELLOWled.off()
        GREENledButton()["text"] = "Turn LED off"
        
def YELLOWledToggle(): # for yellow led
    if YELLOWled.is_lit:
        YELLOWled.off()
        YELLOWledButton()["text"] = "Turn LED on"
    else:
        YELLOWled.on() # only yellow led will glow others will be turned off.
        REDled.off()
        GREENled.off()
        YELLOWledButton()["text"] = "Turn LED off"

def close(): # closing all the leds
    GPIO.cleanup()
    win.destroy()
    REDled.off()
    GREENled.off()
    YELLOWled.off()

#Buttons creation
REDledButton = Button(win, text = 'Turn LED On', font = winFont, command = REDledToggle,bg = 'red', height = 1, width = 24)
REDledButton.grid(row = 0, column = 1)

GREENledButton = Button(win, text = 'Turn LED On', font = winFont, command = GREENledToggle,bg = 'green', height = 1, width = 24)
GREENledButton.grid(row = 1, column = 1)

YELLOWledButton = Button(win, text = 'Turn LED On', font = winFont, command = YELLOWledToggle,bg = 'yellow', height = 1, width = 24)
YELLOWledButton.grid(row = 2, column = 1)

exitRedButton = Button(win, text = 'Exit', font = winFont, command = close,bg = 'bisque2', height = 1, width = 6)
exitRedButton.grid(row = 3, column = 1)

win.protocol("WM_DELETE_WINDOW",close) #exit cleanly

win.mainloop() #loops forever

