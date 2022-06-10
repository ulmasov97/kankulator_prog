from tkinter import *
root = Tk()
root.title("Kalkulator")
# root.geometry("350x400")
# root.resizable(False,False)
root.configure(bg="#17161b")

input1 = Entry(root, width=43, borderwidth=3,font=("arial",10))
input1.grid(row=0, column=0, columnspan=10,padx=10,pady=20)

def button_click(number):
	string = input1.get()
	input1.delete(0, END)
	input1.insert(0, str(string)+str(number))

def button_clear():
	input1.delete(0, END)

def button_add():
	raqamni_olish = input1.get()
	global saqlangan_raqam
	global amal
	amal = "qushish"
	saqlangan_raqam = int(raqamni_olish)
	input1.delete(0, END)

def button_ayir():
	raqamni_olish = input1.get()
	global saqlangan_raqam
	global amal
	amal = "ayirish"
	saqlangan_raqam = int(raqamni_olish)
	input1.delete(0, END)

def button_bul():
	raqamni_olish = input1.get()
	global saqlangan_raqam
	global amal
	amal = "bulish"
	saqlangan_raqam = int(raqamni_olish)
	input1.delete(0, END)

def button_kup():
	raqamni_olish = input1.get()
	global saqlangan_raqam
	global amal
	amal = "kupaytirish"
	saqlangan_raqam = int(raqamni_olish)
	input1.delete(0, END)


def button_tenglik():
	summa = input1.get()	
	input1.delete(0, END)
	if amal == "qushish":
		input1.insert(0, saqlangan_raqam + int(summa))		
	if amal == "ayirish":
		input1.insert(0, saqlangan_raqam - int(summa))
	if amal == "bulish":
		input1.insert(0, saqlangan_raqam // int(summa))
	if amal == "kupaytirish":
		input1.insert(0, saqlangan_raqam * int(summa))

button_1 = Button(root, text="1", padx=35, pady=15,bd=1,fg="#fff",bg="#2a2d36",command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=35, pady=15,bd=1,fg="#fff",bg="#2a2d36",command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=35, pady=15,bd=1,fg="#fff",bg="#2a2d36",command=lambda: button_click(3))

button_4 = Button(root, text="4", padx=35, pady=15,bd=1,fg="#fff",bg="#2a2d36",command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=35, pady=15,bd=1,fg="#fff",bg="#2a2d36",command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=35, pady=15,bd=1,fg="#fff",bg="#2a2d36",command=lambda: button_click(6))

button_7 = Button(root, text="7", padx=35, pady=15,bd=1,fg="#fff",bg="#2a2d36",command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=35, pady=15,bd=1,fg="#fff",bg="#2a2d36",command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=35, pady=15,bd=1,fg="#fff",bg="#2a2d36",command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=35, pady=15,bd=1,fg="#fff",bg="#2a2d36",command=lambda: button_click(0))

button_add = Button(root, text="+", padx=34, pady=15,bd=1,command=button_add)
button_ay = Button(root, text="-", padx=35, pady=15,bd=1,command=button_ayir)
button_bull = Button(root, text="/", padx=35, pady=15,bd=1,command=button_bul)
button_kupp = Button(root, text="*", padx=35, pady=15,bd=1,command=button_kup)
button_teng = Button(root, text="=", padx=34, pady=15,bd=1,fg="#fff",bg="#fe9037",command=button_tenglik)
button_clr = Button(root, text="C", padx=34, pady=15,bd=1,fg="#fff",bg="#3697f5",command=button_clear)


button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=4,column=0)
button_5.grid(row=4,column=1)
button_6.grid(row=4,column=2)

button_7.grid(row=5,column=0)
button_8.grid(row=5,column=1)
button_9.grid(row=5,column=2)
button_0.grid(row=6,column=1)

button_add.grid(row=3,column=3)
button_ay.grid(row=4,column=3)
button_bull.grid(row=5,column=3)
button_kupp.grid(row=6,column=3)
button_teng.grid(row=6,column=2)
button_clr.grid(row=6,column=0)

root.mainloop()

