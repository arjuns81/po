from tkinter import*
root=Tk()
root.title("color dictionary")
root.geometry("600x400")
label_of_red = Label(root)
label_of_blue = Label(root)
label_of_purple = Label(root)

dictionary = {'red':'red is a primary colour,','blue': 'blue is also a primary colour,' 
              'purple': 'purple is blue and red mixed'}

def red():
    label_of_red["text"] = dictonary['red']
    
def blue():
    label_of_red["text"] = dictonary['blue']
    
def purple():
    label_of_purple["text"] = dictonary['purple']
    
    button_blue=Button(root,text="meaning of purple",command = mutable)
    button_blue.place(relx = 0.5, rely =0.2, anchor = CENTER)

    label_of_mutable.place(relx = 0.5, rely =0.3, anchor = CENTER)

    button_red = Button(root, text = "Meaning of Immutable",command =  immutable)
    button_red.place(relx = 0.5, rely =0.4, anchor = CENTER)

    label_of_immutable.place(relx = 0.5, rely =0.5, anchor = CENTER)

    button_purple = Button(root, text = "Meaning of Tkinter", command = tkinter)
    button_purple.place(relx = 0.5, rely =0.6, anchor = CENTER)

    label_of_purple.place(relx = 0.5, rely =0.7, anchor = CENTER)

    root.mainloop()