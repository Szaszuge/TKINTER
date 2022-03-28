from tkinter import *
import math


def szamitas ():
    r = int(sugarbe.get())
    m = int(magssagbe.get())

    terfogat = round (math.pi * r * r * m, 2)
    terfogatki.delete (0, END)
    terfogatki.insert (0, str(terfogat)+' cm3' )

    vashenger = round (7.874 * terfogat, 2)
    vashengerki.delete (0, END)
    vashengerki.insert (0, str(vashenger)+' g' )

    fahenger = round (0.65 * terfogat, 2)
    fahengerki.delete (0, END)
    fahengerki.insert (0, str(fahenger)+' g' )


foablak = Tk()
gyoker = 'D:\\IKT\\tkinter\\'


icon = PhotoImage(file='png.png')
foablak.iconphoto(True, icon)


foablak.title('Henger')


sugarm = Label(foablak, text='Sugár (cm):')
sugarm.grid (column=1, row=1)
sugarbe = Entry(foablak)
sugarbe.grid (column=2, row=1, columnspan=2)


magassagm = Label(foablak, text='Magasság (cm):')
magassagm.grid (column=1, row=2)
magssagbe = Entry(foablak)
magssagbe.grid (column=2, row=2, columnspan=2)


terfogatm = Label(foablak, text='Térfogat:')
terfogatm.grid (column=1, row=4)
terfogatki = Entry(foablak)
terfogatki.grid (column=2, row=4, columnspan=2)


vashengerm = Label(foablak, text='Vashenger:')
vashengerm.grid (column=1, row=5)
vashengerki = Entry(foablak)
vashengerki.grid (column=2, row=5, columnspan=2)


fahengerm = Label(foablak, text='Tölgyfa henger:')
fahengerm.grid (column=1, row=6)
fahengerki = Entry(foablak)
fahengerki.grid (column=2, row=6, columnspan=2)


szamitasg = Button(foablak, text='kiszámítás', command=szamitas)
szamitasg.grid (column= 3, row=3)


foablak.mainloop()