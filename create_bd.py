import pymysql

# Datos de conexión al servidor MySQL
host = 'localhost'
user = 'root'
password = '123456'

# Crear la conexión
connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS products_db")
    print("Base de datos 'products_db' creada o ya existente.")
finally:
    connection.close()
