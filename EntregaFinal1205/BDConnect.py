# importing required library
import mysql.connector
 
# connecting to the database
dataBase = mysql.connector.connect(
                     host = "localhost",
                     user = "user",
                     passwd = "pass",
                     database = "practicaUCLM" ) 
 
# preparing a cursor object
cursorObject = dataBase.cursor()
 
# creating table 
cita = """CREATE TABLE CITA (
                   NOMBRE  VARCHAR(20),
                   CORREO VARCHAR(50),
                   TELEFONO VARCHAR(10),
                   FECHA VARCHAR(20),
                   HORA VARCHAR(12),
                   )"""

pedidos = """CREATE TABLE PEDIDOS (
                   NOMBRE  VARCHAR(20),
                   CORREO VARCHAR(50),
                   TELEFONO VARCHAR(10),
                   MODELO VARCHAR(20),
                   COLOR VARCHAR(12,
                   )"""

direcciones = """CREATE TABLE DIRS (
                   MAC ORIGEN  VARCHAR(50),
                   MAC DESTINO VARCHAR(50),
                   IP ORIGEN VARCHAR(16),
                   IP DESTINO VARCHAR(16),
                   COMMENTS VARCHAR(50),
                   )"""
 
# table created
cursorObject.execute(pedidos) 
cursorObject.execute(cita) 
cursorObject.execute(direcciones) 
 
# disconnecting from server
dataBase.close()