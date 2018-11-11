#!/usr/bin/python
import psycopg2
from config import config

"""
I created this file with reference to here: http://www.postgresqltutorial.com/postgresql-python/connect/
"""

def connection():
    """
    Conectar con postgresql
    """
    connection = None
    try:
        # leer los parámetros de conexión
        params = config()

        # conectar con la base de datos de postgreql
        print('Conectando con postgres ...')
        connection = psycopg2.connect(**params)

        # Create a cursor
        cursor = connection.cursor()

        # Se pregunta la versión de postgres
        print('Versión de Postgresql:')
        cursor.execute('SELECT version()')
        db_version = cursor.fetchone()
        print(db_version)

        # se cierra la conexion
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Conexion cerrada')

