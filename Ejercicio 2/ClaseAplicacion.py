from tkinter import *
from tkinter import ttk, messagebox

class Aplicacion:
    __mainframe = None
    __preciobase = 0
    __iva = 0
    __impuesto = 0
    __total = 0

    def __init__(self):
        self.__mainframe = Tk()
        self.__mainframe.title('Calculo de IVA')
        self.__mainframe.geometry('350x350')
        self.__mainframe.rowconfigure(0, weight=1)
        self.__mainframe.rowconfigure(1, weight=1)
        self.__mainframe.rowconfigure(2, weight=1)
        self.__mainframe.rowconfigure(3, weight=1)
        self.__mainframe.columnconfigure(0, weight=1)
        self.__preciobase = StringVar()
        self.__iva = StringVar()
        self.__impuesto = StringVar()
        self.__total = StringVar()
        stylebar = ttk.Style()
        stylebar.configure('BW.TLabe', background="limegreen")
        self.tituframe = ttk.Frame(self.__mainframe, height=50, style="BW.TLabel")
        self.tituframe.configure(border=1, borderwidth=1)
        self.tituframe.grid(row=0, column=0, sticky='nwe')
        self.tituframe.rowconfigure(0, weight=1)
        self.tituframe.columnconfigure(0, weight=1)
        self.titulabel = ttk.Label(self.tituframe, text='Calculo de IVA', font=('Helvetica', 15), background='limegreen')
        self.titulabel.grid(row=0, column=0, sticky='nw', padx=100, ipadx=20, pady=20)

        self.labelprecioiva = ttk.Label(self.__mainframe, text='Precio sin IVA', background='white')
        self.labelprecioiva.grid(row=1, column=0, sticky='w', padx=15)
        self.__Entrypreciosiniva = ttk.Entry(self.__mainframe, textvariable=self.__preciobase, width=20)
        self.__Entrypreciosiniva.grid(row=1, column=0, sticky='w', padx=100, ipadx=3)

        stylebutton = ttk.Style()
        stylebutton.configure('Wild.TRadiobutton', background='white')

        self.radioiva10 = ttk.Radiobutton(self.__mainframe, text='IVA 10.5%', value=10, variable=self.__iva, state='Wild.TRadiobutton')
        self.radioiva10.grid(row=2, column=0, sticky='nw', pady=40, padx=20)

        self.radioiva21= ttk.Radiobutton(self.__mainframe, text='IVA 21%', value=21, variable=self.__iva, style='Wild.TRadiobutton')
        self.radioiva21.grid(row=2, column=0, sticky='nw', pady=40, padx=20)

        self.LavelIVA = ttk.Label(self.__mainframe, text='IVA', background='white')
        self.LavelIVA.grid(row=2, column=0, sticky='w', pady=70, padx=30)
        self.__EntryIVA = ttk.Entry(self.__mainframe, textvariable=self.__impuesto, state='disable')
        self.__EntryIVA.grid(row=2, column=0, sticky='w', padx=120)

        self.labelprecioconiva = ttk.Label(self.__mainframe, text='Precio con IVA', background='white')
        self.labelprecioconiva.grid(row=2, column=0, sticky='sw', pady=45, padx=30)
        self.__EntryPrecioconIVA = ttk.Entry(self.__mainframe, textvariable=self.__total, state='disable')
        self.__EntryPrecioconIVA.grid(row=2, column=0, sticky='sw', pady=45, padx=120)

        self.botoncalcular = Button(self.__mainframe, text='Calcular', height=2, width=10, background='lightgreen', command=lambda: self.calcular)
        self.botoncalcular.grid(row=3, column=0, sticky='w', padx=30)

        self.botonsalir = Button(self.__mainframe, text='Salir', height=2, width=10, background='pink', command=lambda:quit())
        self.botonsalir.grid(row=3, column=0, sticky='e', padx=80)

        self.__Entrypreciosiniva.focus()
    
    def calcular(self):
        try:
            pbase = float(self.__Entrypreciosiniva.get())
            if int(self.__iva.get()) == 10:
                imp = (pbase * 10.5) / 100
                tot = pbase + imp
            elif int(self.__iva.get()) == 21:
                imp = (pbase * 21) / 100
                tot = pbase + imp
            else:
                tot = 0
                imp = 0
            self.__impuesto.set(str(imp))
            self.__total.set(str(tot))
        except ValueError:
            messagebox.showerror(title='Error de tipo', message='Debe ingresar un valor numerico')


    def ejecutar(self):
        self.__mainframe.mainloop()