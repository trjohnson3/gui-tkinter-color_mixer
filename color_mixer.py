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
#Create utility buttons
store_button = tkinter.Button(input_frame, text='Store Color')
save_button = tkinter.Button(input_frame, text='Save')
quit_button = tkinter.Button(input_frame, text='Quit', command=root.destroy)
#Put widgets on input frame
red_label.grid(row=0, column=0)
red_slider.grid(row=1, column=0)
red_button.grid(row=2, column=0)
green_label.grid(row=0, column=1)
green_slider.grid(row=1, column=1)
green_button.grid(row=2, column=1)
blue_label.grid(row=0, column=2)
blue_slider.grid(row=1, column=2)
blue_button.grid(row=2, column=2)
yellow_button.grid(row=3, column=0)
cyan_button.grid(row=3, column=1)
magenta_button.grid(row=3, column=2)
store_button.grid(row=3, column=3)
save_button.grid(row=3, column=4)
quit_button.grid(row=3, column=5)

#Run app
root.mainloop()

