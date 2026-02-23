from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal
@app.route('/')
def inicio():
    return render_template('index.html')

# Página Acerca de
@app.route('/about')
def about():
    return render_template('about.html')

# Ruta dinámica (usuarios o pacientes)
@app.route('/usuario/<nombre>')
def usuario(nombre):
    return render_template('usuario.html', nombre=nombre)

# Ruta de ejemplo: productos
@app.route('/productos')
def productos():
    lista_productos = ["Laptop", "Mouse", "Teclado"]
    return render_template('productos.html', productos=lista_productos)

if __name__ == '__main__':
    app.run(debug=True)