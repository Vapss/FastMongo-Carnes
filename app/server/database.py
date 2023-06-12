import motor.motor_asyncio
from bson.objectid import ObjectId


MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.proveedores

proveedor_collection = database.get_collection("proveedores_collection")
cliente_collection = database.get_collection("clientes_collection")
pedido_collection = database.get_collection("pedidos_collection")
producto_collection = database.get_collection("productos_collection")
tienda_collection = database.get_collection("tiendas_collection")

# helpers


def proveedor_helper(proveedor) -> dict:
    return {
        "id": str(proveedor["_id"]),
        "ProveedorId": proveedor["ProveedorId"],
        "Nombre": proveedor["Nombre"],
        "Telefono": proveedor["Telefono"],
        "Email": proveedor["Email"],
        "Estado": proveedor["Estado"],
    }

def cliente_helper(cliente) -> dict:
    return {    
            "id": str(cliente["_id"]),
            "ClienteId": cliente["ClienteId"],
            "Telefono": cliente["Telefono"],
            "Nombre": cliente["Nombre"],
            "Email": cliente["Email"],
            "Direccion": cliente["Direccion"],
            "Estado": cliente["Estado"],
    }

def pedido_helper(pedido) -> dict:
    return {
        "id": str(pedido["_id"]),
        "PedidoId": pedido["PedidoId"],
        "Cliente": pedido["Cliente"],
        "Proveedor": pedido["Proveedor"],
        "Tienda": pedido["Tienda"],
        "Producto": pedido["Producto"],
        "CantidadKG": pedido["CantidadKG"],
        "Fecha_pedido": pedido["Fecha_pedido"],
        "Fecha_entrega": pedido["Fecha_entrega"],
    }

def producto_helper(producto) -> dict:
    return {
        "id": str(producto["_id"]),
        "ProductoId": producto["ProductoId"],
        "Nombre": producto["Nombre"],
        "Precio": producto["Precio"],
        "PesoKG": producto["PesoKG"],
        "Distribuidor": producto["Distribuidor"],
        "Tienda": producto["Tienda"],
    }

def tienda_helper(tiendas) -> dict:
    return {
        "id": str(tiendas["_id"]),
        "TiendaId": tiendas["TiendaId"],
        "Nombre": tiendas["Nombre"],
        "Direccion": tiendas["Direccion"],
        "Estado": tiendas["Estado"],
        "Distribuidor": tiendas["Distribuidor"],
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


# Pedidos Collection
async def retrieve_pedidos():
    pedidos = []
    async for pedido in pedido_collection.find():
        pedidos.append(pedido_helper(pedido))
    return pedidos

# Add a new pedido into to the database
async def add_pedido(pedido_data: dict) -> dict:
    pedido = await pedido_collection.insert_one(pedido_data)
    new_pedido = await pedido_collection.find_one({"_id": pedido.inserted_id})
    return pedido_helper(new_pedido)

# Retrieve a pedido with a matching ID
async def retrieve_pedido(id: str) -> dict:
    pedido = await pedido_collection.find_one({"_id": ObjectId(id)})
    if pedido:
        return pedido_helper(pedido)

# Retrieve pedido with agreggate function
async def retrieve_pedido_aggregate() :
    pipeline = [
        {
            '$lookup': {
                'from': 'productos_collection', 
                'localField': 'Producto', 
                'foreignField': 'ProductoId', 
                'as': 'Producto'
            }
        }, {
            '$unwind': {
                'path': '$Producto', 
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$lookup': {
                'from': 'proveedores_collection', 
                'localField': 'Proveedor', 
                'foreignField': 'ProveedorId', 
                'as': 'Proveedor'
            }
        }, {
            '$unwind': {
                'path': '$Proveedor', 
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$lookup': {
                'from': 'clientes_collection', 
                'localField': 'Cliente', 
                'foreignField': 'ClienteId', 
                'as': 'Cliente'
            }
        }, {
            '$unwind': {
                'path': '$Cliente', 
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$lookup': {
                'from': 'tiendas_collection', 
                'localField': 'Tienda', 
                'foreignField': 'TiendaId', 
                'as': 'Tienda'
            }
        }, {
            '$unwind': {
                'path': '$Tienda', 
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$project': {
                'Cliente': '$Cliente.Nombre', 
                'Proveedor': '$Proveedor.Nombre', 
                'Tienda': '$Tienda.Nombre', 
                'Producto': '$Producto.Nombre', 
            }
        }
    ]
    pedidos = []
    async for pedido in pedido_collection.aggregate(pipeline):
        pedidos.append(pedido)
    return pedidos

# Update a pedido with a matching ID
async def update_pedido(id: str, data: dict):
    # Return false if an empty request body is sent.
    if not data:
        return False
    pedido = await pedido_collection.find_one({"_id": ObjectId(id)})
    if pedido:
        update_pedido = await pedido_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        return bool(update_pedido)

# Delete a pedido from the database
async def delete_pedido(id: str):
    pedido = await pedido_collection.find_one({"_id": ObjectId(id)})
    if pedido:
        await pedido_collection.delete_one({"_id": ObjectId(id)})
        return True

# Productos Collection
async def retrieve_productos():
    productos = []
    async for producto in producto_collection.find():
        productos.append(producto_helper(producto))
    return productos

# Add a new producto into to the database
async def add_producto(producto_data: dict) -> dict:
    producto = await producto_collection.insert_one(producto_data)
    new_producto = await producto_collection.find_one({"_id": producto.inserted_id})
    return producto_helper(new_producto)

# Retrieve a producto with a matching ID
async def retrieve_producto(id: str) -> dict:
    producto = await producto_collection.find_one({"_id": ObjectId(id)})
    if producto:
        return producto_helper(producto)

# Update a producto with a matching ID
async def update_producto(id: str, data: dict):
    # Return false if an empty request body is sent.
    if not data:
        return False
    producto = await producto_collection.find_one({"_id": ObjectId(id)})
    if producto:
        update_producto = await producto_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        return bool(update_producto)

# Delete a producto from the database
async def delete_producto(id: str):
    producto = await producto_collection.find_one({"_id": ObjectId(id)})
    if producto:
        await producto_collection.delete_one({"_id": ObjectId(id)})
        return True

# Tiendas Collection
async def retrieve_tiendas():
    tiendas = []
    async for tienda in tienda_collection.find():
        tiendas.append(tienda_helper(tienda))
    return tiendas

# Add a new tienda into to the database
async def add_tienda(tienda_data: dict) -> dict:
    tienda = await tienda_collection.insert_one(tienda_data)
    new_tienda = await tienda_collection.find_one({"_id": tienda.inserted_id})
    return tienda_helper(new_tienda)

# Retrieve a tienda with a matching ID
async def retrieve_tienda(id: str) -> dict:
    tienda = await tienda_collection.find_one({"_id": ObjectId(id)})
    if tienda:
        return tienda_helper(tienda)

# Update a tienda with a matching ID
async def update_tienda(id: str, data: dict):
    # Return false if an empty request body is sent.
    if not data:
        return False
    tienda = await tienda_collection.find_one({"_id": ObjectId(id)})
    if tienda:
        update_tienda = await tienda_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        return bool(update_tienda)

# Delete a tienda from the database
async def delete_tienda(id: str):
    tienda = await tienda_collection.find_one({"_id": ObjectId(id)})
    if tienda:
        await tienda_collection.delete_one({"_id": ObjectId(id)})
        return True