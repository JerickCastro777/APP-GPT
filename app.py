import os
from dotenv import load_dotenv
from resumen import Resumentexto
import tkinter as tk
from tkinter import ttk, messagebox

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave de API desde las variables de entorno
api_key = os.environ.get("OPENAI_API_KEY")

# Inicializar la clase Resumentexto con la clave de API
gpt_resumen = Resumentexto(api_key=api_key)

def generar_resumen():
    texto = texto_input.get("1.0", tk.END).strip()
    idioma = idioma_var.get()
    if not texto:
        messagebox.showerror("Error", "Por favor, introduce el texto a resumir.")
        return
    
    try:
        resumen = gpt_resumen.resumen(texto, idioma)
        resumen_output.delete("1.0", tk.END)
        resumen_output.insert(tk.END, resumen)
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

# Configurar la interfaz gráfica
root = tk.Tk()
root.title("Generador de Resúmenes")

# Crear widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

texto_label = ttk.Label(frame, text="Texto a resumir:")
texto_label.grid(row=0, column=0, sticky=tk.W)

texto_input = tk.Text(frame, width=60, height=15)
texto_input.grid(row=1, column=0, columnspan=2)

idioma_label = ttk.Label(frame, text="Idioma del resumen:")
idioma_label.grid(row=2, column=0, sticky=tk.W)

idioma_var = tk.StringVar(value="es")
idioma_entry = ttk.Entry(frame, textvariable=idioma_var)
idioma_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

generar_button = ttk.Button(frame, text="Generar Resumen", command=generar_resumen)
generar_button.grid(row=3, column=0, columnspan=2)

resumen_label = ttk.Label(frame, text="Resumen:")
resumen_label.grid(row=4, column=0, sticky=tk.W)

resumen_output = tk.Text(frame, width=60, height=15)
resumen_output.grid(row=5, column=0, columnspan=2)

# Configurar el estiramiento
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

# Ejecutar la aplicación
root.mainloop()
