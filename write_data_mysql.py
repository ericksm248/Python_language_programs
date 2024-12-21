import mysql.connector
import random
from mysql.connector import Error

def conectar():
    """Conecta al servidor MySQL."""
    try:
        conexion = mysql.connector.connect(
            host='127.0.0.1',
            user='admin',
            password='1234',
            database='bd_almacen'
        )
        if conexion.is_connected():
            print('Conexión exitosa.')
            return conexion
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")

def insertar_datos(conexion):
    try:
        cursor = conexion.cursor()
        for i in range(50):
            #consulta_sql = "INSERT INTO almacen(id_producto, producto,precio) VALUES (%s,%s,%s )"
            consulta_sql = "INSERT INTO almacen(id_producto,producto,precio) VALUES (%s,%s,%s )"
            #consulta_sql = ("UPDATE bd_almacen.almacen SET producto = (%s) WHERE (id_producto = (%s))")
            #datos = (str(''.join(f"dataasd {i}")), i+8)
            datos = (i,str(''.join(f"data {i}")), random.randint(0, 200))
            cursor.execute(consulta_sql, datos)
            conexion.commit()
            print(f"Dato {i} actualizado correctamente.")
    except Error as e:
        print(f"Error al insertar datos: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print('Conexión cerrada.')

# Uso de las funciones
conexion = conectar()
if conexion:
    insertar_datos(conexion)
