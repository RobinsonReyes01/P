from database import conectar

# -------------------------
# Clase Producto
# -------------------------
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_cantidad(self, nueva_cantidad):
        self._cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self._precio = nuevo_precio


# -------------------------
# Clase Inventario
# -------------------------
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

    def agregar_producto(self, nombre, cantidad, precio):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)",
            (nombre, cantidad, precio)
        )
        conexion.commit()
        conexion.close()

    def eliminar_producto(self, id):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
        conexion.commit()
        conexion.close()

    def actualizar_producto(self, id, cantidad, precio):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE productos SET cantidad = ?, precio = ? WHERE id = ?",
            (cantidad, precio, id)
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