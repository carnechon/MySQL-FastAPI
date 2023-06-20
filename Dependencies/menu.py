import uvicorn, os
from program.endpoints import app



@app.get("/")
def get_root():
    return "Hello World"

@app.get("/health")
def health_check():
    return "OK"


# ------ Eventos ------
@app.on_event("startup")
def startup_event():
    os.system('cls' if os.name == 'nt' else 'clear') # Limpia la consola una vez y corrige un bug al mostrar las peticiones en W10 con PS7.
    print("TEST FastAPI")



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
#cd ./Dependencies & python .\menu.py

# http://localhost:8000/ - peticion web
# curl -X GET http://localhost:8000/ - peticion a terminal por consola.
