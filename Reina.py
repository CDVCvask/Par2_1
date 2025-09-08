import tkinter as tk
class Reina:
    def __init__(self,codigo,nombre,edad,insitucion,municipio):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad
        self.insitucion = insitucion
        self.municipio = municipio
        self.puntaje = 0
    #código, nombre, edad, institución educativa, municipio
class Jurado:
    def __init__(self,codigo,nombre,especialidad):
        self.codigo = codigo
        self.nombre = nombre
        self.especialidad = especialidad
        self.calificaciones = {}
class Mostrar_Reinas:
    def __init__(self):
        self.Reinas = []
        self.Jurados = []
    def Puntaje_Reinas(self,reina,jurado,cultura,proyeccion,entrevista):
        allow = 0
        allow2 = 0
        try:
            cultura = int(cultura)
            entrevista = int(entrevista)
            proyeccion = int(proyeccion)
        except ValueError:
            print("Tipo de dato ingresado no es valido")
        for Reina in self.Reinas:
            if Reina.codigo == reina:
                allow = 1
        for Jurado in self.Jurados:
            if Jurado.codigo == jurado:
                allow2 = 0
        if allow == 1 and allow2 == 1:
            if cultura >= 0 and cultura <= 10:
                if entrevista >= 0 and entrevista <= 10:
                    if proyeccion >= 0 and proyeccion <= 10:
                        promedio =  cultura + entrevista + proyeccion
                        promedio = promedio / 3
                        for Jurado in self.Jurados:
                            if Jurado.codigo == jurado:
                                Jurado.Calificaciones[reina] = {'Cultura':cultura,'Entrevista':entrevista,'Proyeccion':proyeccion,'Promedio':promedio}
        else:
            print("El codigo de la reina o el jurado no es valido")
    def Calificacion(self):
        total = 0
        for Reina in self.Reinas:
            for code,value in Jurado.calificaciones.items():
                if Reina.codigo == code:
                    total = total + value['Promedio']
            Reina.puntaje = total
    def Ordenar_Reinas(self,reinas):
        if len(reinas) <= 1:
            return reinas
        low = []
        same = []
        high = []
        piv = 0
        for Reina in reinas:
            piv = Reina.puntaje
            break
        for Reina in reinas:
            if Reina.puntaje < piv:
                low.append(Reina)
            if Reina.puntaje > piv:
                high.append(Reina)
            if Reina.puntaje == piv:
                same.append(Reina)
        return self.Ordenar_Reinas(high) + same + self.Ordenar_Reinas(low)
    def Agregar_Reina(self,reina):
        if reina in self.Reinas:
            print("Esta reina ya existe")
        else:
            self.Reinas.append(reina)
    def Agregar_Jurado(self,jurado):
        if jurado in self.Jurados:
            print("Esta jurado ya existe")
        else:
            self.Jurados.append(jurado)
contR= 0
contJ = 0
mos = Mostrar_Reinas()
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
        opciones.add_command(label="Mostrar candidatas", command=self.Mostrar_candidatas)
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
        codeR = f"R{contR}"
        registrar = tk.Button(inscribir_ventana, text="REGISTRAR", font=("Arial", 12, "bold"), command=lambda: self.inscribir(codeR,nombre_entrada.get(),edad_entrada.get(),insti_entrada.get(),muni_entrada.get()))
        #contR = contR + 1
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
    def Mostrar_candidatas(self):
        mostar_ventana = tk.Tk()
        mostar_ventana.title("Mostrar candidatas")
        mostar_ventana.geometry("600x400")
        #listas = tk.Listbox(mostar_ventana)
        #listas.grid(row=0, column=2, padx=5, pady=5)
        titulo=tk.Label(mostar_ventana, text="Mostrar candidatas", font=("Arial", 16, "bold"))
        titulo.grid(row=0, column=0, pady=10)
        x=1
        for reina in mos.Reinas:
            candidata=tk.Label(mostar_ventana, text=f"{reina.nombre}", font=("Arial", 12))
            candidata.grid(row=x, column=1, pady=10)
            x=x+1
    def Inscribir_Jurado(self):
        inscribir_ventana = tk.Tk()
        inscribir_ventana.title("Inscripcion de jurado")
        inscribir_ventana.geometry("600x400")
        titulo = tk.Label(inscribir_ventana, text="Inscripcion de Jurado", font=("Arial", 16, "bold"))
        nombre = tk.Label(inscribir_ventana, text="Ingrese el nombre del Jurado: ", font=("Arial", 12))
        nombre_entrada = tk.Entry(inscribir_ventana, font=("Arial", 12))
        especialidad = tk.Label(inscribir_ventana, text="Ingrese la especialidad del Jurado: ", font=("Arial", 12))
        especialidad_entrada = tk.Entry(inscribir_ventana, font=("Arial", 12))
        registar = tk.Button(inscribir_ventana,text="Registar",command =lambda:self.Inscribir_Jurado())
    def inscribir_Reina(self,codigo, nombre, edad, insti, municipio):
        x = tk.Tk()
        x.title("Registrando")
        edad = int(edad)
        nuevaCandidata = Reina(codigo,nombre,edad,insti,municipio)
        mos.Agregar_Reina(nuevaCandidata)
        x.destroy()
    def Inscribir_Jurado(self,codigo,nombre,especialidad):
        x = tk.Tk()
        pass
concurso = Concurso_Reinas_app()


