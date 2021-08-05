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
    os.system("pip3 install tkinter")
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
def disableadservers():


    getadservers = requests.get("https://tinocoppens.github.io/hostslist/index.html").text

    importtohosts = open("C:/Windows/System32/drivers/etc/hosts", "w")
    importtohosts.write(getadservers)
    importtohosts.close
def stop():
    importtohosts = open("C:/Windows/System32/drivers/etc/hosts", "w")
    importtohosts.write("")
    importtohosts.close

win = Tk()
win.geometry("350x100")
win.title("Spotify adblocker")
ttk.Button(win, text="On", command= disableadservers).pack(side=TOP)
ttk.Button(win, text="Off", command= stop).pack(side=TOP)
win.mainloop()
