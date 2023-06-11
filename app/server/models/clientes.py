from typing import Optional

from pydantic import BaseModel, Field, EmailStr

class ClientesSchema(BaseModel):
    Telefono: str = Field(...)
    Nombre: str = Field(...)
    Email: EmailStr = Field(...)
    Direccion: str = Field(...)
    Estado: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "Telefono": "123456789",
                "Nombre": "Jeanette Lynn",
                "Email":  "tellus.id@yahoo.com",
                "Direccion": "Ap #651-8679 Sodales. Av.",
                "Estado": "Ciudad de México",
            }
        }

class UpdateClientesModel(BaseModel):
    Telefono: Optional[str]
    Nombre: Optional[str]
    Email: Optional[EmailStr]
    Direccion: Optional[str]
    Estado: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "Telefono": "123456789",
                "Nombre": "Jeanette Lynn",
                "Email":  "tellus.id@yahoo.com",
                "Direccion": "Ap #651-8679 Sodales. Av.",
                "Estado": "Ciudad de México",
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