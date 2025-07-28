import tkinter as tk
from PIL import Image, ImageTk
import os

# Crear ventana principal
root = tk.Tk()
root.title("Galería de carpetas")
root.geometry("600x500")

# Carpeta base
carpeta_base = "imagenes"

# Crear si no existe
if not os.path.exists(carpeta_base):
    os.makedirs(carpeta_base)

# Listbox con carpetas
listbox = tk.Listbox(root)
listbox.place(x=20, y=20, width=200, height=150)

# Frame para las imágenes
labels_imagenes = []

for i in range(4):
    lbl = tk.Label(root, text=f"Imagen {i+1}", bg="lightgray", width=15, height=8)
    lbl.place(x=250 + (i % 2) * 120, y=20 + (i // 2) * 120)
    labels_imagenes.append(lbl)

# Cargar carpetas

def cargar_carpetas():
    listbox.delete(0, tk.END)
    carpetas = [f for f in os.listdir(carpeta_base) if os.path.isdir(os.path.join(carpeta_base, f))]
    for carpeta in carpetas:
        listbox.insert(tk.END, carpeta)

# Mostrar imágenes de carpeta seleccionada

def mostrar_imagenes(event):
    seleccion = listbox.curselection()
    if not seleccion:
        return
    carpeta = listbox.get(seleccion[0])
    ruta_carpeta = os.path.join(carpeta_base, carpeta)

    imagenes = [f for f in os.listdir(ruta_carpeta) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    imagenes.sort()

    for i in range(4):
        lbl = labels_imagenes[i]
        if i < len(imagenes):
            img_path = os.path.join(ruta_carpeta, imagenes[i])
            img = Image.open(img_path).resize((100, 100))
            img_tk = ImageTk.PhotoImage(img)
            lbl.config(image=img_tk, text="")
            lbl.image = img_tk
        else:
            lbl.config(image="", text="(vacío)", bg="lightgray")

# Asociar evento
listbox.bind("<<ListboxSelect>>", mostrar_imagenes)

# Cargar carpetas al iniciar
cargar_carpetas()

root.mainloop()
