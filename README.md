# MySQL-FastAPI

Final project of the year, using the FastAPI Framework, uvicorn to connect through the desired port and the standard MySQL database "world".

---

## Description in English

Under construction...

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

## Como funciona
Una explicacion sencilla de como utilizarla con la BD de ejemplo "World" de MySQL.


## Modificaciones
Modificaciones que se pueden realizar para adaptar la API a otras tablas.

## Problemas
Algunos problemas que puedes encontrar durante la ejecucion del servidor o con las peticiones a FastAPI.

