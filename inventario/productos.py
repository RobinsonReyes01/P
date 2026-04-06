from sqlalchemy import Column, Integer, String, Float
from inventario.bd import Base


class Producto(Base):

    __tablename__ = "productos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    stock = Column(Integer)
    precio = Column(Float)

    def __init__(self, nombre, stock, precio):
        self.nombre = nombre
        self.stock = stock
        self.precio = precio