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
You can modify the example values that are not enclosed in "" quotes for each request.
```
> curl get http://localhost:8000/city ...city
> curl -X POST -H "Content-Type: application/json" -d '{"id": 4080, "name": "City Name", "countryCode": "USA", "district": "LosAlamos", "population": 1000}' http://localhost:8000/city
> curl -X PUT -H "Content-Type: application/json" -d '{"id": 4080, "name": "New City Name", "countryCode": "USA", "district": "LosAlamos2", "population": 3215}' http://localhost:8000/city/4080
> curl -X DELETE http://localhost:8000/city/4080
```

Or just from the browser.
```
http://localhost:8000/docs
http://localhost:8000/city
http://localhost:8000/city/6
http://localhost:8000/city/countrycode=USA
```


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
Puedes modificar los valores de ejemplo que no estan entre "" comillas de cada peticion.
```
> curl get http://localhost:8000/city
> curl -X POST -H "Content-Type: application/json" -d '{"id": 4080, "name": "City Name", "countryCode": "USA", "district": "LosAlamos", "population": 1000}' http://localhost:8000/city
> curl -X PUT -H "Content-Type: application/json" -d '{"id": 4080,"name": "New City Name","countryCode": "USA","district": "LosAlamos2","population": 3215}' http://localhost:8000/city/4080
> curl -X DELETE http://localhost:8000/city/4080
```

O simplemete desde el navegador.
```
http://localhost:8000/docs
http://localhost:8000/city
http://localhost:8000/city/6
http://localhost:8000/city/countrycode=USA
```

## Funcionamiento de la API

### menu.py
No hace mucho, solo llama a /program/endpoints.py para definir los endpoints de FastAPI ademas de levantar el servidor Uvicorn con una IP y un puerto especificos.

### endpoints.py
El cuerpo de los endpoints, es la conexion a la BD de MySQL,la variable repositorio que ejecuta el metodo de la clase Repositorio() de metodos.py y ademas almacena la ultima accion realizada y errores de excepcion e integridad de errores.
- GET
Si en una peticion GET recibe un codigo de pais (/city?countrycode=ESP), esperara a cities he imprimira el resultado del metodo find_by_type con la variable countrycode.
Si por el contrario no tiene un codigo de pais (/city), esperara a cities y mostrara el resultado de get_all ubicado en metodos.py
```
async def get_city(countrycode: Optional[str] = None):
    try:
        if countrycode:
            print ("Buscando por countrycode: ", countrycode)
            cities = await repositorio.find_by_type(countrycode)
        if not countrycode:
            print("Mostrando la tabla completa.")
            cities = await repositorio.get_all()
    ...
    else:   
        return cities
```
- GET_ID
Espera a find_by_id con la variable "city_id" que difine la id que va a recibir en repositorio.find_by_id y lo guarda en repositorio. 
```
async def get_city(city_id: int):
    try:
        city = await repositorio.find_by_id(city_id)
    ...
    else:   
        return city
```

- POST
Recibe valores segun la estructura de City, espera al metodo create, la ejecuta y lo guarda en repositorio. 
```
async def create_city(city: City):
    repositorio = Repositorio()
    try:
        await repositorio.create(city)
        return {f"{city}": "City created successfully"}
```

- PUT
Recibe una id y valores segun la estructura de City, y son procesadas por el metodo "update" y almacenada en repositorio
```
async def update_city(city_id: int, city: City):
    repositorio = Repositorio() 
    try:
        await repositorio.update(city_id, city)
        return {f"{city}": "City updated successfully"}
```

- DELETE
Espera al metodo delete que procese el input de usuario como "city_id", lo guarda en repositorio he imprime un mensaje.
```
async def delete_city(city_id: int):
    repositorio = Repositorio()
    try:
        await repositorio.delete(city_id)
        return {f"City with id {city_id}": "City deleted successfully"}
```

- HTTPexception
En caso de recibir un error de sintaxis y que no exista, devolvera este error.
```
async def http_exception_handler(exc):
    status_code = exc.status_code
    detail = str(exc.detail)
    return JSONResponse(status_code=status_code, content={"Error 404":detail+"| (._.)?"})
```

### database.py
Almacena la conexion a la base de datos, los commit son automaticos, por lo que si se envia un "execute" en un cursor es procesado automaticamente por MySQL.
```
autocommit=True
```

### esquema.py
Contine una clase con la estructura de una fila (izquierda a derecha) y el tipo de valor de cada campo de una tabla de una BD.
La idea de que sea una clase es de poder añadir mas tablas en forma de funciones y que dependan de la misma clase(auque ahora mismo no tenga ninguna funcion), no es necesario __init__ o self al no haber "datos en común", aunque podria usarse para modificar Foreign Keys si por el contrario fueran comunes y si se utilizaria __init__.
```
class City(BaseModel):
    id: int
    name: str
    countryCode: str
    district: str
    population: int
```

### metodos.py
Aqui se definen los metodos que realizan mediante un cursor, ejecuta una sentencia SQL, almacena y devuelve una (fetchone) o muchas (fetchall) lineas para imprimirlo en la terminal, hace un commit (Aun no siendo necesario) y luego cierra la conexion con la BD.

```
async def find_by_id(self, city_id):
    db_connection = await get_database()
    try:
        async with db_connection.cursor() as cursor:
            await cursor.execute("SELECT * FROM city WHERE id = %s", (city_id,))
            result = await cursor.fetchone()
            
            if result:
                city = {"id": result[0],"name": result[1],"countryCode": result[2]}
                return city
    finally:
        db_connection.close()
```
```
async def create(self, city: City):
    db_connection = await get_database()
    try:
        async with db_connection.cursor() as cursor:
            await cursor.execute(
                "INSERT INTO city (ID, Name, CountryCode, District, Population)"
                "VALUES (%s, %s, %s, %s, %s)",
                (city.id, city.name, city.countryCode, city.district, city.population)
                )
            await db_connection.commit()
    finally:
        db_connection.close()
```
