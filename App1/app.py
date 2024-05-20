from tkinter import *
from tkinter import messagebox
from recopilar_procesos import recopilar_procesos
from recopilar_procesos import procss


def callback():
    num_procesos_str = num_procesos_entry.get()
    id_catalogo_str = id_entry.get()

    if num_procesos_str.isdigit() and id_catalogo_str.isdigit():
        num_procesos = int(num_procesos_str)
        recopilar_procesos(id_entry.get(), nombre_catalogo_entry.get(), num_procesos, var.get())
        
        # for i in procss:
        #     p.config(text=i)
    else:
        messagebox.showerror("Error Campos no llenados", "Debe rellenar los campos")

ventana = Tk()
ventana.title('Aplicación 1 - Procesos')
ventana.geometry('400x400')
ventana.iconbitmap('icono.ico')

titulo_label = Label(ventana, text="Recopilador de procesos", font=("Arial", 14))
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

id_label = Label(ventana, text="ID", font=("Arial", 12))
id_label.grid(row=1, column=0, pady=10)
id_entry = Entry(ventana, font=("Arial", 12))
id_entry.grid(row=1, column=1)

nombre_catalogo_label = Label(ventana, text="Nombre del catálogo", font=("Arial", 12))
nombre_catalogo_label.grid(row=2, column=0, pady=10)
nombre_catalogo_entry = Entry(ventana, font=("Arial", 12))
nombre_catalogo_entry.grid(row=2, column=1)

num_procesos_label = Label(ventana, text="Número de procesos", font=("Arial", 12))
num_procesos_label.grid(row=3, column=0, pady=10)
num_procesos_entry = Entry(ventana, font=("Arial", 12))
num_procesos_entry.grid(row=3, column=1)

var = StringVar(value="cpu")
cpu_radiobutton = Radiobutton(ventana, text="Mayor uso de CPU", variable=var, value="cpu", font=("Arial", 12))
memoria_radiobutton = Radiobutton(ventana, text="Mayor uso de memoria", variable=var, value="memoria", font=("Arial", 12))

cpu_radiobutton.grid(row=4, column=0, pady=10)
memoria_radiobutton.grid(row=4, column=1, pady=10)

boton_guardar = Button(ventana, text="Guardar", command=callback, font=("Arial", 12), bg="lightblue")
boton_guardar.grid(row=5, column=0, columnspan=2, pady=20)

boton_limpiar = Button(ventana, text="Limpiar", command=lambda: [id_entry.delete(0, END), nombre_catalogo_entry.delete(0, END), num_procesos_entry.delete(0, END)], font=("Arial", 12), bg="lightblue")
boton_limpiar.grid(row=5, column=1, columnspan=2, pady=10)

# p = Label(ventana, font=("Arial", 12))
# p.grid(row=6, column=0, pady=10)

ventana.mainloop()

