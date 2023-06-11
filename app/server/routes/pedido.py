from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_pedidos,
    add_pedido,
    retrieve_pedido,
    update_pedido,
    delete_pedido
)

from server.models.pedidos import (
    ErrorResponseModel,
    ResponseModel,
    PedidosSchema,
    UpdatePedidosModel
)

router = APIRouter()

@router.post("/", response_description="Pedido data added into the database")
async def add_pedido_data(pedido: PedidosSchema = Body(...)):
    pedido = jsonable_encoder(pedido)
    new_pedido = await add_pedido(pedido)
    return ResponseModel(new_pedido, "Pedido added successfully.")

@router.get("/", response_description="Pedidos retrieved")
async def get_pedidos():
    pedidos = await retrieve_pedidos()
    if pedidos:
        return ResponseModel(pedidos, "Pedidos data retrieved successfully")
    return ResponseModel(pedidos, "Empty list returned")

@router.get("/{id}", response_description="Pedido data retrieved")
async def get_pedido_data(id):
    pedido = await retrieve_pedido(id)
    if pedido:
        return ResponseModel(pedido, "Pedido data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Pedido doesn't exist.")


@router.put("/{id}")
async def update_pedido_data(id: str, req: UpdatePedidosModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_pedido = await update_pedido(id, req)
    if updated_pedido:
        return ResponseModel(
            f"Pedido with ID: {id} name update is successful",
            "Pedido name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the pedido data.",
    )
    

@router.delete("/{id}", response_description="Pedido data deleted from the database")
async def delete_pedido_data(id: str):
    deleted_pedido = await delete_pedido(id)
    if deleted_pedido:
        return ResponseModel(
            f"Pedido with ID: {id} removed", "Pedido deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Pedido with id {0} doesn't exist".format(id)
    )