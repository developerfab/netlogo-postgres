#!/usr/bin/python
import psycopg2
from config import config

"""
I created this file with reference to here: http://www.postgresqltutorial.com/postgresql-python/connect/
"""

class Connector(object):

    # Attributes
    connection = None
    cursor = None

    # Constructor
    def __init__(self):
        """
        Conectar con postgresql
        """
        try:
            # leer los parámetros de conexión
            params = config()

            # conectar con la base de datos de postgreql
            print('Conectando con postgres ...')
            self.connection = psycopg2.connect(**params)

            # Create a self.cursor
            self.cursor = self.connection.cursor()

            # Se pregunta la versión de postgres
            print('Versión de Postgresql:')
            self.cursor.execute('SELECT version()')
            db_version = self.cursor.fetchone()
            print(db_version)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.connection is None:
                self.connection.close()
                print('Conexion cerrada')

    def insert(self, message):
        self.cursor.execute(message+"COMMIT;")

    def close(self):
        # se cierra la conexion
        self.cursor.close()
        print('Conexion cerrada')
