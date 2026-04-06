import sqlite3

def conectar():
    return sqlite3.connect("inventario.db")

def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        stock INTEGER NOT NULL,
        precio REAL NOT NULL
    )
    """)

    conexion.commit()
    conexion.close()

def crear_tabla_usuarios():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    """)

    conexion.commit()
    conexion.close()
