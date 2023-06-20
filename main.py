
from tkinter import *
from tkinter import ttk
import time
import random
from threading import Timer
from random import randint
import tkinter as tk
import pickle
import glob
import os
from PIL import Image, ImageTk
window = tk.Tk()
window.title('Overgrown 0.0.1 prealpha (internal use only)')
window.geometry("1920x1080")
window['bg']='#262626'
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=2)
window.rowconfigure(1, weight=1)
title = """
 ____   _  .   _____  ____   _____  ____   ____   _    .  _    . 
/  _ \ / \ |\ /  __/ /  __\ /  __/ /  __\ /  _ \ / \  /| / \  /|
| / \| | | // |  \   |  \/| | |  _ |  \/| | / \| | |  || | |\ ||
| \_/| | \//  |  /_  |    / | |_// |    / | \_/| | |/\|| | | \||
\____/ \__/   \____\ \_/\_\ \____\ \_/\_\ \____/ \_/  \| \_/  \|
                                                       
"""

greeting = tk.Label(
    text=title,
    background="#262626", 
    foreground="#FFFFFF",
    font=("Courier", 15)
)
greeting.pack()

saves = glob.glob("*.dat")
print(saves)

roomids = {
    1 : "page2",
    2 : "page3",
    3 : "page4",
    4 : "page5",
    5 : "encounter",
    6 : "boss",
    7 : "chest"
}

def buttoneq():
    buttoneq = tk.Button(
        text="Ekwipunek",
        width=15,
        height=5,
        background="#545454",
        foreground="#FFFFFF",
        command=equipment,
        font=("Courier", 15)
    )
    buttoneq.place(rely=0.5,relx=0,anchor="w")
    return buttoneq

def waithere():
    print("waiting...")

def next():
    buttonstart.pack_forget()
    buttoncontinue.pack_forget()
    buttonexit.pack_forget()
    greeting.pack_forget()
    intro()

def exit():
    print("Żegnaj bohaterze")
    window.destroy()


def next2():
    buttonstart.pack_forget()
    buttoncontinue.pack_forget()
    buttonexit.pack_forget()
    greeting.pack_forget()
    save = open(saves[0], "rb")
    char = pickle.load(save)
    print(char)
    savedroom = char["room"]
    command = roomids[savedroom] + "()"
    print(command)
    exec(command)
    save.close()

class imgloading():
    def __init__(self, name, masterw=window):
        self.imgname = ("png/"+name+".png")
        print(self.imgname)
        self.imgload = Image.open(self.imgname)
        self.imgrender = ImageTk.PhotoImage(self.imgload)
        self.img = Label(master=masterw,image=self.imgrender)
        self.img.image = self.imgrender
    
    def place(self):
        self.img.place(relx=0.5,rely=0.03, anchor="n")
    def forget(self):
        self.img.place_forget()

def imgloader(name, masterw=window):
    imgname = ("png/"+name+".png")
    print(imgname)
    imgload = Image.open(imgname)
    imgrender = ImageTk.PhotoImage(imgload)
    img = Label(master=masterw,image=imgrender)
    img.image = imgrender
    img.place(relx=0.5,rely=0.03, anchor="n")
    return img

buttonstart = tk.Button(
    text="""
Rozpocznij 
nową grę
    """,
    justify="center",
    width=15,
    height=5,
    background="#545454",
    foreground="#FFFFFF",
    command=next,
    font=("Courier", 20)
    
)

buttoncontinue = tk.Button(
    text="Kontynuuj",
    width=15,
    height=5,
    background="#545454",
    foreground="#FFFFFF",
    command=next2,
    font=("Courier", 20)
    
)
buttonexit = tk.Button(
    window,
    text="Wyjdź",
    width=15,
    height=5,
    background="#545454",
    foreground="#FFFFFF",
    command=exit,
    font=("Courier", 20)
)

if len(saves) == 0:
    buttonstart.pack(pady="5")
else:
    buttoncontinue.pack(pady="5")

buttonexit.pack(pady="5")

