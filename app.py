from Flask import Flask, render_template, request, redirect
from inventario.bd import Base, engine, SessionLocal
from inventario.productos import Producto
from inventario.inventario import guardar_txt, guardar_json, guardar_csv
from inventario.inventario import leer_txt, leer_json, leer_csv
from Flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import Usuario
from Conexion.conexion import conectar
from services.producto_service import *
from forms.producto_form import ProductoForm

app = Flask(__name__)

app.secret_key = "clave_secreta"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

Base.metadata.create_all(engine)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/productos')
def listar_productos():

    productos = obtener_productos()
    return render_template("productos/lista.html", productos=productos)

@app.route('/productos/nuevo', methods=['GET','POST'])
def nuevo_producto():

    if request.method == 'POST':

        form = ProductoForm(request.form)

        crear_producto(form.nombre, form.precio, form.stock)

        return redirect('/productos')

    return render_template("productos/form.html")

@app.route('/productos/editar/<int:id>', methods=['GET','POST'])
def editar_producto(id):

    if request.method == 'POST':

        form = ProductoForm(request.form)

        actualizar_producto(id, form.nombre, form.precio, form.stock)

        return redirect('/productos')

    producto = obtener_producto(id)

    return render_template("productos/form.html", producto=producto)

@app.route('/productos/eliminar/<int:id>')
def eliminar(id):

    eliminar_producto(id)
    return redirect('/productos')


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

from reportlab.platypus import SimpleDocTemplate, Table

@app.route('/reporte_pdf')
def reporte_pdf():

    productos = obtener_productos()

    doc = SimpleDocTemplate("reporte_productos.pdf")

    data = [["ID","Nombre","Precio","Stock"]]

    for p in productos:
        data.append([p[0], p[1], p[2], p[3]])

    table = Table(data)

    elements = []
    elements.append(table)

    doc.build(elements)

    return "Reporte generado"


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