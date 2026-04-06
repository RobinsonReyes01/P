from Conexion.conexion import conectar
from werkzeug.security import generate_password_hash, check_password_hash

# CREAR USUARIO
def crear_usuario(nombre, email, password):
    hashed_password = generate_password_hash(password)
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("INSERT INTO usuarios (nombre, email, password) VALUES (?, ?, ?)", (nombre, email, hashed_password))

    conexion.commit()
    conexion.close()

# OBTENER TODOS LOS USUARIOS
def obtener_usuarios():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT id, nombre, email FROM usuarios")

    usuarios = cursor.fetchall()
    conexion.close()

    return usuarios

# OBTENER UN USUARIO POR EMAIL
def obtener_usuario_por_email(email):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
    usuario = cursor.fetchone()

    conexion.close()

    return usuario

# OBTENER UN USUARIO POR ID
def obtener_usuario_por_id(id):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
    usuario = cursor.fetchone()

    conexion.close()

    return usuario

# ACTUALIZAR USUARIO
def actualizar_usuario(id, nombre, email, password=None):
    conexion = conectar()
    cursor = conexion.cursor()

    if password:
        hashed_password = generate_password_hash(password)
        cursor.execute("UPDATE usuarios SET nombre = ?, email = ?, password = ? WHERE id = ?", (nombre, email, hashed_password, id))
    else:
        cursor.execute("UPDATE usuarios SET nombre = ?, email = ? WHERE id = ?", (nombre, email, id))

    conexion.commit()
    conexion.close()

# ELIMINAR USUARIO
def eliminar_usuario(id):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))

    conexion.commit()
    conexion.close()