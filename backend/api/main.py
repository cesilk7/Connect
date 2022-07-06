from re import I
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi_csrf_protect import CsrfProtect
from fastapi_csrf_protect.exceptions import CsrfProtectError

from api.routers import route_place, route_visited, route_auth
from api.schemas.schema_auth import Csrf, SuccessMsg, CsrfSettings


app = FastAPI()
app.include_router(route_place.router)
app.include_router(route_visited.router)
app.include_router(route_auth.router)
origins = ['http://localhost:3000']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@CsrfProtect.load_config
def get_csrf_config():
    return CsrfSettings()


@app.exception_handler(CsrfProtectError)
def csrf_protect_exception_handler(request: Request, exc: CsrfProtectError):
    return JSONResponse(
        status_code=exc.status_code,
        content={'detail':  exc.message}
    )


@app.get('/hello')
async def hello():
    return {'message': 'hello world!'}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
    