import json
import csv


def guardar_txt(producto):

    with open("inventario/data/datos.txt", "a") as f:
        linea = f"{producto['nombre']},{producto['cantidad']},{producto['precio']}\n"
        f.write(linea)


def leer_txt():

    productos = []

    with open("inventario/data/datos.txt", "r") as f:
        for linea in f:
            datos = linea.strip().split(",")

            productos.append({
                "nombre": datos[0],
                "cantidad": datos[1],
                "precio": datos[2]
            })

    return productos


def guardar_json(producto):

    archivo = "inventario/data/datos.json"

    try:
        with open(archivo,"r") as f:
            datos = json.load(f)
    except:
        datos = []

    datos.append(producto)

    with open(archivo,"w") as f:
        json.dump(datos,f,indent=4)


def leer_json():

    with open("inventario/data/datos.json","r") as f:
        return json.load(f)


def guardar_csv(producto):

    with open("inventario/data/datos.csv","a",newline="") as f:

        writer = csv.writer(f)

        writer.writerow([
            producto['nombre'],
            producto['cantidad'],
            producto['precio']
        ])


def leer_csv():

    productos = []

    with open("inventario/data/datos.csv","r") as f:

        reader = csv.reader(f)

        for fila in reader:

            productos.append({
                "nombre": fila[0],
                "cantidad": fila[1],
                "precio": fila[2]
            })

    return productos