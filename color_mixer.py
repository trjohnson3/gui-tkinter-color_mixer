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

#Run app
root.mainloop()

