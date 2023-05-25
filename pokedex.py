import requests
import tkinter as tk
from io import BytesIO


def obtener_informacion_pokemon(numero):
    url = f"https://pokeapi.co/api/v2/pokemon/{numero}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        nombre = datos['name']
        tipos = [tipo['type']['name'] for tipo in datos['types']]
        habilidades = [habilidad['ability']['name'] for habilidad in datos['abilities']]
        altura = datos['height']
        peso = datos['weight']
        imagen_url = datos['sprites']['front_default']

        resultado_text.delete(1.0, tk.END)  # Limpiar el contenido anterior
        resultado_text.insert(tk.END, f"Nombre: {nombre}\n")
        resultado_text.insert(tk.END, f"Tipo(s): {', '.join(tipos)}\n")
        resultado_text.insert(tk.END, f"Habilidades: {', '.join(habilidades)}\n")
        resultado_text.insert(tk.END, f"Altura: {altura} dm\n")
        resultado_text.insert(tk.END, f"Peso: {peso} hg\n")

        # Descargar la imagen del Pokémon
        response = requests.get(imagen_url)
        imagen_binaria = response.content

        # Mostrar la imagen en la ventana
        imagen = tk.PhotoImage(data=imagen_binaria)
        etiqueta_imagen.config(image=imagen)
        etiqueta_imagen.image = imagen
    else:
        resultado_text.delete(1.0, tk.END)  # Limpiar el contenido anterior
        resultado_text.insert(tk.END, "No se pudo obtener la información del Pokémon.")


def buscar_pokemon():
    numero_pokemon = entrada.get()
    obtener_informacion_pokemon(numero_pokemon)


# Crear la ventana de la interfaz de usuario
ventana = tk.Tk()
ventana.title("Pokédex")

# Crear un campo de entrada para el número del Pokémon
etiqueta = tk.Label(ventana, text="Número del Pokémon:")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

# Crear un botón para buscar el Pokémon
boton_buscar = tk.Button(ventana, text="Buscar", command=buscar_pokemon)
boton_buscar.pack()

# Crear una etiqueta para mostrar la imagen
etiqueta_imagen = tk.Label(ventana)
etiqueta_imagen.pack()

# Crear un widget Text para mostrar los resultados
resultado_text = tk.Text(ventana, height=10, width=50)
resultado_text.pack()

ventana.mainloop()
