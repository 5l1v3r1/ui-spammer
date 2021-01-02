from tkinter import *
from tkinter import messagebox
from time import sleep as sleep
import time
import random
import pyautogui

start_time = time.time()

window = Tk()
window.geometry("350x100")
window.title("ZiksthemW - Spam Bot")

spamtext = StringVar()
spamtext1 = Label(window, text="Input message to spam!")
spamtext2 = Entry(window, textvariable=spamtext)

def spam():
        question = messagebox.askyesno("Attention!","Spam will be started in 1 second.\nDo you still wanna continue?")
        if question == True:
            print("User pressed 'Yes'.")
            number = messagebox.askyesno("Question", "Do you want to add numbers to avoid spam protections?\nExample: 123text")
            if number == True:
                while True:
                    sleep(1)
                    pyautogui.typewrite(str(random.randint(1, 600)) + str(spamtext.get()))
                    pyautogui.press('enter')
            else:
                while True:
                    sleep(1)
                    pyautogui.typewrite(str(spamtext.get()))
                    pyautogui.press('enter')
        else:
            print("User pressed 'No'.")

spambutton = Button(window, text="Click Me!", command=lambda: spam())
programclose = Button(window, text="Close Program!", command=lambda: exit())

print("It took", time.time() - start_time, "seconds to run the code.")
spamtext1.pack()
spamtext2.pack()
spambutton.pack()
programclose.pack()
window.resizable(False, False)
window.mainloop()
