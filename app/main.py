from fastapi import FastAPI
import uvicorn

#app creation using FastAPI
app = FastAPI()

@app.get("/")
async def root():
    name = "Vijay"
    return {"message": f"Hello {name}"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": int(item_id)}

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")