from tkinter import*
import random

root=Tk()
root.title("random countries")
root.geometry

enter_name=Entry(root)
def addfriend():
    friend_name = enter_name.get()
    list1.append(friend_name)
    friend_list["text"] = "Your countries : " + str(list1)
    
def random_number():
    length = len(list1)
    random_no = random.randint(0, length-1)
    random_number_label["text"] = str(random_no)
    generated_random_number = list1[random_no]
    lucky_friend["text"] = "your =capital is: " + str(generated_random_number)
    
btn = Button(root, text="Add to thecapital list", command = addfriend)
btn.place(relx= 0.5,rely = 0.3, anchor = CENTER)

friend_list.place(relx= 0.5,rely = 0.4, anchor = CENTER)

btn1 = Button(root, text="What is your capital?  ", command = random_number)
btn1.place(relx= 0.5,rely = 0.5, anchor = CENTER )

random_number_label.place(relx= 0.5,rely = 0.6, anchor = CENTER)
lucky_friend.place(relx= 0.5,rely = 0.7, anchor = CENTER)

root.mainloop()