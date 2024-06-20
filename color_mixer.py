import tkinter
from tkinter import BOTH, IntVar, DISABLED

#Define window
root = tkinter.Tk()
root.title('Color Mixer')
root.iconbitmap('./images/color.ico')
root.geometry('450x500')
root.resizable(0,0)

#Define functions
def get_red(slider_value):
    '''Get slider value from red scale and turn into a hex value and update color.
    Scale value is autoupdated when moved, so it needs a parameter for it.'''
    global red_value
    #Turn slider value into an int and hex, strip leading characters so only 2 remain
    red_value = hex(int(slider_value))
    red_value = red_value.strip('0x')
    #If hex value is single didgit, prepend a 0
    while len(red_value) < 2:
        red_value = '0' + str(red_value)
    update_color()


def get_green(slider_value):
    '''Get slider value from green scale and turn into a hex value and update color.
    Scale value is autoupdated when moved, so it needs a parameter for it.'''
    global green_value
    #Turn slider value into an int and hex, strip leading characters so only 2 remain
    green_value = hex(int(slider_value))
    green_value = green_value.strip('0x')
    #If hex value is single didgit, prepend a 0
    while len(green_value) < 2:
        green_value = '0' + str(green_value)
    update_color()


def get_blue(slider_value):
    '''Get slider value from blue scale and turn into a hex value and update color.
    Scale value is autoupdated when moved, so it needs a parameter for it.'''
    global blue_value
    #Turn slider value into an int and hex, strip leading characters so only 2 remain
    blue_value = hex(int(slider_value))
    blue_value = blue_value.strip('0x')
    #If hex value is single didgit, prepend a 0
    while len(blue_value) < 2:
        blue_value = '0' + str(blue_value)
    update_color()
    

def update_color():
    '''update current color box based on slider values. Display tuple
    and hex value of current color'''
    #Make the color box smaller than the original due internal padding on original
    color_box = tkinter.Label(input_frame, bg='#' + red_value + green_value + blue_value,
                              width=15, height=6)
    color_box.grid(row=1, column=3, columnspan=2, padx=35, pady=10)
    #Display hex and tuple values
    color_tuple.config(text='(' + str(red_slider.get()) + ') ,'
                       + '(' + str(green_slider.get()) + ') ,'
                       + '(' + str(blue_slider.get()) + ')')
    color_hex.config(text='#' + red_value + green_value + blue_value)


def set_color(red_value, green_value, blue_value):
    '''Set slider values equal to red.'''
    red_slider.set(red_value)
    green_slider.set(green_value)
    blue_slider.set(blue_value)


#GUI Layout
input_frame = tkinter.LabelFrame(root, padx=5, pady=5)
output_frame = tkinter.LabelFrame(root, padx=5, pady=5)
input_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)
output_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

#Setting up input frame
#Create label, button, slidder for each RGB
red_label = tkinter.Label(input_frame, text='R')
red_slider = tkinter.Scale(input_frame, from_=0, to=255, command=get_red)
red_button = tkinter.Button(input_frame, text='Red', command=lambda:set_color(255, 0, 0))
green_label = tkinter.Label(input_frame, text='G')
green_slider = tkinter.Scale(input_frame, from_=0, to=255, command=get_green)
green_button = tkinter.Button(input_frame, text='Green', command=lambda:set_color(0, 255, 0))
blue_label = tkinter.Label(input_frame, text='B')
blue_slider = tkinter.Scale(input_frame, from_=0, to=255, command=get_blue)
blue_button = tkinter.Button(input_frame, text='Blue', command=lambda:set_color(0, 0, 255))

#Create buttons for comp. colors
yellow_button = tkinter.Button(input_frame, text='Yellow', command=lambda:set_color(255, 255, 0))
cyan_button = tkinter.Button(input_frame, text='Cyan', command=lambda:set_color(0, 255, 255))
magenta_button = tkinter.Button(input_frame, text='Magenta', command=lambda:set_color(255, 0, 255))

#Create utility buttons
store_button = tkinter.Button(input_frame, text='Store Color')
save_button = tkinter.Button(input_frame, text='Save')
quit_button = tkinter.Button(input_frame, text='Quit', command=root.destroy)

#Put widgets on input frame
red_label.grid(row=0, column=0, sticky='W')
red_slider.grid(row=1, column=0, sticky='W')
red_button.grid(row=2, column=0, padx=1, pady=1, ipadx=20)
green_label.grid(row=0, column=1, sticky='W')
green_slider.grid(row=1, column=1, sticky='W')
green_button.grid(row=2, column=1, padx=1, pady=1, ipadx=15)
blue_label.grid(row=0, column=2, sticky='W')
blue_slider.grid(row=1, column=2, sticky='W')
blue_button.grid(row=2, column=2, padx=1, pady=1, ipadx=20)
yellow_button.grid(row=3, column=0, padx=1, pady=1, sticky='WE')
cyan_button.grid(row=3, column=1, padx=1, pady=1, sticky='WE')
magenta_button.grid(row=3, column=2, padx=1, pady=1, sticky='WE')
store_button.grid(row=4, column=0, columnspan=3, padx=1, pady=1, sticky='WE')
save_button.grid(row=4, column=3, padx=1, pady=1, sticky='WE')
quit_button.grid(row=4, column=4, padx=1, pady=1, sticky='WE')

#Create color box and color labels
color_box = tkinter.Label(input_frame, bg='black', height=6, width=15)
color_tuple = tkinter.Label(input_frame, text='(0), (0), (0)')
color_hex = tkinter.Label(input_frame, text='#000000')

#Put on the frame
color_box.grid(row=1, column=3, columnspan=2, padx=35, pady=10, ipadx=10, ipady=10)
color_tuple.grid(row=2, column=3, columnspan=2)
color_hex.grid(row=3, column=3, columnspan=2)

#Setup output frame
#Initialize a dictionary to hold all stored colors
stored_colors = {}
stored_color = IntVar()

#Create radio buttons to select stores values and populate rows with selected values
for i in range(6):
    radio = tkinter.Radiobutton(output_frame, variable=stored_color, value=i)
    radio.grid(row=i, column=0, sticky='W')
    recall_button = tkinter.Button(output_frame, text='Recall Color', state=DISABLED)
    new_color_tuple = tkinter.Label(output_frame, text='(255), (255), (255)')
    new_color_hex = tkinter.Label(output_frame, text='#FFFFFF')
    new_color_black_box = tkinter.Label(output_frame, bg='black', width=3, height=1)
    new_color_box = tkinter.Label(output_frame, bg='white', width=3, height=1)

    recall_button.grid(row=i, column=1, padx=20)
    new_color_tuple.grid(row=i, column=2, padx=20)
    new_color_hex.grid(row=i, column=3, padx=20)
    new_color_black_box.grid(row=i, column=4, pady=2, ipadx=5, ipady=5)
    new_color_box.grid(row=i, column=4)

    #.cget() returns teh value of a specific option. Store the text value for tuple and hex.
    stored_colors[stored_color.get()] = [new_color_tuple.cget('text'), new_color_hex.cget('text')]

#Initialize starting values for color box display
red_value = '00'
green_value = '00'
blue_value = '00'

#Run app
root.mainloop()

