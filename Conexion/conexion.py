import mysql.connector

def conectar():

    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",  
        database="tienda"
    )

    return conexion