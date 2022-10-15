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
winFont = tkinter.font.Font(family = 'Helevetica', size = 12, weight = "bold")

def REDledToggle():
    if REDled.is_lit:
        REDled.off()
        REDledButton["text"] = "Turn LED on"
    else:
        REDled.on()
        GREENled.off()
        YELLOWled.off()
        REDledButton["text"] = "Turn LED oFF"

def GREENledToggle():
    if GREENled.is_lit:
        GREENled.off()
        GREENledButton()["text"] = "Turn LED on"
    else:
        GREENled.on()
        REDled.off()
        YELLOWled.off()
        GREENledButton()["text"] = "Turn LED off"
        
def YELLOWledToggle():
    if YELLOWled.is_lit:
        YELLOWled.off()
        YELLOWledButton()["text"] = "Turn LED on"
    else:
        YELLOWled.on()
        REDled.off()
        GREENled.off()
        YELLOWledButton()["text"] = "Turn LED off"

def close():
    GPIO.cleanup()
    win.destroy()
    REDled.off()
    GREENled.off()
    YELLOWled.off()

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

