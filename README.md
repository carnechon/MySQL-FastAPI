# MySQL-FastAPI

Final project of the year, using the FastAPI Framework, uvicorn to connect through the desired port and the standard MySQL database "world".

---
### Page under construction...

## Description in English
This is my last project of this school year in which I have developed with Python an API with the FastAPI framework with a generic MySQL database as a base model for the operation of the code, this code currently only collects the GET, PUSH, PUT, DELETE functions for a single table, it could be developed to view and display other tables, but this is enough to display and use most of the options that this tool allows for this use. In addition, the database is asynchronous, so it can wait a certain amount of time for requests from the server.

### Libraries that I have used
- anyio - Used only for an asynchronous DB reconnection loop.
- aiomysql - To be able to use asynchronous DB connection in database.py and define errors.
- fastapi - Define and build the Python API with MySQL, also to declare Python endpoints. Also to be able to use the @app decorator.
- uvicorn - Asynchronous web server to handle multiple requests. Also used to define the connection port to the server.
- requests - To be able to make requests to the DB.
- typing - To be able to return None in case the variable is not found, this is useful when using the same code for several different things.
- os - To use system functions, in my case cleaning the terminal when booting, both Windows and Linux.

## How it works
A simple explanation of how to use it with the MySQL "World" sample DB.

## Modifications
Modifications that can be made to adapt the API to other tables.

## Problems
Some problems you may encounter during server execution or with FastAPI requests.

---

## Descripcion en Español
Este es mi ultimo proyecto del curso escolar en el cual he desarrollado con Python una API con el marco de trabajo FastAPI con una base de datos genérica de MySQL como modelo base para el funcionamiento del código, este código actualmente solo recoge las funciones GET, PUSH, PUT, DELETE para una única tabla, se podría desarrollar para poder ver y mostrar otras tablas, pero con esto es suficiente para poder mostrar y utilizar la mayoría de opciones que permite esta herramienta para este uso. Además la base de datos es asíncrona, por lo que puede esperar un tiempo a las peticiones del servidor.

### Librerias que he utilizado
- anyio - Usado únicamente para un bucle de reconexión asíncrona de la BD
- aiomysql - Para poder utilizar la conexión asíncrona a la BD en database.py y definir errores.
- fastapi - Define y construye la API de Python con MySQL, tambien para declarar los endpoints de Python. Además para poder utilizar el decorador @app.
- uvicorn - Servidor web asíncrono para gestionar múltiples peticiones. Además se utiliza para  definir el puerto de conexión al servidor.
- requests - Para poder realizar las peticiones a la BD.
- typing - Para poder devolver None en caso de que no se encuentre la variable, esto es útil al utilizar el mismo código para varias cosas diferentes.
- os - Para utilizar funciones de sistema, en mi caso limpiar la terminal cuando se arranca, tanto Windows como en Linux.

## Cómo funciona
Una explicacion sencilla de como utilizarla con la BD de ejemplo "World" de MySQL.


## Modificaciones
Modificaciones que se pueden realizar para adaptar la API a otras tablas.

## Problemas
Algunos problemas que puedes encontrar durante la ejecucion del servidor o con las peticiones a FastAPI.

