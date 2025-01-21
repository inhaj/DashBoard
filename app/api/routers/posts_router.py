from fastapi import APIRouter

router = APIRouter()

# 게시글 생성
@router.post("/")
async def create():
    return 0

# 게시글 조회
@router.get("/{post_id}")
async def create():
    return 0

# 게시글 리스트 조회
@router.get("/")
async def create():
    return 0

# 게시글 수정
@router.put("/{post_id}")
async def create():
    return 0

# 게시글 삭제
@router.delete("/{post_id}")
async def create():
    return 0