from fastapi import FastAPI
import uvicorn

from app.api import user

app = FastAPI()

app.include_router(user.router)

if __name__ == "__main__":
    uvicorn.run(app)
