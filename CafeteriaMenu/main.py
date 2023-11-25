import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

menu = tk.Tk()

menu.title("Cafeteria Menu")
menu.geometry("400x630")
menu.resizable(width=False, height=True)
canv = tk.Canvas(bg='#a63f59', width=2000, height=3000)
canv.pack()

img = ImageTk.PhotoImage(file="veins.png")
breadim = ImageTk.PhotoImage(file='bread.png')

wsaim = Image.open('wsa.png')
wsaim = wsaim.resize((50, 50), Image.BICUBIC)
wsaim = ImageTk.PhotoImage(wsaim)

slices = Image.open('slices.png')
slices = slices.resize((200, 56), Image.LANCZOS)
slc = ImageTk.PhotoImage(slices)

yog1 = Image.open('608300-1-eng-GB_raspberry-yogurt-crunch-pots.jpg')
yog1 = yog1.resize((138, 138), Image.LANCZOS)
yog1 = ImageTk.PhotoImage(yog1)

water = Image.open('water.jpg')
water = water.resize((138, 138), Image.LANCZOS)
water = ImageTk.PhotoImage(water)

mangoim = Image.open('1735627_main.jpg')
mangoim = mangoim.resize((138, 138), Image.LANCZOS)
mangoim = ImageTk.PhotoImage(mangoim)

orangeim = Image.open('1735647_main.jpg')
orangeim = orangeim.resize((138, 138), Image.LANCZOS)
orangeim = ImageTk.PhotoImage(orangeim)

applej1 = Image.open('1735651_main.jpg')
applej1 = applej1.resize((138, 138), Image.LANCZOS)
applej1 = ImageTk.PhotoImage(applej1)

labanm = Image.open('1589030280Marmum_Laban_Cool_Bottle_-_200ml.jpg')
labanm = labanm.resize((138, 138), Image.LANCZOS)
labanm = ImageTk.PhotoImage(labanm)

maches = Image.open('1469254919210.jpeg')
maches = maches.resize((138, 138), Image.LANCZOS)
maches = ImageTk.PhotoImage(maches)

bmuffin = Image.open('Blueberry-Muffin-Slice-735x1102.jpg')
bmuffin = bmuffin.resize((138, 138), Image.LANCZOS)
bmuffin = ImageTk.PhotoImage(bmuffin)

chickencaesarwrapslices = Image.open('chicken-caesar-wraps-9.jpg')
chickencaesarwrapslices = chickencaesarwrapslices.resize((121, 120), Image.LANCZOS)
chickencaesarwrapslices = ImageTk.PhotoImage(chickencaesarwrapslices)

fruitsalad = Image.open('fruit-salad-ingredients-close-up-bowl.jpg')
fruitsalad = fruitsalad.resize((138, 138), Image.LANCZOS)
fruitsalad = ImageTk.PhotoImage(fruitsalad)

pizza = Image.open('IMG_2032-500x500.jpg')
pizza = pizza.resize((138, 138), Image.LANCZOS)
pizza = ImageTk.PhotoImage(pizza)

turkeycheesesandwich = Image.open('Market_Sandwich-Mega-SmokedTurkeyCheese-basic.jpg')
turkeycheesesandwich = turkeycheesesandwich.resize((138, 120), Image.LANCZOS)
turkeycheesesandwich = ImageTk.PhotoImage(turkeycheesesandwich)

paneerkadaiwrapslices = Image.open('paneer-kathi-rolls-1-1-850x1133.jpg')
paneerkadaiwrapslices = paneerkadaiwrapslices.resize((138, 138), Image.LANCZOS)
paneerkadaiwrapslices = ImageTk.PhotoImage(paneerkadaiwrapslices)

pennepastaslices = Image.open('penne-arrabiata-1.jpg')
pennepastaslices = pennepastaslices.resize((138, 138), Image.LANCZOS)
pennepastaslices = ImageTk.PhotoImage(pennepastaslices)