def intro():
    canvas = tk.Canvas(window,
                    bg="#262626",
                    height=300,
                    width=500,
                    
                    )
    canvas.place(relx=0.5, rely=0.5, anchor="center")

    def next():
        char = {    
            "name" : entry1.get(),
            "hp" : 100,
            "room" : 1,
            "weap" : "Basic sword",
            "shield" : "Basic shield",
            "eq" : ["Basic sword", 10, "Basic shield", 10]
        }
        savename = entry1.get() + ".dat"
        save = open(savename, "wb")
        pickle.dump(char, save)
        save.close()
        buttonstart.pack_forget()
        buttonexit.pack_forget()
        greeting.pack_forget()
        canvas.place_forget()
        canvas1.pack_forget()
        imgloader("intro").place_forget()
        page2()
    text1 = canvas.create_text(10, 10, text='', anchor=tk.NW, font="Courier", justify="left", fill="#FFFFFF")
    imgloader("intro")

    opis = """
    WITAJ PRZYBYSZU
    JAK SIĘ NAZYWASZ?
    """
    delta = 100
    delay = 0
    for i in range(len(opis) + 1):
        s = opis[:i]
        update_text = lambda s=s: canvas.itemconfigure(text1, text=s)
        canvas.after(delay, update_text)
        delay += delta

    buttonstart = tk.Button(
        text="To jest moje imie",
        width=15,
        height=5,
        background="#545454",
        foreground="#FFFFFF",
        command=next,
        font=("Courier", 15)
    )
    buttonstart.pack(fill='none', side="bottom") 
    canvas1 = tk.Canvas(window, width=350, height=100, )
    canvas1.pack(side="bottom", pady=40)
    entry1 = tk.Entry(window, bg="#262626", font=("Courier", 20), borderwidth=5, fg="#FFFFFF", justify=CENTER, highlightthickness=0, text="Name") 
    canvas1.create_window(175, 50, window=entry1, height=100, width=350)

def page2():
    img = imgloading("page2")
    img.place()
    canvas = tk.Canvas(window,
                    bg="#262626",
                    height=300,
                    width=500,
                    
                    )
    canvas.place(relx=0.5, rely=0.6, anchor="center")
    buttoneq()
    def next():
        buttonstart.pack_forget()
        buttonexit.pack_forget()
        greeting.pack_forget()
        canvas.place_forget()
        saves = glob.glob("*.dat")
        save = open(saves[0], "rb")
        char = pickle.load(save)
        print(char)
        char["room"] = 2
        print(char)
        save.close()
        save = open(saves[0], "wb")
        save = pickle.dump(char, save)
        img = imgloading("page3")
        img.forget()
        page3()


    text1 = canvas.create_text(10, 10, text='', anchor=tk.NW, font="Courier", justify="left", fill="#FFFFFF")

    opis = """
    Budzisz się w miejscu którego nigdy 
    nie widziałeś.
    Ściany są pełne pęknięć.
    Oprócz tego jedyne co widzisz to drzwi 
    oznaczone dziwnym symbolem.
    """
    delta = 75
    delay = 0
    for i in range(len(opis) + 1):
        s = opis[:i]
        update_text = lambda s=s: canvas.itemconfigure(text1, text=s)
        canvas.after(delay, update_text)
        delay += delta

    buttonstart = tk.Button(
        text="Przejdź przez drzwi",
        width=15,
        height=5,
        background="#545454",
        foreground="#FFFFFF",
        command=next,
        font=("Courier", 15)
    )
    buttonstart.pack(fill='none', side="bottom")
    

