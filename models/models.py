from datetime import datetime

from fastapi import File
from sqlalchemy import Table, Column, String, Integer, Text, Boolean, MetaData, TIMESTAMP, Date, ForeignKey, Float

metadata = MetaData()

movie = Table(
    'movie',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('description', Text),
    Column('seen', Integer, default=0),
    Column('posted_at', TIMESTAMP, default=datetime.utcnow),
    Column('like', Integer, default=0),
    Column('price', Float, default=0),
    Column('video', String),
    Column('hash', String, unique=True),
    Column('video_url',String),
)


category = Table(
    'category',
    metadata,
    Column('id',Integer,primary_key=True,autoincrement=True),
    Column('name',String)
)


category_movie = Table(
    'category_movie',
    metadata,
    Column('id',Integer,primary_key=True,autoincrement=True),
    Column('movie_id',Integer,ForeignKey('movie.id')),
    Column('category_id',Integer,ForeignKey('category.id'))
)