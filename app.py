from flask import Flask, render_template, request, redirect
from inventario.bd import Base, engine, SessionLocal
from inventario.productos import Producto
from inventario.inventario import guardar_txt, guardar_json, guardar_csv
from inventario.inventario import leer_txt, leer_json, leer_csv

from Conexion.conexion import conectar

app = Flask(__name__)

# Crear tablas SQLite
Base.metadata.create_all(engine)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/productos')
def productos():

    db = SessionLocal()
    productos = db.query(Producto).all()
    db.close()

    return render_template("productos.html", productos=productos)


@app.route('/producto/nuevo', methods=['GET','POST'])
def nuevo_producto():

    if request.method == "POST":

        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        precio = request.form['precio']

        db = SessionLocal()

        producto = Producto(nombre, cantidad, precio)

        db.add(producto)
        db.commit()

        db.close()

        return redirect("/productos")

    return render_template("producto_form.html")


@app.route('/guardar_archivo', methods=['POST'])
def guardar_archivo():

    producto = {
        "nombre": request.form['nombre'],
        "cantidad": request.form['cantidad'],
        "precio": request.form['precio']
    }

    guardar_txt(producto)
    guardar_json(producto)
    guardar_csv(producto)

    return redirect("/datos")


@app.route('/datos')
def datos():

    datos_txt = leer_txt()
    datos_json = leer_json()
    datos_csv = leer_csv()

    return render_template("datos.html",
                           txt=datos_txt,
                           json=datos_json,
                           csv=datos_csv)


if __name__ == '__main__':
    app.run(debug=True)