ches1 = Image.open('ches.png')
ches1 = ches1.resize((138, 120), Image.LANCZOS)
chesim = ImageTk.PhotoImage(ches1)

ap1 = Image.open('aple.png')
ap1 = ap1.resize((138, 138), Image.LANCZOS)
appleim = ImageTk.PhotoImage(ap1)

po1 = Image.open('pocorn.png')
po1 = po1.resize((138, 138), Image.LANCZOS)
popim = ImageTk.PhotoImage(po1)

line = Image.open('line.png')
line = line.resize((360, 2), Image.LANCZOS)
line = ImageTk.PhotoImage(line)

food = Image.open('food.png')
food = food.resize((250, 180), Image.LANCZOS)
food = ImageTk.PhotoImage(food)

beverage = Image.open('beverage.png')
beverage = beverage.resize((200, 200), Image.LANCZOS)
beverage = ImageTk.PhotoImage(beverage)

warmfood = Image.open('warmfood.png')
warmfood = warmfood.resize((190, 130), Image.LANCZOS)
warmfood = ImageTk.PhotoImage(warmfood)

freshfood = Image.open('freshfood.png')
freshfood = freshfood.resize((190, 130), Image.LANCZOS)
freshfood = ImageTk.PhotoImage(freshfood)

otherfood = Image.open('otherfood.png')
otherfood = otherfood.resize((190, 130), Image.LANCZOS)
otherfood = ImageTk.PhotoImage(otherfood)

info = Image.open('info.png')
info = info.resize((20, 20), Image.LANCZOS)
info = ImageTk.PhotoImage(info)

s = tk.Label(image=slc, bg='#a63f59')
s.place(anchor='nw', x=105, y=10)
wsalabel = tk.Label(menu, image=wsaim, bg='#a63f59')
wsalabel.place(anchor='nw', x=25, y=16)
line1 = tk.Label(menu, image=line, bg='#a63f59')
line1.place(anchor='nw', x=18, y=78)
line2 = tk.Label(menu, image=line, bg='#a63f59')
line2.place(anchor='nw', x=18, y=104)


