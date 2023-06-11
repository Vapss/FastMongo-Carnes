import motor.motor_asyncio
from bson.objectid import ObjectId


MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.proveedores

proveedor_collection = database.get_collection("proveedores_collection")

# helpers


def proveedor_helper(proveedor) -> dict:
    return {
        "id": str(proveedor["_id"]),
        "Nombre": proveedor["Nombre"],
        "Telefono": proveedor["Telefono"],
        "Email": proveedor["Email"],
        "Estado": proveedor["Estado"],
    }

# CRUD Operations

# Retrieve all proveedores present in the database
async def retrieve_proveedores():
    proveedores = []
    async for proveedor in proveedor_collection.find():
        proveedores.append(proveedor_helper(proveedor))
    return proveedores

# Add a new proveedor into to the database
async def add_proveedor(proveedor_data: dict) -> dict:
    proveedor = await proveedor_collection.insert_one(proveedor_data)
    new_proveedor = await proveedor_collection.find_one({"_id": proveedor.inserted_id})
    return proveedor_helper(new_proveedor)

# Retrieve a proveedor with a matching ID
async def retrieve_proveedor(id: str) -> dict:
    proveedor = await proveedor_collection.find_one({"_id": ObjectId(id)})
    if proveedor:
        return proveedor_helper(proveedor)

# Update a proveedor with a matching ID
async def update_proveedor(id: str, data: dict):
    # Return false if an empty request body is sent.
    if not data:
        return False
    proveedor = await proveedor_collection.find_one({"_id": ObjectId(id)})
    if proveedor:
        update_proveedor = await proveedor_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        return bool(update_proveedor)

# Delete a proveedor from the database
async def delete_proveedor(id: str):
    proveedor = await proveedor_collection.find_one({"_id": ObjectId(id)})
    if proveedor:
        await proveedor_collection.delete_one({"_id": ObjectId(id)})
        return True
