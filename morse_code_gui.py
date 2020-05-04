from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
led = LED(27)

# Dictionary representing the morse code chart
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ':' '}

def long_blink():
    led.on()
    sleep(1.5)
    led.off()
    sleep(0.5)

def short_blink():
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)

def space():
    sleep(1.5)

def encrypt():
    ciphertext = ""
    plaintext = textBox.get()
    if len(plaintext) > 12:
        return

    for ch in plaintext:
        for x in MORSE_CODE[ch.upper()]:
            if x == '-':
                long_blink()
            elif x == '.':
                short_blink()
            else:
                space()
        space()

#GUI Definitions
root = Tk()
root.title("Morse Code Translator")
myCanvas = Canvas(root, width=400, height=300)
myCanvas.pack()
myFont = tkinter.font.Font(family="Helvetica", size=12, weight="bold")

#Widgets
textLabel = Label(root, font=myFont, text="Enter message (max 12 characters)")
myCanvas.create_window(200, 100, window=textLabel)

textBox = Entry(root)
myCanvas.create_window(200, 140, window=textBox)

submitButton = Button(text="Encrypt message", command=encrypt)
myCanvas.create_window(200, 180, window=submitButton)

root.mainloop()
