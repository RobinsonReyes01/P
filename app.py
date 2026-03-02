from flask import Flask, render_template, request, redirect
from database import crear_tabla
from models import Inventario

app = Flask(__name__)
crear_tabla()

inventario = Inventario()

@app.route('/')
def index():
    productos = inventario.obtener_todos()
    return render_template("productos.html", productos=productos)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        precio = request.form['precio']
        inventario.agregar_producto(nombre, cantidad, precio)
        return redirect('/')
    return render_template("agregar.html")

@app.route('/eliminar/<int:id>')
def eliminar(id):
    inventario.eliminar_producto(id)
    return redirect('/')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        cantidad = request.form['cantidad']
        precio = request.form['precio']
        inventario.actualizar_producto(id, cantidad, precio)
        return redirect('/')
    return render_template("editar.html", id=id)

if __name__ == '__main__':
    app.run(debug=True)