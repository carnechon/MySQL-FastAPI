# asyncio es una libreria que permite ejecutar funciones asincronas, es decir, que se ejecutan en un tiempo determinado.
# aiomysql es una libreria que permite la conexion a una BD MySQL.
import asyncio
import aiomysql

#Realiza la conexion a la base de datos, cerrar conexion tiene que ser un metodo a parte definido en repository.
#Modifica "example" por tu nombre y contraseña de usuario.
async def get_database():
    while True:
        try:
            conn = await aiomysql.connect(
                host="localhost",
                port=3306,
                user="example", 
                password="example",
                db="world",
                autocommit=True
            )
        except aiomysql.Error as e:
            print("Problema al conectar con la BD: ", e)
            await asyncio.sleep(5)
        else:
            return conn









