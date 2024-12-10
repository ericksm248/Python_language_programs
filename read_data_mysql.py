import mysql.connector

import string
from mysql.connector import Error

def conectar():
    """Conecta al servidor MySQL."""
    try:
        conexion = mysql.connector.connect(
            host='127.0.0.1',
            user='admin',
            password='1234',
            database='my_bd'
        )
        if conexion.is_connected():
            print('Conexión exitosa.')
            return conexion
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")


def leer_datos(conexion):
    #tengo que saber como esta estructurada la tabla y sus campos
    try:
        cursor = conexion.cursor()
        query = "select * from almacen;"
        cursor.execute(query)
        for (id_producto,producto,precio) in cursor:
            print("{},{},{}".format(id_producto,producto,precio))

    except Error as e:
        print(f"Error al leer datos: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print('Conexión cerrada.')

# Uso de las funciones
conexion = conectar()
if conexion:
    leer_datos(conexion)
