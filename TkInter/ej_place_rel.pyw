from tkinter import Tk, Label, Button, Entry

vent = Tk()
vent.title("Ejemplo de place")
vent.geometry("400x200")

def fnSuma():
    n1 = txt1.get()
    n2 = txt2.get()
    r = float(n1) + float(n2)
    txt3.delete(0,'end')
    txt3.insert(0,r)


lbl1 = Label(vent,text="Primer numero", bg="yellow")
lbl1.place(relx=0.03,rely=0.04, relwidth=0.23, relheight=0.1)
txt1 = Entry(vent, bg="pink")
txt1.place(relx=0.3, rely=0.04, relwidth=0.22, relheight=0.1)

lbl2 = Label(vent,text="Segundo numero", bg="yellow")
lbl2.place(relx=0.03,rely=0.17, relwidth=0.23, relheight=0.1)
txt2 = Entry(vent, bg="pink")
txt2.place(relx=0.3,rely=0.17, relwidth=0.22, relheight=0.1)

btn1=Button(vent,text="Sumar", command=fnSuma)
btn1.place(relx=0.55,rely=0.17, relwidth=0.20, relheight=0.1)

lbl3 = Label(vent,text="Resultado", bg="yellow")
lbl3.place(relx=0.03,rely=0.35, relwidth=0.23, relheight=0.1)
txt3 = Entry(vent, bg="pink")
txt3.place(relx=0.3,rely=0.35, relwidth=0.22, relheight=0.1)


vent.mainloop()