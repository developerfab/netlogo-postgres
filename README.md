## WHAT IS IT?

This is a test to try to connect netlogo with postgresql through python

## Requeriments

For run this project you need to install:

1. **virtualenv**To run this project you must to have install _virtualenv_. More information [here](https://virtualenv.pypa.io/en/latest/)

2. **psycopg2:** 
  This python plugin help to connect python with postgresql

  With pip:

  ```bash
  pip install psycopg2
  ```

  More information [here](https://pypi.org/project/psycopg2/)


3. **sbt:** It's a build tool for scala, java an more. Is necessary that you have installing Java 1.8 or later.  More information [here](https://www.scala-sbt.org/index.html)

4. **python extension:** It's a netlogo extension to connect netlogo with python. Please follow the steps that are describe there. More information [here](https://github.com/NetLogo/PythonExtension)

5. **configparser** It's an anaconda library. If you want to install it you could use anaconda navigator in the section environment and in the search field put something as _configparser_.

## HOW IT WORKS

This applitacion can insert data in postgres through python using the python extension. I created a python configuration with multiple files achieving connect python with postgres. 

## HOW TO USE IT

1. If you are using virtualenv or an anaconda environment you first should power on the environment. Remember that that environment should be configured in python 3.

2. Please run the command `pip install -r requeriments.txt` 
3. Please download `python extension` and configured like the author describe.
5. Please copy `database.ini.example` to `database.ini` and put your host, database, user and password postgresql.
6. Run netlogo from environment. For example, in mac you could run this command:
  ```bash
  open /Applications/NetLogo\ 6.0.3/NetLogo\ 6.0.3.app/
  ```
7. Inside in netlogo, in the command line you could run this instruction:

  ```
  > conection
  ```

  And you should see something like:

  ```
  observer> conection
  [('host', 'localhost'), ('database', 'netlogo'), ('user', 'postgres'), ('password', 'your_password_postgres')]
  Conectando con postgres ...
  Versión de Postgresql:
  ('PostgreSQL 9.4.10 on x86_64-apple-darwin, compiled by i686-apple-darwin11-llvm-gcc-4.2 (GCC) 4.2.1 (Based on Apple Inc. build 5658) (LLVM build   2336.11.00), 64-bit',)
  Conexion cerrada
  ```
6. If you want to send an especific instruction you can change the 10 line in this project. Also I adde in `connection.py` to the function `insert()` a `COMMIT` by default. You can change it if you preffer. 

## THINGS TO TRY

Try to change the line 10 in this project. Also you could change the connection file.

## EXTENDING THE MODEL

If you have ideas about how this works, I receive suggestions to better this project.

## RELATED MODELS

(models in the NetLogo Models Library and elsewhere which are of related interest)

## CREDITS AND REFERENCES

* [PostgresSQL python: Connect to PostgreSQL database server](http://www.postgresqltutorial.com/postgresql-python/connect/)
* [Netlogo Distribuido](https://gitlab.com/cdaza/netlogo-distribuido)
