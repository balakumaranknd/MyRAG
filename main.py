from fastapi import FastAPI
from endpoints import router  # adjust if file name differs

app = FastAPI()

app.include_router(router)