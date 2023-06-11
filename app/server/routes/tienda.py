from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_tiendas,
    add_tienda,
    retrieve_tienda,
    update_tienda,
    delete_tienda
)

from server.models.tiendas import (
    ErrorResponseModel,
    ResponseModel,
    TiendasSchema,
    UpdateTiendasModel
)

router = APIRouter()

@router.post("/", response_description="Tienda data added into the database")
async def add_tienda_data(tienda: TiendasSchema = Body(...)):
    tienda = jsonable_encoder(tienda)
    new_tienda = await add_tienda(tienda)
    return ResponseModel(new_tienda, "Tienda added successfully.")

@router.get("/", response_description="Tiendas retrieved")
async def get_tiendas():
    tiendas = await retrieve_tiendas()
    if tiendas:
        return ResponseModel(tiendas, "Tiendas data retrieved successfully")
    return ResponseModel(tiendas, "Empty list returned")

@router.get("/{id}", response_description="Tienda data retrieved")
async def get_tienda_data(id):
    tienda = await retrieve_tienda(id)
    if tienda:
        return ResponseModel(tienda, "Tienda data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Tienda doesn't exist.")

@router.put("/{id}")
async def update_tienda_data(id: str, req: UpdateTiendasModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_tienda = await update_tienda(id, req)
    if updated_tienda:
        return ResponseModel(
            f"Tienda with ID: {id} name update is successful",
            "Tienda name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the tienda data.",
    )

@router.delete("/{id}", response_description="Tienda data deleted from the database")
async def delete_tienda_data(id: str):
    deleted_tienda = await delete_tienda(id)
    if deleted_tienda:
        return ResponseModel(
            f"Tienda with ID: {id} removed", "Tienda deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Tienda with id {0} doesn't exist".format(id)
    )

