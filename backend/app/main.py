import uvicorn
from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter()


@router.get("/api/v1")
async def home() -> dict[str, str]:
    return {"hello": "world"}


app.include_router(router)


def start():
    """_summary_

    Launched with 'poetry run start' command at root level
    """
    uvicorn.run("app.main:app", host="localhost", port=8080, reload=True)
