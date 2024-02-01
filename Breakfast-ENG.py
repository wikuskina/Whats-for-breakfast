from tkinter import *
import tkinter as tk
import random
import PIL
from PIL import ImageTk, Image
import os 

# Changing working directory of Python to where the script is located, to enable file opening
os.chdir(os.path.dirname(__file__))
#print("THIS IS DIRECTORY" + os.getcwd())

List_of_choices = ("Delicious omlette!", "Pancakes or blinys!", "Boiled eggs or scrambled eggs (with salmon)!",
	"Healhy oat porridge or muesli!", "Syrniki or pierogi!", "Sandwiches, all sorts!", "Freshly baked croissants!",
	"English Breakfast!","Turkish Breakfast!",
	)

# Show result by selecting from the random list above, can be clicked multiple times
def show_result():
	choice_display = tk.Label(window, text= random.choice(List_of_choices), font="bold", bg="Orange")
	choice_display.pack(padx=1, pady=5, side=tk.TOP)
	window.after(7000, choice_display_destroy, choice_display)

window = tk.Tk()
window.title("What's for Breakfast?")
window.geometry("500x500")
window.resizable(False,False)

# picture for the page
path = "eggs.png"

try:
	img = ImageTk.PhotoImage(Image.open(path))
	panel = Label(window, image=img)
	panel.photo = img
	panel.pack(padx=1, pady=5, side=tk.TOP)
except:
	print("Unable to load image.")

choose_button = tk.Button(window, text = "Click and find out what's for Breakfast!", font="bold", bg="White",
	command=show_result)
choose_button.pack(padx=1, pady=5, side=tk.TOP)


def choice_display_destroy(widget):
	widget.forget()


window.mainloop()