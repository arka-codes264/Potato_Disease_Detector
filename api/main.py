from fastapi import FastAPI
# import uvicorn


app = FastAPI()

@app.get("/ping")
async def ping():
    return "Hello, I am alive"


if __name__ == "__main__":
    uvicorn.run(app, host = 'localhost', port = 8000)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)