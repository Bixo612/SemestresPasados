from tkinter import Label,Button,Entry,Frame,Tk, messagebox
from libFracMix import FracMix
from tkinter.ttk import Combobox



class MainFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=320, height=170)
        self.master = master        
        self.pack()        
        self.create_widgets()

    def fCalcular(self):
        e1 = int(self.txt1E.get())
        n1 = int(self.txt1N.get())
        d1 = int(self.txt1D.get())
        f1 = FracMix(e1,n1,d1)
        e2 = int(self.txt2E.get())
        n2 = int(self.txt2N.get())
        d2 = int(self.txt2D.get())
        f2 = FracMix(e2,n2,d2)

        if self.cmbOpciones.get() == self.opciones[4]:
            if f1 == f2:
                messagebox.showinfo(title="Fracciones Mixtas", message = "Las fracciones son iguales")
            else:
                messagebox.showinfo(title="Fracciones Mixtas", message = "Las fracciones son diferentes")
        else:
            if self.cmbOpciones.get() == self.opciones[0]:
                f3 = f1+f2
            elif self.cmbOpciones.get() == self.opciones[1]:
                f3 = f1-f2
            elif self.cmbOpciones.get() == self.opciones[2]:
                f3 = f1*f2
            elif self.cmbOpciones.get() == self.opciones[3]:
                f3 = f1/f2        
                
            self.txtRes.delete(0,'end')
            self.txtRes.insert(0,f3)


        

    def create_widgets(self):
        fFrac1= Frame(self,width=100, height=60)
        fFrac1.place(x=30,y=30)
        fx1=Frame(fFrac1,width=42, height=27)
        fx1.grid(row=0,column=0,rowspan=2)
        Label(fx1,text="Ent").pack(side="left")
        self.txt1E = Entry(fx1,width=4)
        self.txt1E.pack(side="right")
        Label(fFrac1,text="Num").grid(row=0,column=2)
        Label(fFrac1,text="Den").grid(row=1,column=2)
        self.txt1N=Entry(fFrac1,width=4)
        self.txt1D=Entry(fFrac1,width=4)
        self.txt1N.grid(row=0,column=1)
        self.txt1D.grid(row=1,column=1)
        fFrac2= Frame(self,width=100, height=60)
        fFrac2.place(x=180,y=30)
        fx2=Frame(fFrac2,width=42, height=27)
        fx2.grid(row=0,column=0,rowspan=2)
        Label(fx2,text="Ent").pack(side="left")
        self.txt2E = Entry(fx2,width=4)
        self.txt2E.pack(side="right")
        Label(fFrac2,text="Num").grid(row=0,column=2)
        Label(fFrac2,text="Den").grid(row=1,column=2)
        self.txt2N=Entry(fFrac2,width=4)
        self.txt2D=Entry(fFrac2,width=4)
        self.txt2N.grid(row=0,column=1)
        self.txt2D.grid(row=1,column=1)
        Label(self,text="Fraccion 1:").place(x=48,y=8)
        Label(self,text="Fraccion 2:").place(x=198,y=8)
        Label(self,text="Operación:").place(x=30,y=90)
        Label(self,text="Resultado:").place(x=30,y=130)
        self.txtRes=Entry(self,width=15)
        self.txtRes.place(x=100,y=130)
        self.btnCalcular=Button(self,text="Calcular", command=self.fCalcular)
        self.btnCalcular.place(x=210,y=90)
        
        self.opciones=["Suma", "Resta", "Multiplicación","División", "Son Iguales?"]
        self.cmbOpciones = Combobox(self, width="10", values=self.opciones, state="readonly")
        self.cmbOpciones.place(x=100,y=90)
        self.cmbOpciones.current(0)


        

        




