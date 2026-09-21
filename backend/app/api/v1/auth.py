from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.core.security import create_access_token

router = APIRouter()

@router.post("/login")
async def login(user: User):
    # Dummy authentication
    if user.email == "admin@example.com" and user.password == "password":
        token = create_access_token({"email": user.email})
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")

