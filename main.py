import os
import secrets
from datetime import datetime, timedelta
from typing import List

import aiofiles
from fastapi import FastAPI, APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import FileResponse

from database import get_async_session
from models.models import movie, category, category_movie
from schemes import MovieList, MovieAdd, AddCategory, ListCategory, AddCategoryMovie

app = FastAPI(title="Group")
router = APIRouter()


@app.get('/movies', response_model=List[MovieList])
async def get_movies(session: AsyncSession = Depends(get_async_session)):
    query = select(movie)
    result = await session.execute(query)
    movies = result.all()
    datas = []
    for movie_data in movies:
        print(movie_data)

        data = {
            "id": movie_data.id,
            "name": movie_data.name,
            "description": movie_data.description,
            "seen": movie_data.seen,
            "posted_at": movie_data.posted_at,
            "like": movie_data.like,
            "price": movie_data.price
        }
        datas.append(data)
    return datas


@app.get('/movies/premiere', response_model=List[MovieList])
async def premiere(session: AsyncSession = Depends(get_async_session)):
    ten_days_ago = datetime.utcnow() - timedelta(days=10)
    query = select(movie).where(movie.c.posted_at >= ten_days_ago)
    res = await session.execute(query)
    print(res)
    movie_data = res.fetchall()
    print(movie_data)
    return movie_data


class CustomHTTPException(HTTPException):
    def __init__(self, status_code: int, detail: str = None, headers: dict = None, **kwargs):
        super().__init__(status_code, detail, headers, **kwargs)
        # Remove the non-serializable exception instance from the error response
        self.detail = str(detail)


@router.post('/upload-movie')
async def upload_file(
        upload__file: UploadFile,
        data: MovieAdd = Depends(),
        session: AsyncSession = Depends(get_async_session)
):
    try:
        out_file = f'Videos/{upload__file.filename}'
        async with aiofiles.open(f'{out_file}', 'wb') as f:
            content = await upload__file.read()
            await f.write(content)
        hashcode = secrets.token_hex(32)
        query = insert(movie).values(**dict(data), hash=hashcode, video_url=out_file)
        await session.execute(query)
        await session.commit()
    except FileNotFoundError as e:
        raise CustomHTTPException(status_code=400, detail=f"File not found: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {'success': True, 'message': 'Uploaded successfully'}


@app.get('/download-movie/{hashcode}')
async def download_movie(hashcode: str, session: AsyncSession = Depends(get_async_session)):
    if hashcode is None:
        raise HTTPException(status_code=400, detail="Invalid hashcode")

    query = select(movie).where(movie.c.hash == hashcode)
    file_data = await session.execute(query)
    movie_data = file_data.fetchone()

    if movie_data is None:
        raise HTTPException(status_code=404, detail="Movie not found")

    file_url = movie_data.video_url
    file_name = file_url.split('/')[-1]

    return FileResponse(path=file_url, media_type="application/octet-stream", filename=file_name)


@app.post('/category/add')
async def add_category(
        categoryAdd: AddCategory,
        session: AsyncSession = Depends(get_async_session)
):
    query = insert(category).values(**dict(categoryAdd))
    await session.execute(query)
    await session.commit()
    return {'success': True, 'message': 'Added successfully'}


@app.get('/category/list', response_model=List[ListCategory])
async def list_category(session: AsyncSession = Depends(get_async_session)):
    query = select(category)
    res = await session.execute(query)
    result = res.all()
    return result


@app.post('/movies/category')
async def add_movie_category(
        blog: AddCategoryMovie,
        session: AsyncSession = Depends(get_async_session)
):
    query = insert(category_movie).values(**dict(blog))
    await session.execute(query)
    await session.commit()
    return {"success": True, "message": "Added successfully"}


app.include_router(router)
