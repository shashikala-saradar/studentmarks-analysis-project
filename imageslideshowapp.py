#pip install pillow
from itertools import cycle         #repeat a list again and again(any iterable like tuple,string,set,range
from PIL import Image,ImageTk  #this is from pillow library.
# Image-->open and resize images
# ImageTk-->convert image to Tkinter format
import time
import tkinter as tk

root=tk.Tk()                        #create a main window
root.title("image slideshow Viewer")

#List of Image path
image_paths=[
    r"C:\Users\DELL\OneDrive\Documents\IDCARD.jpg",
    r"C:\Users\DELL\OneDrive\Documents\adharcard.jpeg",
    r"C:\Users\DELL\OneDrive\Documents\shashikalaimage.jpg",
]

#resize the images to 1080X1080

image_size=(1080,1080)
images=[Image.open(path).resize(image_size) for path in image_paths]

photo_images=[ImageTk.PhotoImage(image) for image in images]
label=tk.Label(root)            #creates empty box
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)       #puts image in it
        label.update()     #refresh the window immeditaltely
        time.sleep(3)

slideshow=cycle(photo_images)      #this makes images repeat infinitely

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button=tk.Button(root,text="play slideshow",command=start_slideshow)
play_button.pack()

root.mainloop()