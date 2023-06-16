# asyncio es una libreria que permite ejecutar funciones asincronas, es decir, que se ejecutan en un tiempo determinado.
# aiomysql es una libreria que permite la conexion a una BD MySQL.
import asyncio
import aiomysql

#Realiza la conexion a la base de datos, cerrar conexion tiene que ser un metodo a parte definido en repository.
async def get_database():
    while True:
        try:
            conn = await aiomysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="toor",
                db="world",
                autocommit=True
            )
        except aiomysql.Error as e:
            print("Problema al conectar con la BD: ", e)
            await asyncio.sleep(5)
        else:
            return conn



# Ejemplo de uso de la libreria asyncio para crear una funcion asincrona que se conecta a la BD y la cierra en un tiempo determinado.
# # Funcion asincrona que asigna el tiempo de espera a la conexion a la BD y la cierra.
# async def main():
#     conn = await get_database()
#     conn.close()
# 
# # Bucle de eventos. (Condicion que resumidamente, ejecuta main() en un bucle hasta que se complete, si no se completa, no continua con el resto de codigo.
# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())






