from fastapi import FastAPI

from server.routes.proveedor import router as ProveedorRouter

app = FastAPI()

app.include_router(ProveedorRouter, tags=["Proveedor"], prefix="/proveedor")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}