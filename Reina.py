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
                allow2 = 1
        if allow == 1 and allow2 == 1:
            if cultura >= 0 and cultura <= 10:
                if entrevista >= 0 and entrevista <= 10:
                    if proyeccion >= 0 and proyeccion <= 10:
                        promedio =  cultura + entrevista + proyeccion
                        promedio = promedio / 3
                        for Jurado in self.Jurados:
                            if Jurado.codigo == jurado:
                                Jurado.calificaciones[reina] = {'Cultura':cultura,'Entrevista':entrevista,'Proyeccion':proyeccion,'Promedio':promedio}
        else:
            print("El codigo de la reina o el jurado no es valido")
    def Calificacion(self):
        total = 0
        for Reina in self.Reinas:
            for jurado in self.Jurados:
                for code,value in jurado.calificaciones.items():
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
global contR
global contJ
contR = 0
contJ = 0
mos = Mostrar_Reinas()
class Concurso_Reinas_app:
    def __init__(self):
        self.contR = 0
        self.contJ = 0
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
        opciones.add_command(label="Registrar jurado", command=self.Inscribir_Jurado)
        opciones.add_command(label="Registrar evaluacion", command=self.ingresar_evaluacion)
        opciones.add_command(label="Mostrar candidatas", command=self.Mostrar_candidatas)
        opciones.add_command(label="Ranking", command=self.ranking)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)

    def inscribir_candidata(self):
        global contR
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
        codeR = f"R{self.contR}"
        self.contR = self.contR + 1
        registrar = tk.Button(inscribir_ventana, text="REGISTRAR", font=("Arial", 12, "bold"),
                              command=lambda: self.inscribir_Reina(codeR,nombre_entrada.get(),edad_entrada.get(),insti_entrada.get(),muni_entrada.get()))
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
        #for reina in mos.Reinas:
            #candidata=tk.Label(mostar_ventana, text=f"{reina.nombre}", font=("Arial", 12))
            #candidata.grid(row=x, column=1, pady=10)
            #x=x+1
        for reina in mos.Reinas:
            Reina = tk.Label(mostar_ventana, text=f"{reina.nombre}--{reina.codigo}", font=("Arial", 12))
            Reina.grid(row=x, column=1, pady=10)
            x=x+1
    def Inscribir_Jurado(self):
        global contJ
        inscribir_ventana = tk.Tk()
        inscribir_ventana.title("Inscripcion de jurado")
        inscribir_ventana.geometry("600x400")
        titulo = tk.Label(inscribir_ventana, text="Inscripcion de Jurado", font=("Arial", 16, "bold"))
        nombre = tk.Label(inscribir_ventana, text="Ingrese el nombre del Jurado: ", font=("Arial", 12))
        nombre_entrada = tk.Entry(inscribir_ventana, font=("Arial", 12))
        especialidad = tk.Label(inscribir_ventana, text="Ingrese la especialidad del Jurado: ", font=("Arial", 12))
        especialidad_entrada = tk.Entry(inscribir_ventana, font=("Arial", 12))
        codigo_J = f"J{self.contJ}"
        self.contJ = self.contJ + 1
        registar = tk.Button(inscribir_ventana,text="Registar",font=("Arial", 12),command =lambda:self.registrar_jurado(codigo_J,nombre_entrada.get(), especialidad_entrada.get()))


        titulo.grid(row=0, column=2, pady=10)
        nombre.grid(row=1, column=1, pady=10)
        nombre_entrada.grid(row=1, column=2, pady=10)
        especialidad.grid(row=2, column=1, pady=10)
        especialidad_entrada.grid(row=2, column=2, pady=10)
        registar.grid(row=3, column=2, pady=10)

    def inscribir_Reina(self,codigo, nombre, edad, insti, municipio):
        x = tk.Tk()
        x.title("Registrando")
        edad = int(edad)
        nuevaCandidata = Reina(codigo,nombre,edad,insti,municipio)
        mos.Agregar_Reina(nuevaCandidata)
        x.destroy()
    def registrar_jurado(self,codigo,nombre,especialidad):
        x = tk.Tk()
        x.title("Registrando")
        nuevo_jurado = Jurado(codigo,nombre,especialidad)
        mos.Agregar_Jurado(nuevo_jurado)
        x.destroy()
    def ingresar_evaluacion(self):
        ventana_evaluacion = tk.Tk()
        ventana_evaluacion.title("Evaluacion")
        ventana_evaluacion.geometry("650x400")
        titulo = tk.Label(ventana_evaluacion, text="Evaluacion de la Reina.", font=("Arial", 14,"bold"))
        codReina = tk.Label(ventana_evaluacion, text="Ingrese el codigo de la reina para evaluarla: ", font=("Arial", 12))
        codReina_entrada= tk.Entry(ventana_evaluacion,font=("Arial", 12))
        codJurado=tk.Label(ventana_evaluacion, text="Ingrese el codigo del jurado que evalúa: ", font=("Arial", 12))
        codJurado_entrada=tk.Entry(ventana_evaluacion,font=("Arial", 12))
        subtitulo=tk.Label(ventana_evaluacion, text="Ingresando la evaluacion.", font=("Arial", 14, "bold"))
        cultura=tk.Label(ventana_evaluacion, text="Puntuacion Cultura: ", font=("Arial", 12))
        cultura_entrada=tk.Entry(ventana_evaluacion,font=("Arial", 12))
        entrevista=tk.Label(ventana_evaluacion, text="Puntuacion Entrevista: ", font=("Arial", 12))
        entrevista_entrada=tk.Entry(ventana_evaluacion,font=("Arial", 12))
        proyeccion=tk.Label(ventana_evaluacion, text="Puntuacion Proyeccion: ", font=("Arial", 12))
        proyeccion_entrada=tk.Entry(ventana_evaluacion,font=("Arial", 12))
        registrar=tk.Button(ventana_evaluacion, text="Registrar evaluacion", font=("Arial", 12),
        command=lambda: self.registrar_evaluacion(codReina_entrada.get(), codJurado_entrada.get(), cultura_entrada.get(), entrevista_entrada.get(),proyeccion_entrada.get()))

        titulo.grid(row=0, column=2, pady=10)
        codReina.grid(row=1, column=1, pady=10)
        codReina_entrada.grid(row=1, column=2, pady=10)
        codJurado.grid(row=2, column=1, pady=10)
        codJurado_entrada.grid(row=2, column=2, pady=10)
        subtitulo.grid(row=3, column=2, pady=10)
        cultura.grid(row=4, column=1, pady=10)
        cultura_entrada.grid(row=4, column=2, pady=10)
        entrevista.grid(row=5, column=1, pady=10)
        entrevista_entrada.grid(row=5, column=2, pady=10)
        proyeccion.grid(row=6, column=1, pady=10)
        proyeccion_entrada.grid(row=6, column=2, pady=10)
        registrar.grid(row=7, column=2, pady=10)

    def registrar_evaluacion(self,codReina,codJurado,cultura,entrevista,proyeccion):
        x = tk.Tk()
        x.title("Registrar evaluacion")
        mos.Puntaje_Reinas(codReina,codJurado,cultura,proyeccion,entrevista)
        x.destroy()

    def ranking(self):
        ventana_ranking = tk.Tk()
        ventana_ranking.title("Ranking")
        ventana_ranking.geometry("600x500")
        rankingDeReinas= mos.Ordenar_Reinas(mos.Reinas)
        titulo= tk.Label(ventana_ranking, text="Ranking de las reinas.", font=("Arial", 16, "bold"))
        primerLugar= tk.Label(ventana_ranking, text="PRIMER LUGAR.", font=("Arial", 14, "bold"), fg="#cfa959")
        segundoLugar=tk.Label(ventana_ranking, text="SEGUNDO LUGAR.", font=("Arial", 14, "bold"), fg="#939694")
        tercerLugar=tk.Label(ventana_ranking, text="TERCER LUGAR.", font=("Arial", 14, "bold"), fg="#bf8970")
        todas=tk.Label(ventana_ranking, text="El resto de participantes.", font=("Arial", 14, "bold"))

        titulo.grid(row=0, column=2, pady=10)
        primerLugar.grid(row=1, column=2, pady=10)
        contador= 0
        for reina in rankingDeReinas:
            lugar=tk.Label(ventana_ranking, text=f"{reina.nombre}", font=("Arial", 13, "bold"))
            lugar.grid(row=2, column=2, pady=10)
            break
        segundoLugar.grid(row=3, column=1, pady=10)
        for reina in rankingDeReinas:
            if contador == 1:
                lugar= tk.Label(ventana_ranking, text=f"{reina.nombre}", font=("Arial", 12, "bold"))
                lugar.grid(row=4, column=1, pady=10)
                break
            else:
                contador=1
        tercerLugar.grid(row=5, column=3, pady=10)
        contador = 0
        for reina in rankingDeReinas:
            if contador == 2:
                lugar=tk.Label(ventana_ranking,text=f"{reina.nombre}", font=("Arial", 11, "bold"))
                lugar.grid(row=6, column=3, pady=10)
            else:
                contador+=1
        todas.grid(row=7, column=2, pady=10)
        contador = 0
        x=4
        for reina in rankingDeReinas:
            if contador == 3:
                lugar=tk.Label(ventana_ranking,text=f"{x}. {reina.nombre}", font=("Arial", 10, "bold"))
                lugar.grid(row=x+4, column=2, pady=10)
                x=x+1
            else:
                contador+=1


contR = contR + 1
contJ = contJ + 1
concurso = Concurso_Reinas_app()


