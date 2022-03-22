from tkinter import *
import math

def szamitas ():
    r = int(sugarbe.get())
    m = int(magassagbe.get())
    terfogat = math.pi * r * r * m
    terfogatki.delete (0, END)
    terfogatki.insert (0, str(terfogat)+' cm3' )

foablak = Tk()
gyoker = 'D:\\IKT\\TKINTER\\'

sugar = Label(foablak, text='Sugár (cm):')
sugar.grid (column=1, row=1)
sugarbe = Entry(foablak)
sugarbe.grid (column=2, row=1, columnspan=2)

magassag = Label(foablak, text='Magasság (cm):')
magassag.grid (column=1, row=2)
magassagbe = Entry(foablak)
magassagbe.grid (column=2, row=2, columnspan=2)

terfogat = Label(foablak, text='Térfogat:')
terfogat.grid (column=1, row=4)
terfogatki = Entry(foablak)
terfogatki.grid (column=2, row=4, columnspan=2)

vashenger = Label(foablak, text='Vashenger:')
vashenger.grid (column=1, row=5)
vashengerki = Entry(foablak)
vashengerki.grid (column=2, row=5, columnspan=2)

fahenger = Label(foablak, text='Fahenger:')
fahenger.grid (column=1, row=6)
fahengerki = Entry(foablak)
fahengerki.grid (column=2, row=6, columnspan=2)

szamitasg = Button(foablak, text='Kiszámít', command=szamitas)
szamitasg.grid (column= 3, row=3)


foablak.mainloop()