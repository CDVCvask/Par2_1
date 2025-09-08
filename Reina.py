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
    pass
class Mostrar_Reinas:
    def __init__(self):
        self.Reinas = []
        self.Jurados = []
    def Puntaje_Reinas(self,reina,jurado,cultura,proyeccion,entrevista):
        pass
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


