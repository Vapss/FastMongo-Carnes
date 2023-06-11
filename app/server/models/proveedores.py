from typing import Optional

from pydantic import BaseModel, Field, EmailStr

class ProveedoresSchema(BaseModel):
    Nombre: str = Field(...)
    Telefono: str = Field(...)
    Email: EmailStr = Field(...)
    Estado: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "Nombre": "Los tristes",
                "Telefono": "123456789",
                "Email":  "tristes@x.edu.com",
                "Estado": "Ciudad de México",
            }
        }
        
class UpdateProveedoresModel(BaseModel):
    Nombre: Optional[str]
    Telefono: Optional[str]
    Email: Optional[EmailStr]
    Estado: Optional[str]
    
    class Config:
        schema_extra = {
            "example": {
                "Nombre": "Los tristes 21",
                "Telefono": "123456789",
                "Email":  "exa@x.edu.com",
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