from sqlite3 import connect
from  fastapi import APIRouter

from models.mdlob import LineOfBusiness
from config.database import connection

mdlob = APIRouter()

@mdlob.get('/mdlob')
async def find_all_documents():
    return connection.devPhoenixDB.md_line_of_business.find()
