from tkinter import *
from tkinter import ttk, messagebox
import json
from urllib.request import urlopen

class Aplicacion:
    __dolar = None
    __pesos = None

    def __init__(self):
        self.__dolarventa = self.consulta()
        self.__ventana = Tk()
        self.__ventana.title('Conversor en moneda')
        self.__dolar = StringVar()
        self.__pesos = StringVar()

        self.__mainframe = ttk.Frame(self.__ventana, padding=(3,3,12,12))
        self.__mainframe.configure(borderwidth=2, relief='sunken')
        self.__mainframe.grid(row=0, column=0, sticky='nswe')
        self.__mainframe.rowconfigure(0, weight=1)
        self.__mainframe.columnconfigure(0, weight=1)

        self.__entryDolar = ttk.Entry(self.__mainframe, width=8, textvariable=self.__dolar)
        self.__entryDolar.grid(row=1, column=3, sticky='we')

        labelDolar = ttk.Label(self.__mainframe, text='Dolares')
        labelDolar.grid(row=1, column=3, sticky='we')

        lavelequiv = ttk.Label(self.__mainframe, text='es equivalente a ')
        lavelequiv.grid(row=3, column=1)

        labelpesoconvertido = Label(self.__mainframe, textvariable=self.__pesos)
        labelpesoconvertido.grid(row=3, column=2)

        labelpesotext = ttk.Label(self.__mainframe, text='Pesos')
        labelpesotext.grid(row=3, column=3)

        botonsalir = Button(self.__mainframe, text='Salir', command=lambda: quit())
        botonsalir.grid(row=4, column=3)

        self.__dolar.trace('w', self.conversion)
        self.__entryDolar.focus()

    def consulta(self):
        url_template = 'https://www.dolarsi.com/api/api.php?type=dolar'
        respose = urlopen(url_template)
        self.resultado = json.loads(respose.read().decode())
        return self.resultado[0]['casa']['venta']

    def conversion(self, *args):
        if self.__dolar.get() != '':
            try:
                dolares = float(self.__dolar.get())
                self.__dolarventa = self.__dolarventa.replace(',','.')
                total = dolares * float(self.__dolarventa)
                self.__pesos.set('%.2f' % (total))
            except ValueError:
                messagebox.showerror(title='Error', message='Debes ingresar un valor numerico')
        else:
            self.__pesos.set('')

    def ejecutar(self):
        self.__mainframe = mainloop()