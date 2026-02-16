from flask import Flask

app = Flask(__name__)

# Ruta principal
@app.route('/')
def inicio():
    return "Bienvenido al Sistema de Turnos – Clínica XYZ"

# Ruta dinámica
@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f"Bienvenido, {nombre}. Tu turno está en proceso."

# Ejecutar servidor
if __name__ == '__main__':
    app.run(debug=True)
