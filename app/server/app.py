from fastapi import FastAPI

from server.routes.proveedor import router as ProveedorRouter
from server.routes.cliente import router as ClienteRouter
from server.routes.pedido import router as PedidoRouter
from server.routes.producto import router as ProductoRouter
from server.routes.tienda import router as TiendaRouter

app = FastAPI()

app.include_router(ProveedorRouter, tags=["Proveedor"], prefix="/proveedor")

app.include_router(ClienteRouter, tags=["Cliente"], prefix="/cliente")

app.include_router(PedidoRouter, tags=["Pedido"], prefix="/pedido")

app.include_router(ProductoRouter, tags=["Producto"], prefix="/producto")

app.include_router(TiendaRouter, tags=["Tienda"], prefix="/tienda")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}