import motor.motor_asyncio
from bson.objectid import ObjectId


MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.proveedores

proveedor_collection = database.get_collection("proveedores_collection")
cliente_collection = database.get_collection("clientes_collection")

# helpers


def proveedor_helper(proveedor) -> dict:
    return {
        "id": str(proveedor["_id"]),
        "Nombre": proveedor["Nombre"],
        "Telefono": proveedor["Telefono"],
        "Email": proveedor["Email"],
        "Estado": proveedor["Estado"],
    }

def cliente_helper(cliente) -> dict:
    return {    
            "id": str(cliente["_id"]),
            "Telefono": cliente["Telefono"],
            "Nombre": cliente["Nombre"],
            "Email": cliente["Email"],
            "Direccion": cliente["Direccion"],
            "Estado": cliente["Estado"],
    }

# CRUD Operations

# Proveedores Collection
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

# Clientes Collection
async def retrieve_clientes():
    clientes = []
    async for cliente in cliente_collection.find():
        clientes.append(cliente_helper(cliente))
    return clientes

# Add a new cliente into to the database
async def add_cliente(cliente_data: dict) -> dict:
    cliente = await cliente_collection.insert_one(cliente_data)
    new_cliente = await cliente_collection.find_one({"_id": cliente.inserted_id})
    return cliente_helper(new_cliente)

# Retrieve a cliente with a matching ID
async def retrieve_cliente(id: str) -> dict:
    cliente = await cliente_collection.find_one({"_id": ObjectId(id)})
    if cliente:
        return cliente_helper(cliente)

# Update a cliente with a matching ID
async def update_cliente(id: str, data: dict):
    # Return false if an empty request body is sent.
    if not data:
        return False
    cliente = await cliente_collection.find_one({"_id": ObjectId(id)})
    if cliente:
        update_cliente = await cliente_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        return bool(update_cliente)

# Delete a cliente from the database
async def delete_cliente(id: str):
    cliente = await cliente_collection.find_one({"_id": ObjectId(id)})
    if cliente:
        await cliente_collection.delete_one({"_id": ObjectId(id)})
        return True