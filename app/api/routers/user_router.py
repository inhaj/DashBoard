from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.mysql.session import get_db  



router = APIRouter()

@router.post("/signup")
async def create(db: Session = Depends(get_db)):
    return 0

@router.post("/login")
async def create(db: Session = Depends(get_db)):
    return 0

@router.post("/refresh")
async def create(db: Session = Depends(get_db)):
    return 0

@router.post("/logout")
async def create(db: Session = Depends(get_db)):
    return 0