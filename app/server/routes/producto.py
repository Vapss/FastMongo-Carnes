from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_producto,
    delete_producto,
    retrieve_producto,
    retrieve_productos,
    update_producto,
)

from server.models.productos import (
    ErrorResponseModel,
    ResponseModel,
    ProductosSchema,
    UpdateProductosModel
)

router = APIRouter()

@router.post("/", response_description="Producto data added into the database")
async def add_producto_data(producto: ProductosSchema = Body(...)):
    producto = jsonable_encoder(producto)
    new_producto = await add_producto(producto)
    return ResponseModel(new_producto, "Producto added successfully.")

@router.get("/", response_description="Productos retrieved")
async def get_productos():
    productos = await retrieve_productos()
    if productos:
        return ResponseModel(productos, "Productos data retrieved successfully")
    return ResponseModel(productos, "Empty list returned")

@router.get("/{id}", response_description="Producto data retrieved")
async def get_producto_data(id):
    producto = await retrieve_producto(id)
    if producto:
        return ResponseModel(producto, "Producto data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Producto doesn't exist.")

@router.put("/{id}")
async def update_producto_data(id: str, req: UpdateProductosModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_producto = await update_producto(id, req)
    if updated_producto:
        return ResponseModel(
            f"Producto with ID: {id} name update is successful",
            "Producto name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the producto data.",
    )

@router.delete("/{id}", response_description="Producto data deleted from the database")
async def delete_producto_data(id: str):
    deleted_producto = await delete_producto(id)
    if deleted_producto:
        return ResponseModel(
            f"Producto with ID: {id} removed",
            "Producto deleted successfully",
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Producto with id {0} doesn't exist".format(id)
    )
