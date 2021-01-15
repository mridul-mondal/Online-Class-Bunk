from tkinter import *
from datetime import datetime
import webbrowser
import time
import threading
import multiprocessing
now = datetime.now()

root = Tk()
root.title("Pera nai chill")
root.geometry("500x350")
Label(root,font=("arial", 20),text="Please Enter Class details").pack()
Label(root, text="").pack()

def work():
    a= var_a.get()
    b=var_b.get() 
    url=url1.get()
    difference=(int(a)*3600)+(int(b)*60)-(current_hour*3600)-(current_minute*60)-(current_second+5)
    #print(difference)
    Label(root, text="Go to sleep boss.\n Pera nai chill").pack()
    def sleep():
        time.sleep(difference)
        webbrowser.open(url)
    def threadr():
        t1=threading.Thread(target=sleep).start()

    if(difference>=0):
        threadr()
        exit
    else:
        Label(root, text="Enter a valid time").pack()
        time.sleep(3)

var_a=StringVar()
var_a.set("0")
var_b=StringVar()
var_b.set("0")
url1=StringVar()
url1.set("link please")

Label(root,font=("arial", 12), text="Enter Hour in 24 hour formate").pack()
a_entry = Entry(root,width="40", textvariable=var_a).pack()
Label(root,font=("arial", 12), text="Enter Minute").pack()
b_entry = Entry(root,width="40", textvariable=var_b).pack()


Label(root, text="").pack()
Label(root,font=("arial", 12), text="Paste your class link").pack()
link_entry = Entry(root,width="40",textvariable=url1)
link_entry.pack()

current_hour = now.strftime("%H")
current_minute = now.strftime("%M")
current_second =now.strftime("%S")

current_minute = int(current_minute)
current_hour=int(current_hour)
current_second=int(current_second)


Label(root, text="").pack()
Button(root,text="done",width="10",height="2",command=work, bg="#34bdeb").pack()
Label(root, text="").pack()

root.mainloop()