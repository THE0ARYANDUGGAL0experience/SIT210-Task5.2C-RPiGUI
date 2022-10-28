from tkinter import *
import tkinter.font
from gpiozero import LED as RLED
from gpiozero import LED as GLED
from gpiozero import LED as YLED
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# the LED() function of the gpiozero library takes the actually GPIO pin we are using unlike when we are using the setup() from RPi.GPIO which need the location of the GPIO pin
# meaning to use the GPIO pin 14 using the LED() function of the gpiozero library we need to the place the wire in physical pin number 8 but in the program we will pass 14[the exact GPIO pin we are using] as argument in the LED(14) FUNCTION
# however to use the GPIO pin 14 using the setup() from RPi.GPIO we need to the place the wire in physical pin number 8 and in the program we will pass 8[just sepecifing that it is a GPIO pin, we don't need to tell which one] as argument in the setup(8,...) Function

REDled = RLED(14)  
GREENled = GLED(23)
YELLOWled = YLED(17)

win = Tk() #creating a window.
win.title("LED Toggler") #creating  the title of the window.
winFont = tkinter.font.Font(family = 'Helevetica', size = 12, weight = "bold") #define the font colour, size and weight(bold/underline) of the characters of the buttons.

def REDledToggle(): #function to switch the red led on/off.
    if REDled.is_lit: # is_lit checks whether the led is ON or OFF. if it is on then it will be switched OFF when the application is triggered.
        REDled.off()
        REDledButton["text"] = "Turn LED on"
    else: #if the red led is not ON, then it will be switched ON
        REDled.on()
        GREENled.off()
        YELLOWled.off()
        REDledButton["text"] = "Turn LED oFF"

def GREENledToggle(): #function to switch the green led on/off.
    if GREENled.is_lit:
        GREENled.off()
        GREENledButton()["text"] = "Turn LED on"
    else:
        GREENled.on()
        REDled.off()
        YELLOWled.off()
        GREENledButton()["text"] = "Turn LED off"

def YELLOWledToggle(): #function to switch the yellow led on/off.
    if YELLOWled.is_lit:
        YELLOWled.off()
        YELLOWledButton()["text"] = "Turn LED on"
    else:
        YELLOWled.on()
        REDled.off()
        GREENled.off()
        YELLOWledButton()["text"] = "Turn LED off"

def close(): #function to close the GUI program.
    GPIO.cleanup()
    win.destroy()
    REDled.off()
    GREENled.off()
    YELLOWled.off()

#creating the radio buttons
REDledButton = Radiobutton(win, text = 'Turn LED On', font = winFont, command = REDledToggle,bg = 'red', height = 1, width = 24)
REDledButton.grid(row = 0, column = 1)

GREENledButton = Radiobutton(win, text = 'Turn LED On', font = winFont, command = GREENledToggle,bg = 'green', height = 1, width = 24)
GREENledButton.grid(row = 1, column = 1)

YELLOWledButton = Radiobutton(win, text = 'Turn LED On', font = winFont, command = YELLOWledToggle,bg = 'yellow', height = 1, width = 24)
YELLOWledButton.grid(row = 2, column = 1)

exitRedButton = Radiobutton(win, text = 'Exit', font = winFont, command = close,bg = 'bisque2', height = 1, width = 6)
exitRedButton.grid(row = 3, column = 1)

win.protocol("WM_DELETE_WINDOW",close) #switch off all the leds if the GUI is closed.

win.mainloop() #the GUI keeps on running until the Exit or closs is clicked.