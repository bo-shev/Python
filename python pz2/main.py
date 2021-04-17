from tkinter import *
from tkinter import messagebox




birth = " "
home = " "

def infoCut(event):
    birth= str(int(scalevar.get()))
    home=enthome.get()
    surname = entsurname2.get()
    name = entname2.get()
    fathername = entfathername2.get()
    print("Вивід ПІБ, року народження та місця проживання: ")
    tx.insert(1.0, surname + " " + name[0:1] + "." + fathername[0:1] + " " + birth + ", " + home + "\n")


def Say(event):
    pib = [];
    print("Вітаю, введіть наступну інформацію");

    if checksurname.get() == 1:
        pib.append(entsurname.get());
    else:
        pib.append("");
    if checkname.get() == 1:
        pib.append(entname.get());
    else:
        pib.append("");
    #print(checksurname.get()) ;
    if checkfathername.get() == 1:
        pib.append(entfathername.get());
    else:
        pib.append("");
    tx.insert(1.0, ""+pib[0] + " " + pib[1] + " " + pib[2]+ "\n");

    return  pib;

def clear(event):
    tx.delete(1.0, END)


def f(event):
    if var.get() == 0:
        fra['bg'] = 'red'
        changeColorBut['fg'] = 'red'
    elif var.get() == 1:
        fra['bg'] = 'green'
        changeColorBut['fg'] = 'green'
    elif var.get() == 2:
        fra['bg'] = 'blue'
        changeColorBut['fg'] = 'blue'

def textForNewWind():
    pib=Say("null");
    return ""+pib[0] + " " + pib[1] + " " + pib[2]+ "\n";

def onNew(event):
    win = Toplevel(root, relief=SUNKEN, bd=10, bg="lightblue")
    win.title("Дочернее окно")
    win.minsize(width=400, height=200)
    tx2 = Text(win, width=30, heigh=10, font='14')
    tx2.insert(1.0, textForNewWind());
    tx2.pack()


root = Tk()
fra = Frame(root, width=200, heigh=50, bg="green")
fra.grid()

surname = Label(text="Прізвище", padx=15, pady=10)
name = Label(text="Ім`я", padx=15, pady=10)
fathername = Label(text="По батькові", padx=15, pady=10)

surname.grid(row=2,column=2)
name.grid(row=3,column=2)
fathername.grid(row=4,column=2)



entsurname = Entry(root, width=20, bd=3)
entname = Entry(root, width=20, bd=3)
entfathername = Entry(root, width=20, bd=3)

entsurname.grid(row=2,column=3)
entname.grid(row=3,column=3)
entfathername.grid(row=4,column=3)

checksurname = IntVar()
surname_checkbutton = Checkbutton(text="Прізвище", variable=checksurname,
                                 onvalue=1, offvalue=0, padx=15, pady=10)
surname_checkbutton.grid(row=2, column=4)

checkname = IntVar()
name_checkbutton = Checkbutton(text="Ім`я", variable=checkname,
                                     onvalue=1, offvalue=0, padx=15, pady=10)
name_checkbutton.grid(row=3, column=4)

checkfathername = IntVar()
fathername_checkbutton = Checkbutton(text="По батькові", variable=checkfathername,
                                     onvalue=1, offvalue=0, padx=15, pady=10)
fathername_checkbutton.grid(row=4, column=4)

saybut = Button(root)
saybut["text"] = "Say!"
saybut.bind("<Button-1>", Say)
saybut.grid(row=5,column=3)

scale = Label(text="Рік народження", padx=15, pady=10)

scale.grid(row=0,column=5)


scalevar = DoubleVar()
scale = Scale( root, orient=HORIZONTAL,from_=1900, to =2025,variable = scalevar )
scale.grid(row=0,column=6)

home = Label(text="Місце проживання", padx=15, pady=10)

home.grid(row=1,column=5)

enthome = Entry(root, width=20, bd=3)

enthome.grid(row=1,column=6)

surname2 = Label(text="Прізвище", padx=15, pady=10)
name2 = Label(text="Ім`я", padx=15, pady=10)
fathername2 = Label(text="По батькові", padx=15, pady=10)

surname2.grid(row=2,column=5)
name2.grid(row=3,column=5)
fathername2.grid(row=4,column=5)



entsurname2 = Entry(root, width=20, bd=3)
entname2 = Entry(root, width=20, bd=3)
entfathername2 = Entry(root, width=20, bd=3)

entsurname2.grid(row=2,column=6)
entname2.grid(row=3,column=6)
entfathername2.grid(row=4,column=6)

cutInfBut = Button(root)
cutInfBut["text"] = "InfoCut!"
cutInfBut.bind("<Button-1>", infoCut)
cutInfBut.grid(row=5,column=5)

var = IntVar()
var.set(0)
red = Radiobutton(text="Red",
                  variable=var, value=0)
green = Radiobutton(text="Green",
                    variable=var, value=1)
blue = Radiobutton(text="Blue",
                   variable=var, value=2)
changeColorBut = Button(root)
changeColorBut["text"] = "ChangeColor!"
changeColorBut.bind("<Button-1>", f)

red.grid(row=1,column=2)
green.grid(row=1,column=3)
blue.grid(row=1,column=4)
changeColorBut.grid(row=0,column=3)

message = StringVar()
tx = Text(root,width=30, heigh= 5, font ='14')
scr = Scrollbar(root, command=tx.yview)
tx.configure(yscrollcommand=scr.set)




but = Button(root)
but["text"] = "Hello!"
but.bind("<Button-1>", f)
but.grid(row=0,column=0)

tx.grid(row=5,column=0)
scr.grid(row=5,column=1)

delbut = Button(root)
delbut["text"] = "Очистити поле виводу"
delbut.bind("<Button-1>", clear)
delbut.grid(row=5,column=2)

newWindbut = Button(root)
newWindbut["text"] = "Нове віконце"
newWindbut.bind("<Button-1>", onNew)
newWindbut.grid(row=2,column=0)



root.mainloop()