def equipment():
    windoweq = tk.Toplevel()
    windoweq.title('Ekwipunek')
    windoweq.geometry("1280x720")
    windoweq['bg']='#262626'
    windoweq.columnconfigure(0, weight=1)
    windoweq.columnconfigure(1, weight=2)
    windoweq.rowconfigure(1, weight=1)
    title = """
    Ekwipunek
    """
    greeting = tk.Label(
        master=windoweq,
        text=title,
        background="#262626", 
        foreground="#FFFFFF",
        font=("Courier", 15))
    greeting.pack()

    imgloader("eq", windoweq)
    saves = glob.glob("*.dat")
    print(saves)
    save = open(saves[0], "rb")
    char = pickle.load(save)
    eq = char["eq"]
    hp = str(char["hp"])
    name = char["name"]
    print(eq)
    # frame = tk.Frame(
    #     master=windoweq,
    #     background='#262626',

    # )
    # frame.pack()
    # table = ttk.Treeview(frame)

    # table['columns'] = ('nazwa', 'dmg')

    # table.column("#0",width=0,  stretch=NO)
    # table.column("nazwa",anchor=CENTER, width=80)
    # table.column("dmg",anchor=CENTER,width=80)

    # table.heading("#0",text="",anchor=CENTER)
    # table.heading("nazwa",text="",anchor=CENTER)
    # table.heading("dmg",text="",anchor=CENTER)

    # itemid = 0
    # for item in eq:
    #     table.insert(parent='',index='end',iid=itemid,text='', values=item)
    #     itemid = itemid + 1

    # table.pack()

    def back():
        windoweq.destroy()

    buttonstart = tk.Button(
        master=windoweq,
        text="Go back",
        width=15,
        height=5,
        background="#545454",
        foreground="#FFFFFF",
        command=back,
        font=("Courier", 15)
    )
    buttonstart.pack(fill='none', side="bottom")
    infotxt = "Imie: "+name+"\nPunkty życia: "+hp+"\nMiecz: "+str(eq[0])+"\nAtak: "+str(eq[1])+"\nTarcza: "+str(eq[2])+"\nObrona: "+str(eq[3])
    info = tk.Label(master=windoweq,
        text=infotxt,
        background="#262626", 
        foreground="#FFFFFF",
        font=("Courier", 15))
    info.pack(side='bottom')
    
    print(eq)
    save.close()
    windoweq.mainloop()


def page3():
    buttoneq()
    img = imgloading("page3")
    img.place()


    canvas = tk.Canvas(window,
                    bg="#262626",
                    height=300,
                    width=600,
                    
                    )
    canvas.place(relx=0.5, rely=0.7,anchor="center")

    def left():
        buttonleft.grid_forget()
        buttonright.grid_forget()
        canvas.place_forget()
        img.forget()
        saves = glob.glob("*.dat")
        save = open(saves[0], "rb")
        char = pickle.load(save)
        print(char)
        char["room"] = 5
        print(char)
        save.close()
        save = open(saves[0], "wb")
        save = pickle.dump(char, save)
        encounter()


    def right():
        buttonleft.grid_forget()
        buttonright.grid_forget()
        canvas.place_forget()
        img.forget()
        chest()

    text1 = canvas.create_text(10, 10, text='', anchor=tk.NW, font="Courier", justify="left", fill="#FFFFFF")

    opis = """
    Dotarłeś do korytarza który ma dwoje drzwi.
    Które wybierzesz?
    """
    delta = 100
    delay = 0
    for i in range(len(opis) + 1):
        s = opis[:i]
        update_text = lambda s=s: canvas.itemconfigure(text1, text=s)
        canvas.after(delay, update_text)
        delay += delta

    buttonleft = tk.Button(
        text="Idź w lewo",
        width=15,
        height=5,
        background="#545454",
        foreground="#FFFFFF",
        command=left,
        font=("Courier", 20)
    )
    buttonleft.grid(column=0, row=3, sticky='w')
    
    buttonright = tk.Button(
        text="Idź w prawo",
        width=15,
        height=5,
        background="#545454",
        foreground="#FFFFFF",
        command=right,
        font=("Courier", 20)
    )
    buttonright.grid(column=2, row=3, stick='e')

