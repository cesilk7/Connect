from typing import Union

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api.utils.auth import AuthJwtCsrf
from api.models import model_user
from api.schemas import schema_auth

auth = AuthJwtCsrf()


async def db_signup(
    db: AsyncSession, user_info: schema_auth.UserBody
) -> model_user:
    email = user_info.email
    password = user_info.password

    overlap_user: Result = (await db.execute(
        select(model_user.User).filter(model_user.User.email == email)
    )).scalars().first()
    if overlap_user:
        raise HTTPException(status_code=400, detail='Email is already taken')
    if not password or len(password) < 8:
        raise HTTPException(status_code=400, detail='Password too short')

    user = model_user.User(
        email=email, password=auth.generate_hashed_pw(password)
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def db_login(
    db: AsyncSession, user_info: schema_auth.UserBody
) -> model_user.User:
    email = user_info.email
    password = user_info.password

    user: Result = (await db.execute(
        select(model_user.User).filter(model_user.User.email == email)
    )).first()

    if not user or not auth.verify_pw(password, user.password):
        raise HTTPException(status_code=401, detail='Invalid email or password')
    token = auth.encode_jwt(user.email)
    return token
