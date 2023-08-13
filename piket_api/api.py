from fastapi import APIRouter

router = APIRouter()


@router.post('/api/{id}')
async def read_api():
    return {
        "key": "Test",
    }
