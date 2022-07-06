from fastapi import APIRouter, Depends, Request, Response, HTTPException
from fastapi_csrf_protect import CsrfProtect
from sqlalchemy.ext.asyncio import AsyncSession

from api.cruds.crud_auth import db_login, db_signup
from api.database import get_db
from api.schemas.schema_auth import Csrf, SuccessMsg, User, UserBody
from api.utils.auth import AuthJwtCsrf

router = APIRouter()
auth = AuthJwtCsrf()


@router.get('/api/csrftoken', response_model=Csrf)
def get_csrf_token(csrf_protect: CsrfProtect = Depends()):
    csrf_token = csrf_protect.generate_csrf()
    res = {'csrf_token': csrf_token}
    return res


@router.post('/api/register', response_model=User)
async def signup(request: Request, user: UserBody,
    csrf_protect: CsrfProtect = Depends(), db: AsyncSession = Depends(get_db)
):
    csrf_token = csrf_protect.get_csrf_from_headers(request.headers)
    csrf_protect.validate_csrf(csrf_token)
    new_user = await db_signup(db, user)
    return new_user


@router.post('/api/login', response_model=SuccessMsg)
async def login(request: Request, response:  Response, user: UserBody,
    csrf_protect: CsrfProtect = Depends(), db: AsyncSession = Depends(get_db)
):
    csrf_token = csrf_protect.get_csrf_from_headers(request.headers)
    csrf_protect.validate_csrf(csrf_token)
    token = db_login(db, user)
    response.set_cookie(
        key='access_token', value=f'Bearer {token}', httponly=True, samesite='none', secure=True
    )
    return {'message': 'Successfully logged-in'}


@router.post('/api/logout', response_model=SuccessMsg)
async def logout(request: Request, response: Response, csrf_protect: CsrfProtect = Depends()):
    csrf_token = csrf_protect.get_csrf_from_headers(request.headers)
    csrf_protect.validate_csrf(csrf_token)
    response.set_cookie(
        key='access_token', value='', httponly=True, samesite='none', secure=True
    )
    return {'message': 'Successfully logged-out'}


@router.get('/api/user', response_model=User)
async def get_user_refresh_jwt(request: Request, response: Response, csrf_protect: CsrfProtect = Depends()):
    new_token = auth.verify_csrf_update_jwt(
        request, csrf_protect, request.headers
    )
    response.set_cookie(
        key='access_token', value=f'Bearer {new_token}', httponly=True, samesite='none', secure=True
    )
    return {'message': 'user data'}