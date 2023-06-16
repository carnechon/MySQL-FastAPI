import aiomysql
from typing import Optional
from fastapi import FastAPI, status, Response, HTTPException
from fastapi.responses import JSONResponse


from program.esquema import City
from program.metodos import Repositorio
from program.database import get_database


# Almacenan el ultimo registro del programa.
app = FastAPI()
repositorio = Repositorio()


# --------------------------------------------------------------------- GET ---------------------------------------------------------------------------
#/city
# /city?countrycode=ESP
@app.get("/city")
async def get_city(countrycode: Optional[str] = None):
    try:
        if countrycode:# Si countrycode si se especifica.
            print ("Buscando por countrycode: ", countrycode)
            cities = await repositorio.find_by_type(countrycode)
        if not countrycode: # Si no se especifica el tipo de countrycode.
            print("Mostrando la tabla completa.")
            cities = await repositorio.get_all()
    
    except aiomysql.IntegrityError as e:
        error_message = str(e)
        response = Response(content=f"Integrity Error: {error_message}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response
    except Exception as e:
        error_message = str(e)
        response = Response(content=f"Error: {error_message}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response
    else:   
        return cities

# /city/1
@app.get("/city/{city_id}")
async def get_city(city_id: int):
    try:
        city = await repositorio.find_by_id(city_id)
    
    except aiomysql.IntegrityError as e:
        error_message = str(e)
        response = Response(content=f"Integrity Error: {error_message}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response
    except Exception as e:
        error_message = str(e)
        response = Response(content=f"Error: {error_message}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response
    else:
        return city


# ---------------------------------------------------------------- POST, PUT, DELETE --------------------------------------------------------------------
# "Id" no se puede repetir, CountryCode debe ser de 3 caracteres y que ya exista, District puede ser hasta 20 caracteres, Population debe ser mayor a 0.
# curl -X POST -H "Content-Type: application/json" -d '{"id": 4080, "name": "City Name", "countryCode": "USA", "district": "LosAlamos", "population": 1000}' http://localhost:8000/city
@app.post("/city")
async def create_city(city: City):
    repositorio = Repositorio()
    try:
        await repositorio.create(city)
        return {f"{city}": "City created successfully"}
    
    except aiomysql.IntegrityError as e:
        error_message = str(e)
        response = Response(content=f"Integrity Error: {error_message}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response
    except Exception as e:
        error_message = str(e)
        response = Response(content=f"Error: {error_message}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


# CountryCode debe ser de 3 caracteres y que ya exista, District puede ser hasta 20 caracteres, Population debe ser mayor a 0, el numero de "/city/4080" es la id de la ciudad que se quiere modificar.
# curl -X PUT -H "Content-Type: application/json" -d '{"id": 4080,"name": "New City Name","countryCode": "USA","district": "LosAlamos2","population": 3215}' http://localhost:8000/city/4080
@app.put("/city/{city_id}")
async def update_city(city_id: int, city: City):
    repositorio = Repositorio() 
    try:
        await repositorio.update(city_id, city)
        return {f"{city}": "City updated successfully"}
    
    except aiomysql.IntegrityError as e:
        error_message = str(e)
        response = Response(content=f"Integrity Error: {error_message}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response
    except Exception as e:
        error_message = str(e)
        response = Response(content=f"Error: {error_message}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

# Modifica el valor al final de la URL, en este caso "4081".
# curl -X DELETE http://localhost:8000/city/4081
@app.delete("/city/{city_id}")
async def delete_city(city_id: int):
    repositorio = Repositorio()
    try:
        await repositorio.delete(city_id)
        return {f"City with id {city_id}": "City deleted successfully"}
    
    except aiomysql.IntegrityError as e:
        error_message = str(e)
        response = Response(content=f"Integrity Error: {error_message}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response
    except Exception as e:
        error_message = str(e)
        response = Response(content=f"Error: {error_message}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response




# ---------------------------------------------- Eventos de error ---------------------------------------------------

@app.exception_handler(HTTPException)
async def http_exception_handler(exc):
    status_code = exc.status_code
    detail = str(exc.detail)
    return JSONResponse(status_code=status_code, content={"Error 404":detail+"| (._.)?"})
