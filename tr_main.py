from tkinter import *
from tkinter import messagebox
from time import sleep as uyku
import time
import random
import pyautogui

start_time = time.time()

pencere = Tk()
pencere.geometry("350x100")
pencere.title("ZiksthemW - Spam Bot")

spamyazisi = StringVar()
spamyazi1 = Label(pencere, text="Spamlanacak Mesaj Buraya!")
spamyazi2 = Entry(pencere, textvariable=spamyazisi)

def spam():
        soru = messagebox.askyesno("Uyarı!","Spam 1 saniye içinde başlayacaktır.\nDevam etmek istiyor musunuz?")
        if soru == True:
            print("Kullanıcı 'Evet'e bastı.")
            sayi = messagebox.askyesno("Soru", "Spam korumalarını geçmek için yazınızın başına sayı eklemek ister misiniz?\nÖrnek: 123yazi")
            if sayi == True:
                while True:
                    uyku(1)
                    pyautogui.typewrite(str(random.randint(1, 600)) + str(spamyazisi.get()))
                    pyautogui.press('enter')
            else:
                while True:
                    uyku(1)
                    pyautogui.typewrite(str(spamyazisi.get()))
                    pyautogui.press('enter')
        else:
            print("Kullanıcı 'Hayır'a bastı.")

spambuton = Button(pencere, text="Bana tıkla!", command=lambda: spam())
programkapa = Button(pencere, text="Programı Kapat!", command=lambda: exit())

print("Programın çalışması", time.time() - start_time, "saniye sürdü.")
spamyazi1.pack()
spamyazi2.pack()
spambuton.pack()
programkapa.pack()
pencere.resizable(False, False)
pencere.mainloop()
