from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import Dict
from logging_config import get_logger

logger = get_logger(__name__)

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login", status_code=status.HTTP_200_OK)
async def login(request: LoginRequest) -> Dict[str, str]:
    logger.info("User login attempt")
    if request.username == "admin" and request.password == "password":
        return {"token": "fake-jwt-token"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

# Logout endpoint example
@router.post("/logout", status_code=status.HTTP_200_OK)
async def logout():
    logger.info("User logged out")
    return {"message": "Successfully logged out"}
