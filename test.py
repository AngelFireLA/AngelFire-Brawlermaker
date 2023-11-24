import tkinter as tk

root = tk.Tk()

default_text = tk.StringVar(root, value='Enter text here')
text_box = tk.Entry(root, textvariable=default_text)
text_box.pack()

#text_box.bind("<FocusIn>", lambda _: default_text.set(''))

root.mainloop()