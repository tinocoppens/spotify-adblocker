import os
import inspect, os.path
filename = inspect.getframeinfo(inspect.currentframe()).filename
path     = os.path.dirname(os.path.abspath(filename))
print(path)
theamifile = path + "\AreModulesInstalled"
str(theamifile)
def installmodules():
    os.system("pip3 install elevate")
    os.system("pip3 install requests")
    os.system("pip install tkinter")
    blabfjfh = open(theamifile, "w")
    blabfjfh.write("1")
    blabfjfh.close()
dskfjkl = open(theamifile, "r")
slobo = dskfjkl.read()
if slobo == "0":
    installmodules()
    dskfjkl.close()
from tkinter import *
from tkinter import ttk
from elevate import elevate
import requests
elevate()
def disableadservers(status):
    if status == "on":
        getadservers = requests.get("https://tinocoppens.github.io/hostslist/").text
        importtohosts = open("C:/Windows/System32/drivers/etc/hosts", "w")
        importtohosts.write(getadservers)
        importtohosts.close
    if status == "off":
        os.remove("C:/Windows/System32/drivers/etc/hosts")
        importtohosts = open("C:/Windows/System32/drivers/etc/hosts", "w")
        importtohosts.write("")
        importtohosts.close
def home():
    a = input("Typ on to enable spotify adblocker, typ off to disable spotify adblocker. : ")
    if a == "on":
        disableadservers("on")
        print("Blocking ads.")
    if a == "off":
        disableadservers("off")
        print("Ok.")
win = Tk()
win.geometry("350x100")
win.title("Spotify adblocker")
button1= ttk.Button(win, text= "On", command=disableadservers("on"))
button1.pack(side= TOP)
button2= ttk.Button(win, text= "Off", command=disableadservers("off"))
button2.pack(side=TOP)
win.mainloop()