def menu_screen1():

    def categoryf():
        foodscat.destroy()
        beveragecat.destroy()

        def warmf():
            home_button.destroy()
            wf.destroy()
            ff.destroy()
            of.destroy()

            def backwf():
                back_button.destroy()
                home_button1.destroy()
                warm_food.destroy()
                nextb.destroy()
                preb.destroy()
                f1.destroy()
                f2.destroy()
                f3.destroy()
                f4.destroy()
                f5.destroy()
                categoryf()

            def homewf():
                back_button.destroy()
                home_button1.destroy()
                warm_food.destroy()
                nextb.destroy()
                preb.destroy()
                f1.destroy()
                f2.destroy()
                f3.destroy()
                f4.destroy()
                f5.destroy()
                menu_screen1()

            def nextwf():
                back_button.destroy()
                home_button1.destroy()
                warm_food.destroy()
                nextb.destroy()
                preb.destroy()
                f1.destroy()
                f2.destroy()
                f3.destroy()
                f4.destroy()
                f5.destroy()
                freshf()

            def prewf():
                back_button.destroy()
                home_button1.destroy()
                warm_food.destroy()
                nextb.destroy()
                preb.destroy()
                f1.destroy()
                f2.destroy()
                f3.destroy()
                f4.destroy()
                f5.destroy()
                otherf()

            back_button = tk.Button(menu, text="Back", command=backwf, width=7, height=0, bg='#a63f59', bd=0,
                                    fg='white', font=('STHupo', 11))
            back_button.place(x=80, y=83)
            home_button1 = tk.Button(menu, text="Home", command=homewf, width=7, height=0, bg='#a63f59', bd=0,
                                     fg='white', font=('STHupo', 11))
            home_button1.place(x=20, y=83)
            nextb = tk.Button(menu, text=">", fg='white', command=nextwf, width=1, height=0, bg='#a63f59',
                              activebackground='white', bd=0, font=('STHupo', 11))
            nextb.place(x=200, y=83)
            preb = tk.Button(menu, text="<", fg='white', command=prewf, width=1, height=0, bg='#a63f59',
                             activebackground='white', bd=0, font=('STHupo', 11))
            preb.place(x=184, y=83)
            warm_food = tk.Label(menu, text="WARM FOOD", bg='#a63f59', fg='white', font=('STHupo', 12))
            warm_food.place(x=270, y=83)

            f1 = tk.Button(menu, text='Cheese Manakeesh', image=chesim, compound='top', width=160, height=154, bd=0,
                           bg='white', fg='#45212b',
                           font=('STCaiyun', 13), wraplength=110)
            f1.place(x=30, y=122)
            f2 = tk.Button(menu, text='Pizza', image=pizza, compound='top', width=160, height=154, bd=0, bg='white',
                           fg='#45212b',
                           font=('STCaiyun', 13), wraplength=110)
            f2.place(x=200, y=122)
            f3 = tk.Button(menu, text="Paneer Kadai", image=paneerkadaiwrapslices, width=160, height=154,
                           compound="top", bd=0, bg='white', fg='#45212b',
                           font=('STCaiyun', 13), wraplength=110)
            f3.place(x=30, y=287)
            f4 = tk.Button(menu, text="Chicken Caesar Wrap", image=chickencaesarwrapslices, width=160, height=154,
                           compound="top", bd=0, bg='white', fg='#45212b',
                           font=('STCaiyun', 13), wraplength=110)
            f4.place(x=200, y=287)
            f5 = tk.Button(menu, text='Turkey Cheese Sandwich', image=turkeycheesesandwich, compound='top', width=160,
                           height=154, bd=0, bg='white', fg='#45212b',
                           font=('STCaiyun', 13), wraplength=140)
            f5.place(x=30, y=452)

        def freshf():
            home_button.destroy()
            wf.destroy()
            ff.destroy()
            of.destroy()

            def backwf():
                back_button.destroy()
                home_button1.destroy()
                ffood.destroy()
                nextb.destroy()
                preb.destroy()
                categoryf()
                f1.destroy()
                f2.destroy()

            def homewf():
                back_button.destroy()
                home_button1.destroy()
                ffood.destroy()
                nextb.destroy()
                preb.destroy()
                menu_screen1()
                f1.destroy()
                f2.destroy()

            def nextwf():
                back_button.destroy()
                home_button1.destroy()
                ffood.destroy()
                nextb.destroy()
                preb.destroy()
                otherf()
                f1.destroy()
                f2.destroy()

            def prewf():
                back_button.destroy()
                home_button1.destroy()
                ffood.destroy()
                nextb.destroy()
                preb.destroy()
                warmf()
                f1.destroy()
                f2.destroy()

            back_button = tk.Button(menu, text="Back", command=backwf, width=7, height=0, bg='#a63f59', bd=0,
                                    fg='white', font=('STHupo', 11))
            back_button.place(x=80, y=83)
            home_button1 = tk.Button(menu, text="Home", command=homewf, width=7, height=0, bg='#a63f59', bd=0,
                                     fg='white', font=('STHupo', 11))
            home_button1.place(x=20, y=83)
            nextb = tk.Button(menu, text=">", fg='white', command=nextwf, width=1, height=0, bg='#a63f59',
                              activebackground='white', bd=0, font=('STHupo', 11))
            nextb.place(x=200, y=83)
            preb = tk.Button(menu, text="<", fg='white', command=prewf, width=1, height=0, bg='#a63f59',
                             activebackground='white', bd=0, font=('STHupo', 11))
            preb.place(x=184, y=83)
            ffood = tk.Label(menu, text="FRESH FOOD", bg='#a63f59', fg='white', font=('STHupo', 12))
            ffood.place(x=270, y=83)

            f1 = tk.Button(menu, text='Fruit Salad', image=fruitsalad, compound='top', width=160, height=154, bd=0,
                           bg='white', fg='#45212b',
                           font=('STCaiyun', 13), wraplength=110)
            f1.place(x=30, y=122)
            f2 = tk.Button(menu, text='Mac & Cheese', image=maches, compound='top', width=160, height=154, bd=0,
                           bg='white', fg='#45212b',
                           font=('STCaiyun', 13), wraplength=110)
            f2.place(x=200, y=122)

        def otherf():
            home_button.destroy()
            wf.destroy()
            ff.destroy()
            of.destroy()

            def backwf():
                back_button.destroy()
                home_button1.destroy()
                ofood.destroy()
                nextb.destroy()
                preb.destroy()
                f1.destroy()
                f2.destroy()
                f3.destroy()
                f4.destroy()
                categoryf()

            def homewf():
                back_button.destroy()
                home_button1.destroy()
                ofood.destroy()
                nextb.destroy()
                preb.destroy()
                f1.destroy()
                f2.destroy()
                f3.destroy()
                f4.destroy()
                menu_screen1()

            def nextwf():
                back_button.destroy()
                home_button1.destroy()
                ofood.destroy()
                nextb.destroy()
                preb.destroy()
                f1.destroy()
                f2.destroy()
                f3.destroy()
                f4.destroy()
                warmf()

            def prewf():
                back_button.destroy()
                home_button1.destroy()
                ofood.destroy()
                nextb.destroy()
                preb.destroy()
                f1.destroy()
                f2.destroy()
                f3.destroy()
                f4.destroy()
                freshf()

            back_button = tk.Button(menu, text="Back", command=backwf, width=7, height=0, bg='#a63f59', bd=0,
                                    fg='white', font=('STHupo', 11))
            back_button.place(x=80, y=83)
            home_button1 = tk.Button(menu, text="Home", command=homewf, width=7, height=0, bg='#a63f59', bd=0,
                                     fg='white', font=('STHupo', 11))
            home_button1.place(x=20, y=83)
            nextb = tk.Button(menu, text=">", fg='white', command=nextwf, width=1, height=0, bg='#a63f59',
                              activebackground='white', bd=0, font=('STHupo', 11))
            nextb.place(x=200, y=83)
            preb = tk.Button(menu, text="<", fg='white', command=prewf, width=1, height=0, bg='#a63f59',
                             activebackground='white', bd=0, font=('STHupo', 11))
            preb.place(x=184, y=83)
            ofood = tk.Label(menu, text="OTHER FOOD", bg='#a63f59', fg='white', font=('STHupo', 12))
            ofood.place(x=270, y=83)

            f1 = tk.Button(menu, text='Popcorn', image=popim, compound='top', width=160, height=154, bd=0, bg='white',
                           fg='#45212b',
                           font=('STCaiyun', 13), wraplength=110)
            f1.place(x=30, y=122)
            f2 = tk.Button(menu, text='Blueberry Muffin', image=bmuffin, compound='top', width=160, height=154, bd=0,
                           bg='white', fg='#45212b',
                           font=('STCaiyun', 13), wraplength=140)
            f2.place(x=200, y=122)
            f3 = tk.Button(menu, text='Raspberry Yogurt', image=yog1, compound='top', width=160, height=154, bd=0,
                           bg='white', fg='#45212b',
                           font=('STCaiyun', 13), wraplength=140)
            f3.place(x=30, y=287)
            f4 = tk.Button(menu, text='Penne Pasta', image=pennepastaslices, compound='top', width=160, height=154,
                           bd=0, bg='white', fg='#45212b',
                           font=('STCaiyun', 13), wraplength=110)
            f4.place(x=200, y=287)

        def homef():
            home_button.destroy()
            wf.destroy()
            ff.destroy()
            of.destroy()
            menu_screen1()

        home_button = tk.Button(menu, text="Home", command=homef, width=7, height=0, bg='#a63f59', bd=0, fg='white',
                                font=('STHupo', 11))
        home_button.place(x=20, y=83)

        wf = tk.Button(menu, width=360, height=140, text='        Warm Food', image=warmfood, compound='left',
                       command=warmf, bd=0, bg='white', fg='#45212b',
                       font=('STCaiyun', 13), wraplength=140, activebackground='#853447', activeforeground='white')
        ff = tk.Button(menu, width=360, height=140, text='        Fresh Food', image=freshfood, compound='left',
                       command=freshf, bd=0, bg='white', fg='#45212b',
                       font=('STCaiyun', 13), wraplength=140, activebackground='#853447', activeforeground='white')
        of = tk.Button(menu, width=360, height=140, text='        Other Food', image=otherfood, compound='left',
                       command=otherf, bd=0, bg='white', fg='#45212b',
                       font=('STCaiyun', 13), wraplength=140, activebackground='#853447', activeforeground='white')
        wf.place(x=17, y=120)
        ff.place(x=17, y=280)
        of.place(x=17, y=440)

    def categoryb():
        foodscat.destroy()
        beveragecat.destroy()

        def homeb():
            home_button.destroy()
            menu_screen1()
            applejuice.destroy()
            orangejuice.destroy()
            mangojuice.destroy()
            labanmilk.destroy()
            f1.destroy()

        home_button = tk.Button(menu, text="Home", command=homeb, width=7, height=0, bg='#a63f59', bd=0, fg='white',
                                font=('STHupo', 11))
        home_button.place(x=20, y=83)

        applejuice = tk.Button(menu, text="Apple Juice", image=applej1, width=160, height=154, compound="top", bd=0,
                               bg='white', fg='#45212b',
                               font=('STCaiyun', 13), wraplength=110)
        applejuice.place(x=30, y=122)
        orangejuice = tk.Button(menu, text="Orange Juice", image=orangeim, width=160, height=154, compound="top", bd=0,
                                bg='white', fg='#45212b',
                                font=('STCaiyun', 13), wraplength=110)
        orangejuice.place(x=200, y=122)
        mangojuice = tk.Button(menu, text="Mango Juice", image=mangoim, width=160, height=154, compound="top", bd=0,
                               bg='white', fg='#45212b',
                               font=('STCaiyun', 13), wraplength=110)
        mangojuice.place(x=30, y=287)
        labanmilk = tk.Button(menu, text="Laban Milk", image=labanm, width=160, height=154, compound="top", bd=0,
                              bg='white', fg='#45212b',
                              font=('STCaiyun', 13), wraplength=110)
        labanmilk.place(x=200, y=287)
        f1 = tk.Button(menu, text='Water', image=water, compound='top', width=160, height=154, bd=0, bg='white',
                       fg='#45212b',
                       font=('STCaiyun', 13), wraplength=110)
        f1.place(x=30, y=452)

    def information():
        messagebox.showinfo('Info', "Made by Rasya, Taher, Sean, Bryce - From 9B1 - Our ICT project")

    info_button = tk.Button(menu, image=info, width=20, height=20, command=information, bd=0, bg='#a63f59',
                            activebackground='#a63f59')
    info_button.place(x=373, y=5)

    foodscat = tk.Button(menu, text="     Food", command=categoryf, width=360, height=220, image=food, compound="left",
                         bd=0, bg='white', fg='#45212b',
                         font=('STCaiyun', 16), wraplength=140, activebackground='#853447', activeforeground='white')
    foodscat.place(x=17, y=120)
    beveragecat = tk.Button(menu, text="      Beverages", command=categoryb, width=360, height=220, image=beverage,
                            compound="left", bd=0, bg='white', fg='#45212b',
                            font=('STCaiyun', 16), wraplength=140, activebackground='#853447', activeforeground='white')
    beveragecat.place(x=17, y=360)


menu_screen1()

menu.mainloop()
