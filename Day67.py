from PIL import Image, ImageTk
import tkinter as tk

def show_gerald_ford():
    window = tk.Toplevel(root)
    window.title("Gerald Ford")
    image = Image.open("gerald ford.jpg")
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(window, image=photo)
    label.image = photo
    label.pack()

root = tk.Tk()
button = tk.Button(root, text="Click me", command=show_gerald_ford)
button.pack()
root.mainloop()
