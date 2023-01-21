import tkinter as tk

form=tk.Tk()
form.title("Pizza Home")

form.config(bg="lightSteelBlue3")
form.geometry("1500x750")
#form.resizable(False,False)

baslik = tk.Label(text="Pizza Evi",bg="lightSteelBlue3",fg="white",font=("Comic Sans MS",36,"italic"))
baslik.place(x=675,y=35)

#-----------------------------------------------------------------------------------------------
ad1=tk.stringVar()
ad = tk.Label(text="Ad-Soyad",bg="lightSteelBlue3",fg="white",font=("Comic Sans MS",18,"italic"))
ad.place(x=200,y=120)

entry_ad=tk.Entry(textvalue=ad1,fg="lightSteelBlue3", font=("Comic Sans MS", 18 , "bold"))
entry_ad.place(x=375,y=120)

#-----------------------------------------------------------------------------------------------
boyut2= tk.Label(text="Pizza Boyutu",bg="lightSteelBlue3",fg="white",font=("Comic Sans MS",18,"italic"))
boyut2.place(x=200,y=220)

boyut = tk.stringVar()

kücük=tk.Radiobutton(text="Küçük", value="Küçük Boy",fg="lightSteelBlue3", activebackground="lightSteelBlue3",font=("Comic Sans MS", 18 , "bold"),variable=boyut)
kücük.place(x=375,y=220)

orta=tk.Radiobutton(text="Orta", value="Orta Boy",fg="lightSteelBlue3", activebackground="lightSteelBlue3",font=("Comic Sans MS", 18 , "bold"),variable=boyut)
orta.place(x=550,y=220)

büyük=tk.Radiobutton(text="Büyük",value="Büyük Boy",fg="lightSteelBlue3", activebackground="lightSteelBlue3",font=("Comic Sans MS", 18 , "bold"),variable=boyut)
büyük.place(x=725,y=220)


#-----------------------------------------------------------------------------------------------

icindekiler = tk.Label(text="İçindekiler",bg="lightSteelBlue3",fg="white",font=("Comic Sans MS",18,"italic"))
icindekiler.place(x=200,y=320)

deger1=tk.stringVar()
deger2=tk.stringVar()
deger3=tk.stringVar()
deger4=tk.IntVar()
deger5=tk.IntVar()


def d5Selected():
    if check5:
        lb_icindekiler1 = tk.Label(form, text="Salam", fg="lightSteelBlue3", font=("Comic Sans MS", 18, "bold"))
        lb_icindekiler1.place(x=495, y=805)
    elif check4:
        check4 = tk.Checkbutton(form, text="Biber", onvalue="Biber", variable=deger4, fg="lightSteelBlue3",
                                font=("Comic Sans MS", 18, "bold"))
        check4.place(x=900, y=320)


check1=tk.Checkbutton(form,text="Sucuk",variable=deger1,onvalue="Sucuk",fg="lightSteelBlue3", font=("Comic Sans MS", 18 , "bold"))
check1.place(x=375,y=320)

check2=tk.Checkbutton(form,text="Mısır",variable=deger2,onvalue="Mısır",fg="lightSteelBlue3", font=("Comic Sans MS", 18 , "bold"))
check2.place(x=550,y=320)

check3=tk.Checkbutton(form,text="Zeytin",variable=deger3,onvalue="Zeytin",fg="lightSteelBlue3", font=("Comic Sans MS", 18 , "bold"))
check3.place(x=725,y=320)

check4=tk.Checkbutton(form,text="Biber",onvalue="Biber", variable=deger4,fg="lightSteelBlue3", font=("Comic Sans MS", 18 , "bold"))
check4.place(x=900,y=320)


check5=tk.Checkbutton(form,text="Salam", onvalue=1,offvalue=0, variable=deger5, command=d5Selected ,fg="lightSteelBlue3", font=("Comic Sans MS", 18 , "bold"))
check5.place(x=1075,y=320)


#-----------------------------------------------------------------------------------------------

adres=tk.stringVar()
Adres = tk.Label(text="Adres",bg="lightSteelBlue3",fg="white",font=("Comic Sans MS",18,"italic"))
Adres.place(x=200,y=420)

entry_adres=tk.Entry(textvalue=adres,fg="lightSteelBlue3", font=("Comic Sans MS", 18 , "bold"))
entry_adres.place(x=375,y=420)


#-----------------------------------------------------------------------------------------------

def siparis():

    bilgi=tk.Label(form, text="Sipariş Bilgileri" , fg="lightSteelBlue3" ,  font=("Comic Sans MS", 18 , "bold"))
    bilgi.place(x=375,y=625)

    lb_ad=tk.Label(form, text="Ad-Soyad" , fg="lightSteelBlue3" ,  font=("Comic Sans MS", 18 ,"bold"))
    lb_ad.place(x=320,y=685)

    lb_boyut=tk.Label(form, text="Pizza Boyutu" , fg="lightSteelBlue3" ,  font=("Comic Sans MS", 18 ,"bold"))
    lb_boyut.place(x=320,y=745)

    lb_icindekiler = tk.Label(form, text="İçindekiler", fg="lightSteelBlue3", font=("Comic Sans MS", 18, "bold"))
    lb_icindekiler.place(x=320, y=805)

    lb_Adres = tk.Label(form, text="Adres", fg="lightSteelBlue3", font=("Comic Sans MS", 18, "bold"))
    lb_Adres.place(x=320, y=865)
    # -----------------------------------------------------------------------------------------------

    lb_ad1= tk.Label(form, text=entry_ad.get(), fg="lightSteelBlue3", font=("Comic Sans MS", 18, "bold"))
    lb_ad1.place(x=495, y=685)

    lb_boyut1 = tk.Label(form, text="boyut", fg="lightSteelBlue3", font=("Comic Sans MS", 18, "bold"))
    lb_boyut1.place(x=495, y=745)


    lb_Adres1 = tk.Label(form, text=entry_adres.get(), fg="lightSteelBlue3", font=("Comic Sans MS", 18, "bold"))
    lb_Adres1.place(x=495, y=865)
    d5Selected()



def iptal():
    form.quit()


Siparis=tk.Button(form, text="Sipariş Ver" , fg="lightSteelBlue3" ,  font=("Comic Sans MS", 18 , "bold") , command=siparis)
Siparis.place(x=300,y=525)

iptal=tk.Button(form, text="İptal Et" , fg="lightSteelBlue3" ,  font=("Comic Sans MS", 18 , "bold") , command=iptal)
iptal.place(x=500,y=525)







form.mainloop()