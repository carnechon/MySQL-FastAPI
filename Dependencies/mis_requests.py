import requests

def menu():
    while True:
        print()
        print("1. GET (Mostrar la tabla completa.)") #FUNCIONA
        print("2. POST (Añadir una ciudad.)") #FUNCIONA
        print("3. PUT (Modificar una ciudad.)") #FUNCIONA
        print("4. DELETE (Borrar una ciudad.)") #FUNCIONA
        print("5. EXIT") #FUNCIONA
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            Endpoints.get()
        elif opcion == 2:
            Endpoints.post()
        elif opcion == 3:
            Endpoints.put()
        elif opcion == 4:
            Endpoints.delete()
        elif opcion == 5:
            break


class Endpoints:
    @classmethod
    def get(url, id=None):
        print("\033[93mSi no ingresa un ID, se mostrará la tabla completa.\033[0m")
        try:
            id_input = input("Ingrese el ID de la ciudad: ")
            # Convierte el ID ingresado a un número entero, si es cualquier otro tipo de dato, se asigna None.
            id = int(id_input) if id_input else None
        # Si el ID ingresado no es un número, se asigna None
        except ValueError:
            id = None

        # URL del servidor FastAPI
        url_base = "http://localhost:8050/city"

        # Construye la URL según el ID ingresado
        url = f"{url_base}/{id}" if id else url_base

        # Realizar la solicitud GET
        response = requests.get(url)

        # Mostrar el contenido de la respuesta
        print(response.content)

        # Mostrar el código de estado de la respuesta
        print(f"\n Codigo: \033[92m{response.status_code}\033[0m")

    def get_cc(countrycode=None):
        url = "http://localhost:8050/city"
        # Realizar la solicitud GET
        response = requests.get(url, params={"countrycode":"ESP"})

        # Mostrar el contenido de la respuesta
        print(response.content)

        # Mostrar el código de estado de la respuesta
        print(f"\n Codigo: \033[92m{response.status_code}\033[0m")
        
    def post():
        # URL del servidor FastAPI
        url = "http://localhost:8050/city"

        # Datos de la ciudad a enviar en la solicitud POST
        city_info = {
            "id": 4080,
            "name": "NewCity1",
            "countryCode": "USA",
            "district": "ExampleDistrict1",
            "population": 1800
            },{
            "id": 4081,
            "name": "Lomonomo",
            "countryCode": "PSE",
            "district": "Nablus",
            "population": 51516
            },{
            "id": 4082,
            "name": "Nkkmkmkity3",
            "countryCode": "USA",
            "district": "ExampleDistrict3",
            "population": 100
            }

        # Realizar las solicitudes PUT para cada ciudad en la lista
        for city in city_info:
            city_id = city["id"] # city = 4080, 4081, 4082
            response = requests.post(f"{url}", json=city)
            if response.status_code == 200:
                print(f"City {city_id}\033[92m created\033[0m successfully")
            else:
                print(f"Error creating city {city_id}: Code \033[91m{response.status_code}\033[0m")
                print("Error response:", response.content)           


    def put():#Por algun bug, a veces se duplica la peticion.
        # URL del servidor FastAPI
        url = "http://localhost:8050/city"

        # Datos de la ciudad a enviar en la solicitud POST
        city_info = {
            "id": 4080,
            "name": "vrvrvrvaaaaa",
            "countryCode": "USA",
            "district": "ExampleDistrict1aaaa",
            "population": 1800
            },{
            "id": 4081,
            "name": "rvrvrvaaaaa",
            "countryCode": "USA",
            "district": "ExampleDistrictaaaa2",
            "population": 500
            },{
            "id": 4082,
            "name": "rfrffr",
            "countryCode": "USA",
            "district": "ExampleDistrictaaaa3",
            "population": 100
            }

        # Realizar las solicitudes PUT para cada ciudad en la lista
        for city in city_info:
            city_id = city["id"]
            response = requests.put(f"{url}/{city_id}", json=city)
            if response.status_code == 200:
                print(f"City {city_id}\033[93m updated\033[0m successfully")
            else:
                print(f"Error creating city {city_id}: Code \033[91m{response.status_code}\033[0m")
                print("Error response:", response.content)  

    def delete():
        # URL del servidor FastAPI
        url = "http://localhost:8050/city"

        # Datos de la ciudad a enviar en la solicitud POST
        city_info = {
            "id": 4080
            },{
            "id": 4081
            },{
            "id": 4082
            }

        # Realizar las solicitudes PUT para cada ciudad en la lista
        for city in city_info:
            city_id = city["id"]
            response = requests.delete(f"{url}/{city_id}", json=city)
            if response.status_code == 200:
                print(f"City {city_id}\033[91m deleted\033[0m successfully")
            else:
                print(f"Error creating city {city_id}: Code \033[91m{response.status_code}\033[0m")
                print("Error response:", response.content)

menu()