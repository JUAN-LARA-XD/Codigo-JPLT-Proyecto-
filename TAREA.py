import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk  
import math
import random
# Funciones para calcular áreas
def calcula_area_cuadrado():
    lado = float(entrada_cuadrado.get())
    area = lado ** 2
    resultado_area.config(text=f"Área del cuadrado: {area:.2f}")
def calcula_area_rectangulo():
    lado1 = float(entrada_rectangulo1.get())
    lado2 = float(entrada_rectangulo2.get())
    area = lado1 * lado2
    resultado_area.config(text=f"Área del rectángulo: {area:.2f}")
def calcula_area_triangulo():
    base = float(entrada_triangulo_base.get())
    altura = float(entrada_triangulo_altura.get())
    area = (base * altura) / 2
    resultado_area.config(text=f"Área del triángulo: {area:.2f}")
def calcula_area_circulo():
    radio = float(entrada_circulo.get())
    area = math.pi * radio ** 2
    resultado_area.config(text=f"Área del círculo: {area:.2f}")
def calcula_area_poligono():
    lado = float(entrada_poligono_lado.get())
    n_lados = int(entrada_poligono_n_lados.get())
    apotema = float(entrada_poligono_apotema.get())
    perimetro = lado * n_lados
    area = (perimetro * apotema) / 2
    resultado_area.config(text=f"Área del polígono: {area:.2f}")
# Función para actualizar las entradas según la selección del ComboBox
def actualizar_tipo_area(event):
    seleccion = combo_tipo_area.get()
    # Ocultar todos los frames
    for frame in frames_areas:
        frame.pack_forget()
    # Mostrar el frame correspondiente a la selección
    if seleccion == "Cuadrado":
        frame_cuadrado.pack(pady=5)
    elif seleccion == "Rectángulo":
        frame_rectangulo.pack(pady=5)
    elif seleccion == "Triángulo":
        frame_triangulo.pack(pady=5)
    elif seleccion == "Círculo":
        frame_circulo.pack(pady=5)
    elif seleccion == "Polígono":
        frame_poligono.pack(pady=5)
# Crear ventana principal con tema
window = ThemedTk(theme="black")
window.title("Calculadora de Áreas, Calculadora y Num. Aleatorios")
# Crear Notebook para tener diferentes pestañas
notebook = ttk.Notebook(window)
notebook.pack(pady=10, expand=True)
# Crear pestañas
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
frame4 = ttk.Frame(notebook)
# Agregar pestañas al Notebook
notebook.add(frame1, text='Cálculo de Áreas')
notebook.add(frame2, text='Calculadora')
notebook.add(frame3, text='Num. Aleatorios')
notebook.add(frame4, text='Equipo')
# ComboBox para seleccionar tipo de área
ttk.Label(frame1, text="Selecciona el tipo de área:").pack(pady=5)
combo_tipo_area = ttk.Combobox(frame1, values=["Cuadrado", "Rectángulo", "Triángulo", "Círculo", "Polígono"])
combo_tipo_area.pack(pady=5)
combo_tipo_area.bind("<<ComboboxSelected>>", actualizar_tipo_area)
# Crear frames para cada tipo de área
frame_cuadrado = ttk.Frame(frame1)
ttk.Label(frame_cuadrado, text="Lado del Cuadrado:").pack(pady=5)
entrada_cuadrado = ttk.Entry(frame_cuadrado)
entrada_cuadrado.pack(pady=5)
ttk.Button(frame_cuadrado, text="Calcular", command=calcula_area_cuadrado).pack(pady=5)
frame_rectangulo = ttk.Frame(frame1)
ttk.Label(frame_rectangulo, text="Lado 1 del Rectángulo:").pack(pady=5)
entrada_rectangulo1 = ttk.Entry(frame_rectangulo)
entrada_rectangulo1.pack(pady=5)
ttk.Label(frame_rectangulo, text="Lado 2 del Rectángulo:").pack(pady=5)
entrada_rectangulo2 = ttk.Entry(frame_rectangulo)
entrada_rectangulo2.pack(pady=5)
ttk.Button(frame_rectangulo, text="Calcular", command=calcula_area_rectangulo).pack(pady=5)
frame_triangulo = ttk.Frame(frame1)
ttk.Label(frame_triangulo, text="Base del Triángulo:").pack(pady=5)
entrada_triangulo_base = ttk.Entry(frame_triangulo)
entrada_triangulo_base.pack(pady=5)
ttk.Label(frame_triangulo, text="Altura del Triángulo:").pack(pady=5)
entrada_triangulo_altura = ttk.Entry(frame_triangulo)
entrada_triangulo_altura.pack(pady=5)
ttk.Button(frame_triangulo, text="Calcular", command=calcula_area_triangulo).pack(pady=5)
frame_circulo = ttk.Frame(frame1)
ttk.Label(frame_circulo, text="Radio del Círculo:").pack(pady=5)
entrada_circulo = ttk.Entry(frame_circulo)
entrada_circulo.pack(pady=5)
ttk.Button(frame_circulo, text="Calcular", command=calcula_area_circulo).pack(pady=5)
frame_poligono = ttk.Frame(frame1)
ttk.Label(frame_poligono, text="Lado del Polígono:").pack(pady=5)
entrada_poligono_lado = ttk.Entry(frame_poligono)
entrada_poligono_lado.pack(pady=5)
ttk.Label(frame_poligono, text="Número de Lados:").pack(pady=5)
entrada_poligono_n_lados = ttk.Entry(frame_poligono)
entrada_poligono_n_lados.pack(pady=5)
ttk.Label(frame_poligono, text="Apotema del Polígono:").pack(pady=5)
entrada_poligono_apotema = ttk.Entry(frame_poligono)
entrada_poligono_apotema.pack(pady=5)
ttk.Button(frame_poligono, text="Calcular", 
           command=calcula_area_poligono).pack(pady=5)
