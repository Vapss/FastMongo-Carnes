from typing import Optional

from pydantic import BaseModel, Field, EmailStr

class ProductosSchema(BaseModel):
    Nombre: str = Field(...)
    Precio: str = Field(...)
    PesoKG: str = Field(...)
    Distribuidor: str = Field(...)
    Tienda: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "Nombre": "1",
                "Precio": "1",
                "PesoKG": "1",
                "Distribuidor": "1",
                "Tienda": "1",
            }
        }

class UpdateProductosModel(BaseModel):
    Nombre: Optional[str]
    Precio: Optional[str]
    PesoKG: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "Nombre": "1",
                "Precio": "1",
                "CantidadKG": "1",
                "Distribuidor": "1",
                "Tienda": "1",
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
    