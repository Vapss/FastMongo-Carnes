from typing import Optional

from pydantic import BaseModel, Field, EmailStr

class PedidosSchema(BaseModel):
    PedidoId: str = Field(...)
    Cliente: str = Field(...)
    Proveedor: str = Field(...)
    Tienda: str = Field(...)
    Producto: str = Field(...)
    CantidadKG: str = Field(...)
    Fecha_pedido: str = Field(...)
    Fecha_entrega: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "Cliente": "123456789",
                "Proveedor": "123456789",
                "Tienda": "123456789",
                "Producto": "123456789",
                "CantidadKG": "1",
                "Fecha_pedido": "2021-01-01",
                "Fecha_entrega": "2021-01-01",
            }
        }

class UpdatePedidosModel(BaseModel):
    Cliente: Optional[str]
    Proveedor: Optional[str]
    Tienda: Optional[str]
    Producto: Optional[str]
    CantidadKG: Optional[str]
    Fecha_pedido: Optional[str]
    Fecha_entrega: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "Cliente": "123456789",
                "Proveedor": "123456789",
                "Tienda": "123456789",
                "Producto": "1",
                "CantidadKG": "1",
                "Fecha_pedido": "2021-01-01",
                "Fecha_entrega": "2021-01-01",
                
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
