from pydantic import BaseModel
#POST,PUT,DELETE

#IMPORTANTE, respetar el orden de los campos, este debe coincidir exactamente con el orden de los campos de la tabla de la BD.
# No es necesario proporcionar un método "__init__" personalizado en la clase "City" cuando se utilizan las declaraciones de tipos (BaseModel).
class City(BaseModel):
    id: int
    name: str
    countryCode: str
    district: str
    population: int





