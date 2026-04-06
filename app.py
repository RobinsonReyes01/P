from flask import Flask, render_template, request, redirect, flash
from inventario.bd import Base, engine, SessionLocal
from inventario.productos import Producto
from inventario.inventario import guardar_txt, guardar_json, guardar_csv
from inventario.inventario import leer_txt, leer_json, leer_csv
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models.user_model import Usuario
from Conexion.conexion import conectar
from models.producto_service import *
from models.user_service import *
from forms.producto_form import ProductoForm
from database import crear_tabla_usuarios

app = Flask(__name__)

app.secret_key = "0502508104"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    usuario_data = obtener_usuario_por_id(int(user_id))
    if usuario_data:
        return Usuario(id=usuario_data[0], nombre=usuario_data[1], email=usuario_data[2], password=usuario_data[3])
    return None

Base.metadata.create_all(engine)
crear_tabla_usuarios()


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        usuario = verificar_password(email, password)
        if usuario:
            user_obj = Usuario(id=usuario[0], nombre=usuario[1], email=usuario[2], password=usuario[3])
            login_user(user_obj)
            return redirect('/')
        else:
            flash('Credenciales incorrectas')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        try:
            crear_usuario(nombre, email, password)
            flash('Usuario registrado exitosamente')
            return redirect('/login')
        except:
            flash('Error al registrar usuario')
    return render_template('registro.html')

@app.route('/usuarios')
@login_required
def usuarios():
    usuarios_list = obtener_usuarios()
    return render_template('usuarios.html', usuarios=usuarios_list)


@app.route('/productos')
@login_required
def listar_productos():

    productos = obtener_productos()
    return render_template("productos/lista.html", productos=productos)

@app.route('/productos/nuevo', methods=['GET','POST'])
@login_required
def nuevo_producto():

    if request.method == 'POST':

        form = ProductoForm(request.form)

        crear_producto(form.nombre, form.precio, form.stock)

        return redirect('/productos')

    return render_template("productos/form.html")

@app.route('/productos/editar/<int:id>', methods=['GET','POST'])
@login_required
def editar_producto(id):

    if request.method == 'POST':

        form = ProductoForm(request.form)

        actualizar_producto(id, form.nombre, form.precio, form.stock)

        return redirect('/productos')

    producto = obtener_producto(id)

    return render_template("productos/form.html", producto=producto)

@app.route('/productos/eliminar/<int:id>')
@login_required
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