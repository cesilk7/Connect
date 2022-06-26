import uvicorn
from fastapi import FastAPI

from api.routers import route_place, route_visited


app = FastAPI()
app.include_router(route_place.router)
app.include_router(route_visited.router)


@app.get('/hello')
async def hello():
    return {'message': 'hello world!'}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
    