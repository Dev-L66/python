from fastapi import FastAPI
from database import engine
from models import Base
from crud import router as crud_router
from fastapi.midleware.cors import CORSMiddleware
import os
import dotenv

dotenv.load_dotenv()


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("CLIENT_URL")],
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']

)

app.include_router(crud_router, prefix='/todo', tags=["Crud Router"])


@app.get('/')
def home(title: str, description: str):
    return {"message": f"{title}, {description}"}
