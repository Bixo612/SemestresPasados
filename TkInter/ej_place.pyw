from tkinter import Tk,Label,Button,Entry

vent = Tk()
vent.title("Ejemplo place")
vent.geometry("400x200")


def fSuma():
    n1=txtNum1.get()
    n2=txtNum2.get()
    r=float(n1)+float(n2)
    txtNum3.delete(0,'end')
    txtNum3.insert(0,r)    
    

lblNum1 = Label(vent,text="Primer Número: ",bg="yellow")
lblNum1.place(x=10,y=10,width=100, height=30)
txtNum1=Entry(vent,bg="pink")
txtNum1.place(x=120,y=10,width=100, height=30)

lblNum2 = Label(vent,text="Segundo Número: ",bg="yellow")
lblNum2.place(x=10,y=50,width=100, height=30)
txtNum2=Entry(vent,bg="pink")
txtNum2.place(x=120,y=50,width=100, height=30)

btn1=Button(vent,text="Sumar", command=fSuma)
btn1.place(x=230,y=50,width=80, height=30)

lblNum3 = Label(vent,text="Resultado: ",bg="yellow")
lblNum3.place(x=10,y=120,width=100, height=30)
txtNum3=Entry(vent,bg="cyan")
txtNum3.place(x=120,y=120,width=100, height=30)


vent.mainloop()
