from typing import Any, Dict, Optional
from fastapi import APIRouter


demo_router = APIRouter()


@demo_router.get("/")
def root() -> Dict[str, Any]:
    return {"Here": "is a demo route"}


@demo_router.get("/items/{id}")
def demo_query_params(id: int, q: Optional[str] = None) -> Dict[str, Any]:
    return {"id": id, "q": q}
