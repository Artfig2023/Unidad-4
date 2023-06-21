from tkinter import *
from tkinter import ttk, messagebox, font

class Aplicacion:
    __ventana = 0
    __vestimenta = ''
    __vestañobase = ''
    __vestañoactual = ''
    __alimentos = ''
    __aliañobase = ''
    __aliañoactual = ''
    __educacion = ''
    __eduañobase = ''
    __eduañoactual = ''

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('600x409')
        self.__ventana.title('Calculadora IPC')
        self.__ventana.columnconfigure(0, weight=1)
        self.__ventana.configure(background='white')
        self.__vestimenta = StringVar()
        self.__vestañobase = StringVar()
        self.__vestañoactual = StringVar()
        self.__alimentos = StringVar()
        self.__aliañobase = StringVar()
        self.__aliañoactual = StringVar()
        self.__educacion = StringVar()
        self.__eduañobase = StringVar()
        self.__eduañoactual = StringVar()

        ttk.Label(self.__ventana, text='item').grid(column=0, row=0, sticky=(NW))
        ttk.Label(self.__ventana, text='Cantidad').grid(column=1, row=0, sticky=(NW))
        ttk.Label(self.__ventana, text='Precio Año Base').grid(column=2, row=0, sticky=(NW))
        ttk.Label(self.__ventana, text='Precio Año Actual').grid(column=3, row=0, sticky=(NW))
        ttk.Label(self.__ventana, text='Vestimenta').grid(column=0, row=1, sticky=(W))
        ttk.Label(self.__ventana, text='Alimentos').grid(column=0, row=2, sticky=(W))
        ttk.Label(self.__ventana, text='Educacion').grid(column=0, row=3, sticky=(W))

        self.vestimentaEnty = ttk.Entry(self.__ventana, textvariable=self.__vestimenta)
        self.vestimentaEnty.grid(row=1, column=1, pady=0, ipadx=0)

        self.vestañobaseEnty = ttk.Entry(self.__ventana, textvariable=self.__vestañobase)
        self.vestañobaseEnty.grid(sticky='w', row=1, column=2, pady=0, ipadx=0)

        self.vestañoactualEnty = ttk.Entry(self.__ventana, textvariable=self.__vestañoactual)
        self.vestañoactualEnty.grid(sticky='w', row=1, column=3, pady=0, ipadx=0)

        self.alimentosEnty = ttk.Entry(self.__ventana, textvariable=self.__alimentos)
        self.alimentosEnty.grid(sticky='w', row=2, column=1)

        self.alibaseenty = ttk.Entry(self.__ventana, textvariable=self.__aliañobase)
        self.alibaseenty.grid(sticky='w', row=2, column=2)

        self.alimactualenty = ttk.Entry(self.__ventana, textvariable=self.__aliañoactual)
        self.alimactualenty.grid(sticky='w', row=2, column=3)

        self.educacionEnty = ttk.Entry(self.__ventana, textvariable=self.__educacion)
        self.educacionEnty.grid(sticky='w', row=3, column=1)

        self.edubaseEnty = ttk.Entry(self.__ventana, textvariable=self.__eduañobase)
        self.edubaseEnty.grid(sticky='w', row=3, column=2)

        self.eduactualEnty = ttk.Entry(self.__ventana, textvariable=self.__eduañoactual)
        self.eduactualEnty.grid(sticky='w', row=3, column=3)

        self.button1 = ttk.Button(self.__ventana, text= 'Calcular IPC', command=self.aceptar())
        self.button1.grid(sticky='s', row=4, column=1)

        self.button2 = ttk.Button(self.__ventana, text= 'Salir', command=quit)
        self.button2.grid(sticky='s', row='4', column=3)

        self.resullbl = ttk.Label(self.__ventana, text='IPC % {}'.format(self.aceptar()))
        self.resullbl.grid(sticky=(S), row=6, column=0)

    def aceptar(self):
        pass

    def ejecutar(self):
        self.__ventana.mainloop()



        """self.vestimentalbl = ttk.Label(self.__ventana,text='Vestimenta', font=(14), background='white')
        self.vestimentalbl.grid(sticky='e', row=1, column=1, pady=30)
        self.vestimentaEntry = ttk.Entry(self.__ventana, textvariable=self.__vestimenta)
        self.vestimentaEntry.grid(sticky='w', row=1, column=1, pady=20, ipadx=70)

        self.vestañobaselbl = ttk.Label(self.__ventana, 'Año base', font=(14), background='white')
        self.vestañobaselbl.grid(sticky='e', row=1, column=2, pady=30)
        self.vestañobaseEntry = ttk.Entry(self.__ventana, textvariable=self.__vestañobase)
        self.vestañobaseEntry.grid(sticky='w', row=1, column=2, pady=20, ipadx=14)

        self.vestañoactuallbl = ttk.Label(self.__ventana, text='Año actual', font=(14), background='white')
        self.vestañoactuallbl.grid(sticky='e', row=1, column=3, pady=30)
        self.vestañoactualEnty = ttk.Entry(self.__ventana, textvariable=self.__vestañoactual)
        self.vestañoactualEnty.grid(sticky='w', row=1, column=3, pady=20, ipadx=70)

        self.alimentoslbl = ttk.Label(self.__ventana, text='Alimentos', font=(14), background='white')
        self.alimentoslbl.grid(sticky='e', row=2, column=1, pady=30)
        self.alimentosEnty = ttk.Entry(self.__ventana, textvariable=self.__aliañobase)
        self.alimentosEnty.grid(sticky='w', row=2, column=1, pady=20, ipadx=70)

        self.aliañobaselbl = ttk.Label(self.__ventana, text='Año base', font=(14), background='white')
        self.aliañobaselbl.grid(sticky='e', row=2, column=2, pady=30)
        self.aliañobaseEnty = ttk.Entry(self.__ventana, textvariable=self.__aliañobase)
        self.aliañobaseEnty.grid(sticky='e', row=2, column=2, pady=20, ipadx=70)

        self.aliañoactuallbl = ttk.Label(self.__ventana, text='Año actual', font=(14), background='white')
        self.aliañoactuallbl.grid(sticky='e', row=2, column=3, pady=30)
        self.aliañoactualEnty = ttk.Entry(self.__ventana, textvariable=self.__aliañoactual)
        self.aliañoactualEnty.grid(sticky='e', row=2, column=3, pady=20, ipadx=70)

        self.educacionlbl = ttk.Label(self.__ventana, text='Educacion', font=(14), background='white')
        self.educacionlbl.grid(sticky='e', row=3, column=1, pady=30)
        self.educacionEnty = ttk.Entry(self.__ventana, textvariable=self.__educacion)
        self.educacionEnty.grid(sticky='e', row=3, column=1, pady=20, ipadx=70)

        self.eduañobaselbl = ttk.Label(self.__ventana, text='Año base', font=(14), background='white')
        self.eduañobaselbl.grid(sticky='e', row=3, column=2, pady=30)
        self.eduañobaseEnty = ttk.Entry(self.__ventana, textvariable=self.__eduañobase)
        self.eduañobaseEnty.grid(sticky='e', row=3, column=2, pady=20, ipadx=70)

        self.eduañoactuallbl = ttk.Label(self.__ventana, text='Año actual', font=(14), background='white')
        self.eduañoactuallbl.grid(sticky='e', row=3, column=3, pady=30)
        self.eduañoactualEnty = ttk.Entry(self.__ventana, textvariable=self.__eduañoactual)
        self.eduañoactualEnty.grid(sticky='e', row=3, column=3, pady=20, ipadx=70)"""