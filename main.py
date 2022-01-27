# By Samrat Sarkar -_- https://samratsarkar.in/
import tkinter
import webbrowser
import pyautogui
from tkinter import messagebox

webbrowser.open("https://www.google.com/recaptcha/api2/demo")
pyautogui.PAUSE = 2
pyautogui.click(60, 444, duration=1)
pyautogui.PAUSE = 1
pyautogui.click(60, 510, duration=1)
tkinter.messagebox.showinfo(title="LOL", message="Hey Google It's Me Robot")
# By Samrat Sarkar -_- https://samratsarkar.in/
