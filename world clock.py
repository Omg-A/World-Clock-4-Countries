from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
import pytz
import time

root = Tk()
root.title("World Clock")
root.geometry("700x800")
root.configure(background="white")

clock_image = ImageTk.PhotoImage(Image.open("clock.jpg"))

#India
label_india_name = Label(root, text="India Time", bg="white")
label_india_name.place(relx=0.27, rely=0.01, anchor=CENTER)

label_india_image = Label(root, image=clock_image)
label_india_image.place(relx=0.27, rely=0.2, anchor=CENTER)

label_india_time = Label(root, bg="white")
label_india_time.place(relx=0.27, rely=0.45, anchor=CENTER)

#USA
label_usa_name = Label(root, text="USA Time", bg="white")
label_usa_name.place(relx=0.73, rely=0.01, anchor=CENTER)

label_usa_image = Label(root, image=clock_image)
label_usa_image.place(relx=0.73, rely=0.2, anchor=CENTER)

label_usa_time = Label(root, bg="white")
label_usa_time.place(relx=0.73, rely=0.45, anchor=CENTER)

#Japan
label_japan_name = Label(root, text="Japan Time", bg="white")
label_japan_name.place(relx=0.27, rely=0.5, anchor=CENTER)

label_japan_image = Label(root, image=clock_image)
label_japan_image.place(relx=0.27, rely=0.7, anchor=CENTER)

label_japan_time = Label(root, bg="white")
label_japan_time.place(relx=0.27, rely=0.95, anchor=CENTER)

#Australia australia
label_australia_name = Label(root, text="Australia Time", bg="white")
label_australia_name.place(relx=0.73, rely=0.5, anchor=CENTER)

label_australia_image = Label(root, image=clock_image)
label_australia_image.place(relx=0.73, rely=0.7, anchor=CENTER)

label_australia_time = Label(root, bg="white")
label_australia_time.place(relx=0.73, rely=0.95, anchor=CENTER)

class India:
    def time(self):
        home = pytz.timezone("Asia/Kolkata")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H: %M: %S")
        label_india_time["text"] = "Time: " + current_time
        label_india_time.after(200, self.time)

class USA:
    def time(self):
        home = pytz.timezone("US/Central")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H: %M: %S")
        label_usa_time["text"] = "Time: " + current_time
        label_usa_time.after(200, self.time)

class Japan:
    def time(self):
        home = pytz.timezone("Japan")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H: %M: %S")
        label_japan_time["text"] = "Time: " + current_time
        label_japan_time.after(200, self.time)

class Australia:
    def time(self):
        home = pytz.timezone("Australia/ACT")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H: %M: %S")
        label_australia_time["text"] = "Time: " + current_time
        label_australia_time.after(200, self.time)

obj_india = India()
obj_usa = USA()
obj_japan = Japan()
obj_australia = Australia()

button_india = Button(root, text="Show Time", command=obj_india.time)
button_india.place(relx=0.27, rely=0.4, anchor=CENTER)

button_usa = Button(root, text="Show Time", command=obj_usa.time)
button_usa.place(relx=0.73, rely=0.4, anchor=CENTER)

button_japan = Button(root, text="Show Time", command=obj_japan.time)
button_japan.place(relx=0.27, rely=0.9, anchor=CENTER)

button_australia = Button(root, text="Show Time", command=obj_australia.time)
button_australia.place(relx=0.73, rely=0.9, anchor=CENTER)

root.mainloop()