from tkinter import Tk,Label,Button,Entry

vent = Tk()
vent.title("Ejemplo place")
vent.geometry("800x400")


def fSuma():
    n1=txtNum1.get()
    n2=txtNum2.get()
    r=float(n1)+float(n2)
    txtNum3.delete(0,'end')
    txtNum3.insert(0,r)    
    

lblNum1 = Label(vent,text="Primer Número: ",bg="yellow")
txtNum1=Entry(vent,bg="pink")
lblNum2 = Label(vent,text="Segundo Número: ",bg="yellow")
txtNum2=Entry(vent,bg="pink")
btn1=Button(vent,text="Sumar", command=fSuma)
lblNum3 = Label(vent,text="Resultado: ",bg="yellow")
txtNum3=Entry(vent,bg="cyan")

lblNum1.grid(row=0,column=0,padx=6, pady=6, sticky="w",ipady=6)
txtNum1.grid(row=0,column=1,padx=6, pady=6)
lblNum2.grid(row=1,column=0,padx=6, pady=6, sticky="w",ipady=6)
txtNum2.grid(row=1,column=1,padx=6, pady=6)
btn1.grid(row=1,column=2,padx=6, pady=6, ipady=4, ipadx=10)
lblNum3.grid(row=2,column=0,padx=6, pady=6, sticky="w",ipady=6)
txtNum3.grid(row=2,column=1,padx=6, pady=6)


vent.mainloop()