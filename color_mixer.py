import tkinter
from tkinter import BOTH

#Define window
root = tkinter.Tk()
root.title('Color Mixer')
root.iconbitmap('./images/palette.ico')
root.geometry('450x500')
root.resizable(0,0)

#Define fonts and colors
#None, using system defaults


#Define functions


#GUI Layout
input_frame = tkinter.LabelFrame(root)
output_frame = tkinter.LabelFrame(root)
input_frame.pack(fill=BOTH, expand=True, padx=5,pady=5)
output_frame.pack(fill=BOTH, expand=True, padx=5,pady=5)

#Setitng up input frame
#Create label, button, slidder for each RGB
red_label = tkinter.Label(input_frame, text='R')
red_slider = tkinter.Scale(input_frame, from_=0, to=255)
red_button = tkinter.Button(input_frame, text='Red')
green_label = tkinter.Label(input_frame, text='G')
green_slider = tkinter.Scale(input_frame, from_=0, to=255)
green_button = tkinter.Button(input_frame, text='Green')
blue_label = tkinter.Label(input_frame, text='B')
blue_slider = tkinter.Scale(input_frame, from_=0, to=255)
blue_button = tkinter.Button(input_frame, text='Blue')
#Create buttons for comp. colors
yellow_button = tkinter.Button(input_frame, text='Yellow')
cyan_button = tkinter.Button(input_frame, text='Cyan')
magenta_button = tkinter.Button(input_frame, text='Magenta')

#Run app
root.mainloop()

