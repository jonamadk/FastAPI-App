from fastapi import FastAPI
from routes.mdlob import mdlob , test

app = FastAPI()
app.include_router(mdlob)
app.include_router(test)
