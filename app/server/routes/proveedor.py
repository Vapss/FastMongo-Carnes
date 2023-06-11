from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_proveedores,
    add_proveedor,
    retrieve_proveedor,
    update_proveedor,
    delete_proveedor
)

from server.models.proveedores import (
    ErrorResponseModel,
    ResponseModel,
    ProveedoresSchema,
    UpdateProveedoresModel,
)

router = APIRouter()

@router.post("/", response_description="Proveedor data added into the database")
async def add_proveedor_data(proveedor: ProveedoresSchema = Body(...)):
    proveedor = jsonable_encoder(proveedor)
    new_proveedor = await add_proveedor(proveedor)
    return ResponseModel(new_proveedor, "Proveedor added successfully.")

@router.get("/", response_description="Proveedores retrieved")
async def get_proveedores():
    proveedores = await retrieve_proveedores()
    if proveedores:
        return ResponseModel(proveedores, "Proveedores data retrieved successfully")
    return ResponseModel(proveedores, "Empty list returned")

@router.get("/{id}", response_description="Proveedor data retrieved")
async def get_proveedor_data(id):
    proveedor = await retrieve_proveedor(id)
    if proveedor:
        return ResponseModel(proveedor, "Proveedor data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Proveedor doesn't exist.")

@router.put("/{id}")
async def update_proveedor_data(id: str, req: UpdateProveedoresModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_proveedor = await update_proveedor(id, req)
    if updated_proveedor:
        return ResponseModel(
            f"Proveedor with ID: {id} name update is successful",
            "Proveedor name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the proveedor data.",
    )

@router.delete("/{id}", response_description="Proveedor data deleted from the database")
async def delete_proveedor_data(id: str):
    deleted_proveedor = await delete_proveedor(id)
    if deleted_proveedor:
        return ResponseModel(
            f"Proveedor with ID: {id} removed", "Proveedor deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Proveedor with id {0} doesn't exist".format(id)
    )
    