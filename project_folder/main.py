import re
import tkinter as tk
from tkinter import scrolledtext, PhotoImage
from tkinter import ttk
import pyperclip


# Definir la función analizador_lexicográfico
def analizador_lexicografico(cadena):
  with open('diccionario_espanol.txt', 'r', encoding="utf-8") as f:
    diccionario = set(f.read().split())
    
  emoticones = re.findall(r'(:-?[\(\)DdPpO|/*]|;-?[\)]|<3|\\m/|\(y\)|\(n\)|\^\^|>:|:-S|:p|=:o\)|\(-\.-\)|:r\]|\|\|//\||8-nn|S//S|:o\)|:SS|<<>>|XD|:3p1|:3p2|:3p3|:3p4)', cadena)
  palabras_espanol = re.findall(r'\b[a-zA-ZáéíóúüÁÉÍÓÚÜñÑ]+\b', cadena)
  

  num_palabras_espanol = sum(1 for palabra in palabras_espanol
                             if palabra.lower() in diccionario)
  num_emoticones = len(emoticones)

  return cadena, num_palabras_espanol, num_emoticones, emoticones


# Diccionario de emojis
emoticones_dict = {
    "8-)": "002-emoticonos.png",
    ":-]": "003-feliz.png",
    ":-O": "004-conmocionado.png",
    ":-D": "005-sonriente.png",
    ":-)": "006-feliz-1.png",
    ":-/": "007-pensando.png",
    "o_O": "008-confuso.png",
    ":(": "009-triste.png",
    ":D": "010-risa.png",
    ":( - 011-triste-1.png": ":-o",
    ":S": "013-preocuparse.png",
    ":)": "014-sonrisa.png",
    "(_)": "016-estrella.png",
    "^_^": "017-partido.png",
    ";)": "018-guino.png",
    "?_?": "019-entusiasta.png",
    "<:o)": "021-cabeza-alienigena.png",
    "=^_^=": "022-gato.png",
    ":-S": "023-cabeza-alienigena-1.png",
    "zzz": "024-emoji-2.png",
    "8-nn": "025-nerd.png",
    "S//S": "026-superhombre.png",
    ":o)": "030-payaso.png",
    ":-": "033-pensando-1.png",
    ":p": "034-relamerse.png",
    "=:o": "038-sonriente-1.png",
    "(-.-)": "039-orar.png",
    ":r]": "040-robot.png",
    ":3]": "041-robot-1.png",
    ":->": "042-enfermo.png",
    ":Dm": "043-mano.png",
    "(n)": "046-pulgares-abajo-1.png",
    ":-E": "049-fantasma-1.png",
    "<3": "050-enamorado.png",
    "@_@": "053-mareado.png",
    ":SS": "054-pensar.png",
    "<<>>": "056-caca.png",
    "XD": "058-riendo.png",
    ":3p": "060-perro.png",
    ":3p2": "061-perro-1.png",
    ":3p3": "064-perro-4.png",
    ":3p4": "065-perro-5.png",
}


def create_gui():
  window = tk.Tk()
  window.title("Analizador Lexicográfico")

  logo_path = "logo_eafit_completo.png"
  logo_img = PhotoImage(file=logo_path).subsample(2)
  logo_label = tk.Label(window, image=logo_img)
  logo_label.image = logo_img
  logo_label.grid(row=0, column=0, padx=10, pady=10, rowspan=2)

  titulo_label = tk.Label(
      window,
      text="UNIVERSIDAD EAFIT\nPROYECTO FINAL\nLENGUAJES DE PROGRAMACION",
      font=("Arial", 15, "bold"))
  titulo_label.grid(row=0, column=1, padx=10, pady=10)

  input_label = tk.Label(window,
                         text="Ingrese un texto:",
                         font=("Tahoma", 14, "bold"))
  input_label.grid(row=2, column=0, padx=10, pady=5)

  input_text = scrolledtext.ScrolledText(window,
                                         width=40,
                                         height=1,
                                         wrap=tk.WORD,
                                         font=("Tahoma", 14, "bold"))
  input_text.grid(row=3, column=0, padx=10, pady=5, rowspan=2)

  output_label = tk.Label(window, text="Salida:", font=("Tahoma", 14, "bold"))
  output_label.grid(row=5, column=0, padx=10, pady=5)

  output_frame = tk.Frame(window, width=400)
  output_frame.grid(row=6, column=0, padx=10, pady=5)

  def process_text():
    cadena = input_text.get('1.0', tk.END)
    resultado, num_palabras_espanol, num_emoticones, emoticones = analizador_lexicografico(
        cadena)

    parts = re.split(
      r'(:-?[\(\)DdPpO|/*]|;-?[\)]|<3|\\m/|\(y\)|\(n\)|\^\^|>:|:-S|:p|=:o\)|\(-\.-\)|:r\]|\|\|//\||8-nn|S//S|:o\)|:SS|<<>>|XD|:3p1|:3p2|:3p3|:3p4)',
        resultado)
    column_index = 0

    # Eliminar la salida si hay contenido
    if len(output_frame.winfo_children()) > 0:
      for widget in output_frame.winfo_children():
        widget.destroy()

    for part in parts:
      if part in emoticones_dict:
        emoji_path = f"png/{emoticones_dict[part]}"
        emoji_img = PhotoImage(file=emoji_path).subsample(13, 13)
        emoji_label = tk.Label(output_frame, image=emoji_img)
        emoji_label.image = emoji_img
        emoji_label.grid(row=0, column=column_index, padx=2, pady=2)
        column_index += 1
      else:
        text_label = tk.Label(output_frame,
                              text=part,
                              font=("Courier New", 18, "bold"))
        text_label.grid(row=0, column=column_index, padx=2, pady=2)
        column_index += 1

    palabras_espanol_label = tk.Label(
        window,
        text=f"Palabras identificadas: {num_palabras_espanol}",
        font=("Times New Roman", 15, "bold"))
    palabras_espanol_label.grid(row=7, column=0, padx=10, pady=5)

    emoticones_label = tk.Label(
        window,
        text=f"Emoticones identificados: {num_emoticones}",
        font=("Times New Roman", 15, "bold"))
    emoticones_label.grid(row=8, column=0, padx=10, pady=5)

  style = ttk.Style()
  style.configure('Custom.TButton', font=('Courier New', 13, 'bold'))

  process_button = ttk.Button(window,
                              text="Procesar cadena de texto",
                              command=process_text,
                              style='Custom.TButton')
  process_button.grid(row=3,
                      column=1,
                      padx=10,
                      pady=5,
                      rowspan=2,
                      sticky='nsew')
  process_button.config(width=20)

  window.mainloop()


# Llamar a la función para crear la interfaz gráfica
create_gui()
