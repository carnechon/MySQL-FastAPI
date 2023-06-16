from program.database import get_database
from program.esquema import City

# Aqui se define cada metodo que permitira el programa al interactuar con la BD. Luego en _init_.py se continua.
class Repositorio:
    async def get_all(self):
        db_connection = await get_database()
        try:
            async with db_connection.cursor() as cursor:
                await cursor.execute("SELECT * FROM city")
                cities = await cursor.fetchall()
                return cities
        finally:
            db_connection.close()


    async def find_by_type(self, countrycode_type):
        db_connection = await get_database()
        try:
            cursor = await db_connection.cursor()
            await cursor.execute("SELECT * FROM city WHERE countryCode = %s", (countrycode_type,))
            cities = await cursor.fetchall()
            return cities
        finally:
            db_connection.close()


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



    async def update(self, city_id: int, city: City):
        db_connection = await get_database()
        try:
            async with db_connection.cursor() as cursor:
                await cursor.execute(
                    "UPDATE city SET Name=%s, CountryCode=%s, District=%s, Population=%s WHERE ID=%s",
                    (city.name, city.countryCode, city.district, city.population, city_id)
                    )
                await db_connection.commit()
        finally:
            db_connection.close()


    async def delete(self, city_id: int):
        db_connection = await get_database()
        try:
            async with db_connection.cursor() as cursor:
                await cursor.execute("DELETE FROM city WHERE ID = %s", (city_id,))
                await db_connection.commit()
                
        finally:
            db_connection.close()
                    
