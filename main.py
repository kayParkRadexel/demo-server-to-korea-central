from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "Hello World, this is server in Korea Central"
