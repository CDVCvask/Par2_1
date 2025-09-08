import tkinter as tk


class Reina:
    def __init__(self, nombre, edad, insitucion, municipio):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad
        self.insitucion = insitucion
        self.municipio = municipio

    # código, nombre, edad, institución educativa, municipio
    pass


class Jurado:
    pass


class Concurso_Reinas_app:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Reina")
        self.ventana.geometry("400x400")
        self.menu()
        self.titulo = tk.Label(self.ventana, text="Reina")
        self.titulo.place(x=100, y=100)
        self.ventana.mainloop()

    def menu(self):
        barra = tk.Menu(self.ventana)
        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(label="Registrar candidata.", command=self.inscribir_candidata)
        opciones.add_command(label="Registrar jurado", command=self.ventana.destroy)
        opciones.add_command(label="Registrar evaluacion", command=self.ventana.destroy)
        opciones.add_command(label="Mostrar candidatas", command=self.ventana.destroy)
        opciones.add_command(label="Ranking", command=self.ventana.destroy)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)

    def inscribir_candidata(self):
        inscribir_ventana = tk.Tk()
        inscribir_ventana.title("Inscripcion de candidata")
        inscribir_ventana.geometry("600x400")

        titulo = tk.Label(inscribir_ventana, text="Inscripcion de candidata", font=("Arial", 16, "bold"))
        nombre = tk.Label(inscribir_ventana, text="Ingrese el nombre de la candidata: ", font=("Arial", 12))
        nombre_entrada = tk.Entry(inscribir_ventana, font=("Arial", 12))
        edad = tk.Label(inscribir_ventana, text="Ingrese la edad de la candidata: ", font=("Arial", 12))
        edad_entrada = tk.Entry(inscribir_ventana, font=("Arial", 12))
        insti = tk.Label(inscribir_ventana, text="Ingrese la institucion del candidata: ", font=("Arial", 12))
        insti_entrada = tk.Entry(inscribir_ventana, font=("Arial", 12))
        muni = tk.Label(inscribir_ventana, text="Ingrse el municipio del candidata: ", font=("Arial", 12))
        muni_entrada = tk.Entry(inscribir_ventana, font=("Arial", 12))
        registrar = tk.Button(inscribir_ventana, text="REGISTRAR", font=("Arial", 12, "bold"), command=lambda: self.inscribir_candidata(nombre_entrada.get(),edad_entrada.get(),insti_entrada.get(),muni_entrada.get()))

        titulo.grid(row=0, column=2, pady=10)
        nombre.grid(row=1, column=1, pady=10)
        nombre_entrada.grid(row=1, column=2, pady=10)
        edad.grid(row=2, column=1, pady=10)
        edad_entrada.grid(row=2, column=2, pady=10)
        insti.grid(row=3, column=1, pady=10)
        insti_entrada.grid(row=3, column=2, pady=10)
        muni.grid(row=4, column=1, pady=10)
        muni_entrada.grid(row=4, column=2, pady=10)
        registrar.grid(row=5, column=2, pady=10)

    def inscribir(self, nombre, edad, insti, municipio):
        x = tk.Tk()
        x.title("Registrando")
        edad = int(edad)
        nuevaCandidata = Reina(nombre,edad,insti,municipio)



concurso = Concurso_Reinas_app()