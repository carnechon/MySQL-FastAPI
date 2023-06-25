from program.database import get_database
from program.esquema import City
from pydantic import BaseModel

# Aqui se define cada metodo que permitira el programa al interactuar con la BD. Luego en _init_.py se continua.
class Repositorio(BaseModel):
    async def get_all():
        db_connection = await get_database()
        try:
            async with db_connection.cursor() as cursor:
                await cursor.execute("SELECT * FROM city")
                cities = await cursor.fetchall()
                return cities
        finally:
            db_connection.close()

    async def find_by_countrycode(City, countrycode_type):
        db_connection = await get_database()
        try:
            cursor = await db_connection.cursor()
            await cursor.execute("SELECT * FROM city WHERE countryCode = %s", (countrycode_type,))
            cities = await cursor.fetchall()
            return cities
        finally:
            db_connection.close()

    async def find_by_district(City, district_type):
        db_connection = await get_database()
        try:
            cursor = await db_connection.cursor()
            await cursor.execute("SELECT * FROM city WHERE district = %s", (district_type,))
            cities = await cursor.fetchall()
            return cities
        finally:
            db_connection.close()
    
    async def find_by_countrycode_and_district(City, countrycode_type, district_type):
        db_connection = await get_database()
        try:
            cursor = await db_connection.cursor()
            await cursor.execute("SELECT * FROM city WHERE CountryCode = %s AND District = %s", (countrycode_type, district_type,))
            cities = await cursor.fetchall()
            for city in cities:
                print(city)

            return cities
        finally:
            db_connection.close()

    async def find_by_id(City, city_id):
        db_connection = await get_database()
        try:
            async with db_connection.cursor() as cursor:
                await cursor.execute("SELECT * FROM city WHERE id = %s", (city_id,))
                result = await cursor.fetchone()
                
                if result:
                    city = {"id": result[0],"name": result[1],"countryCode": result[2],"district": result[3],"population": result[4]}
                    return city
        finally:
            db_connection.close()


    async def create(City, city: City):
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



    async def create_without_id(City, city: City):
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



    async def update(City, city_id: int, city: City):
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


    async def delete(City, city_id: int):
        db_connection = await get_database()
        try:
            async with db_connection.cursor() as cursor:
                await cursor.execute("DELETE FROM city WHERE ID = %s", (city_id,))
                await db_connection.commit()
                
        finally:
            db_connection.close()
                    
