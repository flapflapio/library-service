from fastapi import FastAPI
from .routers.demo_router import demo_router


app = FastAPI()
app.include_router(demo_router)


