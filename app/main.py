from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.core.database import Base
from app.core.database import engine

from app.routers.product import router

Base.metadata.create_all(bind=engine)

# app = FastAPI()
# app = FastAPI(
#     docs_url="/docs",
#     openapi_url="/openapi.json"
# )
app = FastAPI(
    title="Microservice One",
    root_path="/one"
)

app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message":"FastAPI Product API"
    }