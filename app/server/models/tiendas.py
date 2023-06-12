from typing import Optional

from pydantic import BaseModel, Field, EmailStr

class TiendasSchema(BaseModel):
    TiendaID: str = Field(...)
    Nombre: str = Field(...)
    Direccion: str = Field(...)
    Estado: str = Field(...)
    Distribuidor: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "TiendaID": "1",
                "Nombre": "Matriz",
                "Direccion": "Avenida Siempre Viva 742",
                "Estado": "CDMX",
                "Distribuidor": "1",
            }
        }

class UpdateTiendasModel(BaseModel):
    Nombre: Optional[str]
    Direccion: Optional[str]
    Estado: Optional[str]
    Distribuidor: Optional[str]
    
    class Config:
        schema_extra = {
            "example": {
                "Nombre": "Matriz",
                "Direccion": "Avenida Siempre Viva 742",
                "Estado": "CDMX",
                "Distribuidor": "1",
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}