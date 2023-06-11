from typing import Optional

from pydantic import BaseModel, Field, EmailStr

class PedidosSchema(BaseModel):
    Cliente: str = Field(...)
    Num_pedido: str = Field(...)
    Producto: str = Field(...)
    CantidadKG: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "Cliente": "123456789",
                "Num_pedido": "1",
                "Producto": "1",
                "CantidadKG": "1",
            }
        }

class UpdatePedidosModel(BaseModel):
    Cliente: Optional[str]
    Num_pedido: Optional[str]
    Producto: Optional[str]
    CantidadKG: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "Cliente": "123456789",
                "Num_pedido": "1",
                "Producto": "1",
                "CantidadKG": "1",
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
