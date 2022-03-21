from tkinter import*

ablak1 = Tk()
gyoker = "D:\\IKT\\TKINTER\\"
ablak1.title = ("tk")
icon = PhotoImage(file = gyoker + 'png.png')
ablak1.iconphoto(True, icon)
ablak1.geometry('550x350')

mezo1 = Entry(ablak1)
mezo1.pack(side = LEFT)
mezo2 = Entry(ablak1)
mezo2.pack(side = LEFT)
mezo3 = Entry(ablak1)
mezo3.pack(side = LEFT)
mezo4 = Entry(ablak1)
mezo4.pack(side = LEFT)
ablak1.mainloop()