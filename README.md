# MySQL-FastAPI

Final project of the year, using the FastAPI Framework, uvicorn to connect through the desired port and the standard MySQL database "world".

---
### Page under construction...

## Description in English
This is my last project of this school year in which I have developed with Python an API with the FastAPI framework with a generic MySQL database as a base model for the operation of the code, this code currently only collects the GET, POST, PUT, DELETE functions for a single table, it could be developed to view and display other tables, but this is enough to display and use most of the options that this tool allows for this use. In addition, the database is asynchronous, so it can wait a certain amount of time for requests from the server.

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
A simple explanation of how to use it with the MySQL "World" example database.

For the program to work you need to go to ./program/database.py, from line 12 to 15.
```
  host="localhost",
  port=3306,
  user="example", 
  password="example"
```
We modify these fields with the MySQL user name and password, we define the port with which it will make the connection, the standard port is 3306, and the host is the IP of the equipment, localhost or 0.0.0.0.0 refer to the OS of itself, if it were in another machine we would have to put another IP.

In ./Dependencies/menu.py, on line 24, which is where the Uvicorn server runs, we will also define the port for FastAPI requests.
```
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0.0", port=8000)
```
Then in the system shell go to the ./Dependencies location and then run menu.py.

```
> cd ./Dependencies
> python .menu.py ...py
```
Now, we would have the API working, but.... How do we send requests?
Easy, from ./Dependencies we execute with the terminal mis_requests.py, where I use the library requests
to facilitate the use of requests although in case of modifying the IP or the port we would have to modify the url variable for each request.
```
url = "http://localhost:8000/city"
```

This can also be done using cURL.
```
> curl get http://localhost:8000/city ...city
> curl -X POST -H "Content-Type: application/json" -d '{"id": 4080, "name": "City Name", "countryCode": "USA", "district": "LosAlamos", "population": 1000}' http://localhost:8000/city
> curl -X PUT -H "Content-Type: application/json" -d '{"id": 4080, "name": "New City Name", "countryCode": "USA", "district": "LosAlamos2", "population": 3215}' http://localhost:8000/city/4080
> curl -X DELETE http://localhost:8000/city/4080
```

Or just from the browser.
http://localhost:8000/docs
http://localhost:8000/city
http://localhost:8000/city/6
http://localhost:8000/city/countrycode=USA


## Problems
Some problems you may encounter during server execution or with FastAPI requests.

---

## Descripcion en Español
Este es mi ultimo proyecto del curso escolar en el cual he desarrollado con Python una API con el marco de trabajo FastAPI con una base de datos genérica de MySQL como modelo base para el funcionamiento del código, este código actualmente solo recoge las funciones GET, POST, PUT, DELETE para una única tabla, se podría desarrollar para poder ver y mostrar otras tablas, pero con esto es suficiente para poder mostrar y utilizar la mayoría de opciones que permite esta herramienta para este uso. Además la base de datos es asíncrona, por lo que puede esperar un tiempo a las peticiones del servidor.

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

Para que el programa funcione es necesario ir ./program/database.py, de la linea 12 al 15.
```
  host="localhost",
  port=3306,
  user="example", 
  password="example"
```
Modificamos estos campos con el nombre y contraseña de usuario de MySQL, definimos el puerto con el cual hara la conexion, el puerto estandar es el 3306, y el host es la IP del equipo, localhost o 0.0.0.0 hacen referencia al SO de si mismo, si estuviera en otra maquina que habria que poner otra IP.

En ./Dependencias/menu.py, en la linea 24, que es donde se ejecuta el servidor de Uvicorn donde tambien definiremos el puerto para las peticiones de FastAPI.
```
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
Luego en la Shell del sistema iremos a la ubicación ./Dependencias y luego ejecutamos menu.py.

```
> cd ./Dependencias
> python .\menu.py
```
Ahora, tendriamos la API funcionando, pero... ¿Como enviamos peticiones?
Facil, desde ./Dependencias ejecutamos con la terminal mis_requests.py, donde uso la libreria requests
para facilitar el uso de peticiones aunque en caso de modificar la IP o el puerto habria que modificar la variable url por cada peticion
```
url = "http://localhost:8000/city"
```

Tambien se pueden hacer utilizando cURL.
```
> curl get http://localhost:8000/city
> curl -X POST -H "Content-Type: application/json" -d '{"id": 4080, "name": "City Name", "countryCode": "USA", "district": "LosAlamos", "population": 1000}' http://localhost:8000/city
> curl -X PUT -H "Content-Type: application/json" -d '{"id": 4080,"name": "New City Name","countryCode": "USA","district": "LosAlamos2","population": 3215}' http://localhost:8000/city/4080
> curl -X DELETE http://localhost:8000/city/4080
```

O simplemete desde el navegador.
http://localhost:8000/docs
http://localhost:8000/city
http://localhost:8000/city/6
http://localhost:8000/city/countrycode=USA

### Funcionamiento de la API



## Problemas
Algunos problemas que puedes encontrar durante la ejecucion del servidor o con las peticiones a FastAPI.

