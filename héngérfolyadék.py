from tkinter import *
import math

foablak = Tk()
gyoker = 'D:\\IKT\\tkinter\\'


icon = PhotoImage(file= gyoker + 'henger.png')
foablak.iconphoto(True, icon)


foablak.title('Hengerfolyadék')

mennyiseg = Label(foablak, text= "Bor mennyisége(l):")
mennyiseg.grid(column = 1, row = 1)
mennyib = Entry(foablak)
mennyib.grid(column = 2, row = 1, columnspan = 2)

magassag = Label(foablak, text = "Hordó magassága(dm):")
magassag.grid(column = 1, row = 3)
magassagg = Entry(foablak)
magassagg.grid(column = 2, row = 3, columnspan = 2)

gomb1 = Button(foablak, text= "kiszámítás")
gomb1.grid(column = 3, row = 4)

foablak.mainloop()

#bekérjük azt h mennyi bort szeretnénk tárolni és bekérjük a hordónak a sugarát magasságát a hordó sugarából magasságából kiszámoljuk a térfogatát azt kiírjuk megállapítjuk h belefér-e a megadott literszámból a hordóba és alatta kiírjuk százalékba h mennyi liter a hordó