# Guardar todos los frames en una lista
frames_areas = [frame_cuadrado, frame_rectangulo, frame_triangulo, frame_circulo, frame_poligono]
# Mostrar el resultado
resultado_area = ttk.Label(frame1, text="")
resultado_area.pack(pady=10)





# Elementos en el frame de la calculadora
entrada_calculadora = ttk.Entry(frame2, font=("Arial", 24), justify='right')
entrada_calculadora.grid(row=0, column=0, columnspan=4, pady=10)

# Botones de la calculadora
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]
def on_Button_click(char) :
    if char == 'C':
        entrada_calculadora.delete(0, tk.END)
    elif char == '=':
        try:
            resultado = str(eval(entrada_calculadora.get()))
            entrada_calculadora.delete(0, tk.END)
            entrada_calculadora.insert(0, resultado)
        except Exception:
            entrada_calculadora.delete(0, tk.END)
            entrada_calculadora.insert(0, "Error")
    else:
        entrada_calculadora.insert(tk.END, char)
# Crear botones de la calculadora
for (text, row, column) in botones:
    button = ttk.Button(frame2, text=text, command=lambda t=text:on_Button_click (t))
    button.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)

# Configurar filas y columnas de la calculadora
for i in range(5):
    frame2.grid_rowconfigure(i, weight=1)
for i in range(4):
    frame2.grid_columnconfigure(i, weight=1)

    
# Función para generar un número aleatorio
def generar_numero():
    numero = random.randint(1, 100)
    resultado_aleatorio.config(text=str(numero))
    


# Botón para generar el número

ttk.Button (frame3, text = "Generar Número", command= generar_numero).pack(pady=5)
resultado_aleatorio = ttk.Label(frame3, text="")
resultado_aleatorio.pack(pady=20)


from PIL import Image, ImageTk

# Crear la ventana principal

window.geometry("400x670")



# Cargar la imagen (debe estar en la misma carpeta o indicar la ruta completa)
imagen = Image.open("Equipo.jpeg")  # Cambia "ruta_de_tu_imagen.jpg" por la imagen que quieras usar
imagen = imagen.resize((200, 200), Image.Resampling.LANCZOS)  # Redimensionar la imagen si es necesario
imagen_tk = ImageTk.PhotoImage(imagen)

# Crear un widget label y colocar la imagen
label_imagen = tk.Label(frame4, image=imagen_tk)
label_imagen.pack(pady=20)


# Datos de los integrantes
integrantes = [
    {"nombre": "Juan Pablo Lara Tlahuice", "matricula": "231403038", "numero_lista": "8"},
    {"nombre": "Christian Gavilan Chapulin", "matricula": "231403033", "numero_lista": "7"},
    {"nombre": "Juan Carlos Pineda Soriano", "matricula": "231503048 ", "numero_lista": "18"},
    {"nombre": "Yhair Antonio Toxqui Coyotecalt", "matricula": "231403074", "numero_lista": "24"}
]



# Crear las etiquetas con la información de cada integrante
for integrante in integrantes:
    label_nombre = ttk.Label(frame4, text=f"Nombre: {integrante['nombre']}")
    label_nombre.pack(pady=5)
    
    label_matricula = ttk.Label(frame4, text=f"Matrícula: {integrante['matricula']}")
    label_matricula.pack(pady=5)
    
    label_numero_lista = ttk.Label(frame4, text=f"Número de lista: {integrante['numero_lista']}")
    label_numero_lista.pack(pady=5)
    
    
# Agregar el frame al notebook y mostrar la ventana
notebook.add(frame4, text="Integrantes")
notebook.pack(expand=True, fill="both")






ttk.Button (frame4, text = "Quit", command= window.destroy).pack()

# Ejecutar el bucle principal
window.mainloop()
