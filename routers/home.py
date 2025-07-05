from fastapi import APIRouter, Depends, HTTPException

home_router = APIRouter()
@home_router.get("/", response_model=str)
def hello_world():
    return "Hello World!"
