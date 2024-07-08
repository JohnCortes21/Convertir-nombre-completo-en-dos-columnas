import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox

def show_info(output_path):
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    messagebox.showinfo("Documento Convertido", f"Proceso completado. Archivo guardado como '{output_path}'.")

# Llama a la función con la ruta de tu archivo
output_path = "ruta/al/archivo.txt"
show_info(output_path)

# Proporciona la ruta completa al archivo Excel
file_path = 'C:/Users/ADMIN/OneDrive - 816006449_LA INTEGRIDAD S.A/Escritorio/nombres.xlsx'

try:
    # Cargar el archivo Excel
    df = pd.read_excel(file_path)

    # Asumimos que el archivo tiene una columna llamada 'Nombre Completo'
    def dividir_nombre_apellido(nombre_completo):
        partes = nombre_completo.split()
        nombres = ' '.join(partes[-2:])
        apellidos = ' '.join(partes[:-2])
        return pd.Series([nombres, apellidos])

    # Aplicar la función de división a cada fila
    df[['Nombres', 'Apellidos']] = df['Nombre Completo'].apply(dividir_nombre_apellido)

    # Guardar el resultado en un nuevo archivo Excel
    output_path = 'C:/Users/ADMIN/OneDrive - 816006449_LA INTEGRIDAD S.A/Escritorio/nombres_divididos.xlsx'
    df.to_excel(output_path, index=False)

    print(f"Proceso completado. Archivo guardado como '{output_path}'.")

except FileNotFoundError:
    print(f"El archivo {file_path} no se encuentra.")
except Exception as e:
    print(f"Ha ocurrido un error: {e}")



