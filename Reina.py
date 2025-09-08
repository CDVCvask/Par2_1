import tkinter as tk
class Reina:
    pass
class Jurado:
    pass
class Concurso_Reinas_app:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Reina")
        self.ventana.geometry("400x400")
        self.menu()
        self.ventana.mainloop()
    def menu(self):
        barra = tk.Menu(self.ventana)