def chest():
    buttoneq()
    img = imgloading("chest")
    img.place()


    canvas = tk.Canvas(window,
                    bg="#262626",
                    height=300,
                    width=600,
                    
                    )
    canvas.place(relx=0.5, rely=0.7,anchor="center")

    def left():
        # buttonleft.grid_forget()
        # buttonright.grid_forget()
        # canvas.place_forget()
        # img.forget()
        otworz()


    def right():
        buttonleft.grid_forget()
        buttonright.grid_forget()
        canvas.place_forget()
        img.forget()
        saves = glob.glob("*.dat")
        save = open(saves[0], "rb")
        char = pickle.load(save)
        print(char)
        char["room"] = 5
        print(char)
        save.close()
        save = open(saves[0], "wb")
        save = pickle.dump(char, save)
        buttonleft.grid_forget()
        buttonright.grid_forget()
        canvas.place_forget()
        img.forget()
        encounter()

    text1 = canvas.create_text(10, 10, text='', anchor=tk.NW, font="Courier", justify="left", fill="#FFFFFF")

    opis = """
    Przed tobą stoi duża skrzynia?
    Otworzysz?
    """
    delta = 100
    delay = 0
    for i in range(len(opis) + 1):
        s = opis[:i]
        update_text = lambda s=s: canvas.itemconfigure(text1, text=s)
        canvas.after(delay, update_text)
        delay += delta

    item = ["Zdobiony miecz" , "15"]

    def otworz():
        saves = glob.glob("*.dat")
        save = open(saves[0], "rb")
        char = pickle.load(save)
        print(char)    
        opis = str(" Przedmiot: "+item[0]+" Obrażenia: "+item[1])
        print(opis)
        delta = 100
        delay = 0
        for i in range(len(opis) + 1):
            s = opis[:i]
            update_text = lambda s=s: canvas.itemconfigure(text1, text=s)
            canvas.after(delay, update_text)
            delay += delta
        eq = char["eq"]
        eq[0] = item[0]
        eq[1] = item[1]
        char["room"] = 5
        print(char)
        save.close()
        save = open(saves[0], "wb")
        save = pickle.dump(char, save)
        buttonleft.grid_forget()
        buttonright.grid_forget()
        canvas.place_forget()
        img.forget()
        encounter()



    buttonleft = tk.Button(
        text="Otwórz",
        width=15,
        height=5,
        background="#545454",
        foreground="#FFFFFF",
        command=left,
        font=("Courier", 20)
    )
    buttonleft.grid(column=0, row=3, sticky='w')
    
    buttonright = tk.Button(
        text="Zawróć",
        width=15,
        height=5,
        background="#545454",
        foreground="#FFFFFF",
        command=right,
        font=("Courier", 20)
    )
    buttonright.grid(column=2, row=3, stick='e')
              
def encounter():
    buttoneq()
    img = imgloading("truchlo")
    img.place()
    window.title('go further')
    enemysel = ["truchło",
         "30",
         "5",
         "10"]
    print(enemysel)
    saves = glob.glob("*.dat")
    print(saves)
    save = open(saves[0], "rb")
    char = pickle.load(save)
    print(char)
    eq = char["eq"]
    encounterdata = Encounter(char["name"], char["hp"], eq[1], eq[3], enemysel[0], enemysel[1], enemysel[2], enemysel[3],)
    
    canvas = tk.Canvas(window,
                    bg="#262626",
                    height=300,
                    width=600,
                    
                    )
    canvas.place(relx=0.5, rely=0.7,anchor="center")

    def atak():
        print("atak")
        hp = encounterdata.attackenemydef()
        delta = 30
        delay = 0
        opis = str(f"Zaatakowałeś przeciwnika za: {hp[0]}\nPrzeciwnik zaatakował za: {hp[1]}\nTwoje życie: {hp[2]}\nŻycie przeciwnika: {hp[3]}")
        for i in range(len(opis) + 1):
            s = opis[:i]
            update_text = lambda s=s: canvas.itemconfigure(text1, text=s)
            canvas.after(delay, update_text)
            delay += delta
        saves = glob.glob("*.dat")
        save = open(saves[0], "rb")
        char = pickle.load(save)
        print(char)
        char["hp"] = hp[2]
        print(char)
        save = open(saves[0], "wb")
        save = pickle.dump(char, save)


    def obrona():
        encounterdata.attackherodef()

    text1 = canvas.create_text(10, 10, text='', anchor=tk.NW, font="Courier", justify="left", fill="#FFFFFF")



    opis = "Przed tobą stoi: "+enemysel[0]
    delta = 100
    delay = 0
    for i in range(len(opis) + 1):
        s = opis[:i]
        update_text = lambda s=s: canvas.itemconfigure(text1, text=s)
        canvas.after(delay, update_text)
        delay += delta

    buttonleft = tk.Button(
        text="Atakuj",
        width=15,
        height=5,
        background="#545454",
        foreground="#FFFFFF",
        command=atak,
        font=("Courier", 20)
    )
    buttonleft.place(relx=0.5, rely=1,anchor="s")
    save.close()

