import tkinter as tk



def printSomething():
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()
    for x in range(9): # 0 is unnecessary
        label = tk.Label(root, text= str(x))
    # this creates x as a new label to the GUI
        label.pack()

root = tk.Tk()

button = tk.Button(root, text="Print Me", command=printSomething)
button.pack()

root.mainloop()