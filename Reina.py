import tkinter as tk
class Reina:
    def __init__(self,codigo,nombre,edad,insitucion,municipio):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad
        self.insitucion = insitucion
        self.municipio = municipio
    #código, nombre, edad, institución educativa, municipio
class Jurado:
    def __init__(self,codigo,nombre,especialidad):
        self.codigo = codigo
        self.nombre = nombre
        self.especialidad = especialidad
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
        else:
            print("El codigo de la reina o el jurado no es valido")
    def Agregar_Reina(self,reina):
        self.Reinas.append(reina)
    def Agregar_Jurado(self,jurado):
        self.Jurados.append(jurado)
class Concurso_Reinas_app:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Reina")
        self.ventana.geometry("400x400")
        self.menu()
        self.titulo = tk.Label(self.ventana, text="Reina")
        self.titulo.place(x= 100, y=100)
        self.ventana.mainloop()
    def menu(self):
        barra = tk.Menu(self.ventana)


