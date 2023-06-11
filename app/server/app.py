from fastapi import FastAPI

from server.routes.proveedor import router as ProveedorRouter
from server.routes.cliente import router as ClienteRouter

app = FastAPI()

app.include_router(ProveedorRouter, tags=["Proveedor"], prefix="/proveedor")

app.include_router(ClienteRouter, tags=["Cliente"], prefix="/cliente")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}