from fastapi import APIRouter

router = APIRouter(
    prefix="/admin",
    tags=["Internal"],
)

@router.get("/")
async def get_admin():
    return {"message": "Admin internal area"}

