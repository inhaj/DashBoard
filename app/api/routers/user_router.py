from fastapi import APIRouter

router = APIRouter()

@router.post("/signup")
async def create():
    return 0

@router.post("/login")
async def create():
    return 0

@router.post("/refresh")
async def create():
    return 0

@router.post("/logout")
async def create():
    return 0