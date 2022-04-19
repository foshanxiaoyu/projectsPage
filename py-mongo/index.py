from  fastapi  import FastAPI
from routes.userRouter import uroute

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:7000",
]



app.include_router(uroute)
