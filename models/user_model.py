from database import conectar


class Producto:
    def __init__(self, id, nombre, stock, precio):
        self._id = id
        self._nombre = nombre
        self._stock = stock
        self._precio = precio

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_stock(self):
        return self._stock

    def get_precio(self):
        return self._precio

    # Setters
    def set_stock(self, nueva_stock):
        self._stock = nueva_stock

    def set_precio(self, nuevo_precio):
        self._precio = nuevo_precio



class Inventario:
    def __init__(self):
        # Diccionario para búsqueda rápida
        self.productos = {}

    def cargar_desde_bd(self):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        registros = cursor.fetchall()

        for r in registros:
            producto = Producto(*r)
            self.productos[producto.get_id()] = producto

        conexion.close()

    def agregar_producto(self, nombre, stock, precio):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO productos (nombre, stock, precio) VALUES (?, ?, ?)",
            (nombre, stock, precio)
        )
        conexion.commit()
        conexion.close()

    def eliminar_producto(self, id):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
        conexion.commit()
        conexion.close()

    def actualizar_producto(self, id, stock, precio):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE productos SET stock = ?, precio = ? WHERE id = ?",
            (stock, precio, id)
        )
        conexion.commit()
        conexion.close()

    def obtener_todos(self):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        conexion.close()
        return productos
    
from flask_login import UserMixin
class Usuario(UserMixin):

    def __init__(self, id, nombre, email, password):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.password = password

    def get_id(self):
        return str(self.id)