from tkinter import *
import math

def kiszamitas ():
    if len(sugarbe.get()) == 0 or len(magssagbe.get()) == 0 or len(borbe.get()) == 0 or type(sugarbe.get()) != int or type(borbe.get()) != int:
        megbeleki.delete (0, END)
        megbeleki.insert (0, 'Felesleges számítás' )
        telitetsegki.delete (0,END)
        telitetsegki.insert (0, 'Felesleges számítás' )
        terfogatki.delete (0,END)
        terfogatki.insert (0, 'Felesleges számítás' )

    r = int(sugarbe.get())
    m = int(magssagbe.get())
    borl = int(borbe.get())
    meg = 0
    telitet = 0

    if borl <= 0 or r <= 0 or m <= 0:
        megbeleki.delete (0, END)
        megbeleki.insert (0, 'Felesleges számítás' )
        telitetsegki.delete (0,END)
        telitetsegki.insert (0, 'Felesleges számítás' )
        terfogatki.delete (0,END)
        terfogatki.insert (0, 'Felesleges számítás' )
    else:

        terfogat = round (math.pi * r * r * m * 0.001)
        terfogatki.delete (0, END)
        terfogatki.insert (0, str(terfogat)+' l' )

        meg = terfogat - borl
        telitet = round (borl * (100 / terfogat))

        if borl > terfogat:
            megbeleki.delete (0, END)
            megbeleki.insert (0, 'Túl kicsi a hordó.' )
            telitetsegki.delete (0,END)
            telitetsegki.insert (0, 'Túl kicsi a hordó.' )
        else:
            megbeleki.delete (0, END)
            megbeleki.insert (0, str(meg)+' l')
            telitetsegki.delete (0, END)
            telitetsegki.insert (0, str(telitet)+' %')


foablak = Tk()
gyoker = 'D:\\Asztal\\Programming Stuff\\github\\TKINTER\\'

icon = PhotoImage(file='henger.png')
foablak.iconphoto(True, icon)

foablak.title('Hengerfolyadék')

bor = Label(foablak, text='Bor (l):')
bor.grid (column=1, row=1)
borbe = Entry(foablak, width=35)
borbe.grid (column=2, row=1, columnspan=2)

sugarm = Label(foablak, text='Sugár (cm):')
sugarm.grid (column=1, row=2)
sugarbe = Entry(foablak, width=35)
sugarbe.grid (column=2, row=2, columnspan=2)

magassagm = Label(foablak, text='Magasság (cm):')
magassagm.grid (column=1, row=3)
magssagbe = Entry(foablak, width=35)
magssagbe.grid (column=2, row=3, columnspan=2)


terfogatm = Label(foablak, text='Bor mennyisége(l):')
terfogatm.grid (column=1, row=5)
terfogatki = Entry(foablak, width=35)
terfogatki.grid (column=2, row=5, columnspan=2)

megbelem = Label(foablak, text='Hordó magassága(dm):')
megbelem.grid (column=1, row=6)
megbeleki = Entry(foablak, width=35)
megbeleki.grid (column=2, row=6, columnspan=2)

telitetsegm = Label(foablak, text='Bor benne(%):')
telitetsegm.grid (column=1, row=7)
telitetsegki = Entry(foablak, width=35)
telitetsegki.grid (column=2, row=7, columnspan=2)



kiszamitasg = Button(foablak, text='Számtás', command=kiszamitas)
kiszamitasg.grid (column= 3, row=4)

foablak.mainloop()

#bekérjük azt h mennyi bort szeretnénk tárolni és bekérjük a hordónak a sugarát magasságát a hordó sugarából magasságából kiszámoljuk a térfogatát azt kiírjuk megállapítjuk h belefér-e a megadott literszámból a hordóba és alatta kiírjuk százalékba h mennyi liter a hordó