class Encounter(object):

    def __init__(self, namehero, hphero, attackhero, defencehero, nameenemy, hpenemy, attackenemy, defenceenemy, bosscheck=0):
        self.namehero = namehero
        self.hphero = int(hphero)
        self.attackhero = int(attackhero)
        self.defencehero = int(defencehero)
        self.nameenemy = nameenemy
        self.hpenemy = int(hpenemy)
        self.attackenemy = int(attackenemy)
        self.defenceenemy = int(defenceenemy)
        self.bosscheck = int(bosscheck)
        print(bosscheck)
    
    def name(self):
        return self.namehero, self.nameenemy
    
    def attackenemydef(self):
        attack = int(randint(1,3) * ((self.attackhero / 1.5) / (self.defenceenemy / 5)))
        defend = int(randint(1,3) * self.attackenemy / (self.defencehero / 5))
        print("attackenemy with", attack)
        self.hpenemy = self.hpenemy - attack
        self.hphero = self.hphero - defend
        if self.hpenemy <= 0 and self.bosscheck == 0:
            for widget in window.winfo_children():
                widget.destroy()
            saves = glob.glob("*.dat")
            save = open(saves[0], "rb")
            char = pickle.load(save)
            print(char)
            char["room"] = 3
            print(char)
            save.close()
            save = open(saves[0], "wb")
            save = pickle.dump(char, save)
            page4()
        elif self.hpenemy <= 0 and self.bosscheck == 1:
            for widget in window.winfo_children():
                widget.destroy()
            saves = glob.glob("*.dat")
            print(saves)
            os.remove(saves[0])
            window.destroy()
            print("Udało się!\nPokonałem go!\nAle nic to nie dało.\nWszystko znikneło.\nJest tak ciemno.")
        elif self.hphero <= 0:
            saves = glob.glob("*.dat")
            print(saves)
            os.remove(saves[0])
            print("NIE ŻYJESZ")
            window.destroy()
        print("enemy heath", self.hpenemy)  
        print("hero heath", self.hphero)
        return attack, defend, self.hphero, self.hpenemy

def page4():
    buttoneq()
    img = imgloading("page4")
    img.place()
    canvas = tk.Canvas(window,
                    bg="#262626",
                    height=300,
                    width=600,
                    
                    )
    canvas.place(relx=0.5, rely=0.6, anchor="center")

    text1 = canvas.create_text(10, 10, text='', anchor=tk.NW, font="Courier", justify="left", fill="#FFFFFF",tag="original")

    opis = """
    Przed tobą stoi stary ekran podłączony do klawiatury.
    Za nim jest tekst:
    "mEanwHile i lIve between the lineS"
    Komputer oczekuje odpowiedzi.
    """
    delta = 75
    delay = 0
    for i in range(len(opis) + 1):
        s = opis[:i]
        update_text = lambda s=s: canvas.itemconfigure(text1, text=s)
        canvas.after(delay, update_text)
        delay += delta

    canvas1 = tk.Canvas(window, width=350, height=100, )
    canvas1.place(relx=0.5, rely=0.85, anchor="s")
    entry1 = tk.Entry(window, bg="#262626", font=("Courier", 20), borderwidth=5, fg="#FFFFFF", justify=CENTER, highlightthickness=0, text="Password",) 
    canvas1.create_window(175, 50, window=entry1, height=100, width=350)
    def check():
        entry = entry1.get()
        print(entry)
        if entry == "58919":
            delta = 50
            delay = 0
            opis = "Prawidłowa odpowiedź"
            for i in range(len(opis) + 1):
                s = opis[:i]
                update_text = lambda s=s: canvas.itemconfigure(text1, text=s)
                canvas.after(delay, update_text)
                delay += delta
            buttonleft.place_forget()
            canvas.place_forget()
            canvas1.place_forget()
            img.forget()
            saves = glob.glob("*.dat")
            save = open(saves[0], "rb")
            char = pickle.load(save)
            print(char)
            char["room"] = 4
            print(char)
            save.close()
            save = open(saves[0], "wb")
            save = pickle.dump(char, save)
            page5()
        else:
            opis = """
    Błąd: Zła odpowiedź
    Przed tobą stoi stary ekran podłączony do klawiatury.
    Za nim jest tekst:
    "mEanwHile i lIve between the lineS"
    Komputer ponownie oczekuje odpowiedzi.
            """
            delta = 100
            delay = 0
            for i in range(len(opis) + 1):
                s = opis[:i]
                update_text = lambda s=s: canvas.itemconfigure(text1, text=s)
                canvas.after(delay, update_text)
                delay += delta


    buttonleft = tk.Button(
        text="Check",
        width=15,
        height=4,
        background="#545454",
        foreground="#FFFFFF",
        command=check,
        font=("Courier", 20)
    )
    buttonleft.place(relx=0.5, rely=1, anchor="s")

