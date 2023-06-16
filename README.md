# MySQL-FastAPI
Final project of the year, using the FastAPI Framework, uvicorn to connect through the desired port and the standard MySQL database "world".

-Descricion en Español-
Este es mi ultimo proyecto del curso escolar en el cual he desarrollado con Python una API con el marco de trabajo FastAPI con una base de datos generica de MySQL como modelo base para el funcionamiento del codigo, este codigo alctualmente solo recoge las funciones GET, PUSH, PUT, DELETE para una unica tabla, se podria desarrollar para poder ver y mostrar otras tablas, pero con esto es suficiente para poder mostrar y utilizar la mayoria de opciones que permite esta herramienta para este uso. Ademas la base de datos es asincrona, por lo que puede esperar un tiempo a las peticiones del servidor.

Librerias que he utilizado.
-anyio
-aiomysql - Para poder utilizar la conexion asincrona a la BD en database.py y definir errores.
-fastapi - Para poder utilizar el decorador @app.
-uvicorn
-requests - Para poder realizar las peticiones a la BD.
-typing - Para poder devolver None en caso de que no se encuentre la varible, esto es util al utilizar el mismo codgio para varias cosas diferentes.
