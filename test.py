import tkinter as tk

def blank_function():
    # Replace this with your desired functionality
    pass

root = tk.Tk()
root.title("Tkinter Example")
root.geometry('400x200')

# Create a button
button = tk.Button(root, text="Run Blank Function", command=blank_function)
button.pack()

root.mainloop()