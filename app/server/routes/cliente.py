from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_clientes,
    add_cliente,
    retrieve_cliente,
    update_cliente,
    delete_cliente
)

from server.models.clientes import (
    ErrorResponseModel,
    ResponseModel,
    ClientesSchema,
    UpdateClientesModel
)

router = APIRouter()

@router.post("/", response_description="Cliente data added into the database")
async def add_cliente_data(cliente: ClientesSchema = Body(...)):
    cliente = jsonable_encoder(cliente)
    new_cliente = await add_cliente(cliente)
    return ResponseModel(new_cliente, "Cliente added successfully.")

@router.get("/", response_description="Clientes retrieved")
async def get_clientes():
    clientes = await retrieve_clientes()
    if clientes:
        return ResponseModel(clientes, "Clientes data retrieved successfully")
    return ResponseModel(clientes, "Empty list returned")

@router.get("/{id}", response_description="Cliente data retrieved")
async def get_cliente_data(id):
    cliente = await retrieve_cliente(id)
    if cliente:
        return ResponseModel(cliente, "Cliente data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Cliente doesn't exist.")

@router.put("/{id}")
async def update_cliente_data(id: str, req: UpdateClientesModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_cliente = await update_cliente(id, req)
    if updated_cliente:
        return ResponseModel(
            f"Cliente with ID: {id} name update is successful",
            "Cliente name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the cliente data.",
    )
    

@router.delete("/{id}", response_description="Cliente data deleted from the database")
async def delete_cliente_data(id: str):
    deleted_cliente = await delete_cliente(id)
    if deleted_cliente:
        return ResponseModel(
            f"Cliente with ID: {id} removed", "Cliente deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Cliente with id {0} doesn't exist".format(id)
    )