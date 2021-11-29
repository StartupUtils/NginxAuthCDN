from fastapi import FastAPI, Request
from pydantic import BaseModel


class Item(BaseModel):
    token: str

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "test"}

@app.get("/token")
async def token(request: Request):

    return {"ok": True}