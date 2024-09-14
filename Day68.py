import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Gerald Ford")

image = Image.open("gerald ford.jpg")
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.image = photo
label.pack()

def hide_photo():
    label.pack_forget()

button = tk.Button(root, text="Hide", command=hide_photo)
button.pack()

root.mainloop()
