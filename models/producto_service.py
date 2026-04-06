from Conexion.conexion import conectar
from models.producto import Producto

# CREAR
def crear_producto(nombre, precio, stock):

    conexion = conectar()
    cursor = conexion.cursor()

    sql = "INSERT INTO productos (nombre, precio, stock) VALUES (?,?,?)"
    cursor.execute(sql, (nombre, precio, stock))

    conexion.commit()
    conexion.close()


# LEER
def obtener_productos():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos")

    datos = cursor.fetchall()
    conexion.close()

    return datos


# OBTENER UNO
def obtener_producto(id):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos WHERE id=?", (id,))
    producto = cursor.fetchone()

    conexion.close()

    return producto


# ACTUALIZAR
def actualizar_producto(id, nombre, precio, stock):

    conexion = conectar()
    cursor = conexion.cursor()

    sql = "UPDATE productos SET nombre=?, precio=?, stock=? WHERE id=?"
    cursor.execute(sql, (nombre, precio, stock, id))

    conexion.commit()
    conexion.close()


# ELIMINAR
def eliminar_producto(id):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM productos WHERE id=?", (id,))

    conexion.commit()
    conexion.close()