def page5():
    buttoneq()
    img = imgloading("page5")
    img.place()
    canvas = tk.Canvas(window,
                    bg="#262626",
                    height=300,
                    width=600,
                    
                    )
    canvas.place(relx=0.5, rely=0.6, anchor="center")

    def left():
        buttonleft.place_forget()
        canvas.place_forget()
        img.forget()
        boss()


    text1 = canvas.create_text(10, 10, text='', anchor=tk.NW, font="Courier", justify="left", fill="#FFFFFF")

    opis = """
    Przed sobą widzisz ogromne drzwi
    Wejdziesz?
    """
    delta = 100
    delay = 0
    for i in range(len(opis) + 1):
        s = opis[:i]
        update_text = lambda s=s: canvas.itemconfigure(text1, text=s)
        canvas.after(delay, update_text)
        delay += delta

    buttonleft = tk.Button(
        text="Wejdź",
        width=15,
        height=5,
        background="#545454",
        foreground="#FFFFFF",
        command=left,
        font=("Courier", 20)
    )
    buttonleft.place(relx=0.5, rely=1, anchor="s")
    
bosslist = {
    1 : ["boss",
         "100",
         "5",
         "10"],
}

def boss():
    buttoneq()
    img = imgloading("boss")
    img.place()
    window.title('???')
    enemysel = ["???",
         "100",
         "5",
         "10"]
    print(enemysel)
    saves = glob.glob("*.dat")
    print(saves)
    save = open(saves[0], "rb")
    char = pickle.load(save)
    print(char)
    eq = char["eq"]
    encounterdata = Encounter(char["name"], char["hp"], eq[1], eq[3], enemysel[0], enemysel[1], enemysel[2], enemysel[3],1)
    
    canvas = tk.Canvas(window,
                    bg="#262626",
                    height=300,
                    width=600,
                    
                    )
    canvas.place(relx=0.5, rely=0.7,anchor="center")

    def atak():
        print("atak")
        hp = encounterdata.attackenemydef()
        delta = 30
        delay = 0
        opis = str(f"Zaatakowałeś przeciwnika za: {hp[0]}\nPrzeciwnik zaatakował za: {hp[1]}\nTwoje życie: {hp[2]}\nŻycie przeciwnika: {hp[3]}")
        for i in range(len(opis) + 1):
            s = opis[:i]
            update_text = lambda s=s: canvas.itemconfigure(text1, text=s)
            canvas.after(delay, update_text)
            delay += delta
        saves = glob.glob("*.dat")
        # save = open(saves[0], "rb")
        # char = pickle.load(save)
        # print(char)
        # char["hp"] = hp[2]
        # print(char)
        # save = open(saves[0], "wb")
        # save = pickle.dump(char, save)


    def obrona():
        encounterdata.attackherodef()

    text1 = canvas.create_text(10, 10, text='', anchor=tk.NW, font="Courier", justify="left", fill="#FFFFFF")



    opis = "Przed tobą stoi: "+enemysel[0]
    delta = 100
    delay = 0
    for i in range(len(opis) + 1):
        s = opis[:i]
        update_text = lambda s=s: canvas.itemconfigure(text1, text=s)
        canvas.after(delay, update_text)
        delay += delta

    buttonleft = tk.Button(
        text="Atakuj",
        width=15,
        height=5,
        background="#545454",
        foreground="#FFFFFF",
        command=atak,
        font=("Courier", 20)
    )
    buttonleft.grid(column=0, row=3, sticky='w')
    
    buttonright = tk.Button(
        text="Broń",
        width=15,
        height=5,
        background="#545454",
        foreground="#FFFFFF",
        command=obrona,
        font=("Courier", 20)
    )
    buttonright.grid(column=2, row=3, stick='e')
    save.close()



window.mainloop()
