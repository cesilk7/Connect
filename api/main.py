import uvicorn
from fastapi import FastAPI

from api.routers import place, visited


app = FastAPI()
app.include_router(place.router)
app.include_router(visited.router)


@app.get('/hello')
async def hello():
    return {'message': 'hello world!'}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
    