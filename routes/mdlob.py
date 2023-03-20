
from  fastapi import APIRouter
from models.mdlob import LineOfBusiness
from config.database import connection
from schemas.mdlob import line_of_business_entity, line_of_business_entities
mdlob= APIRouter()
test = APIRouter()



@test.get('/')
async def hello():
    return {"hi":"Hellow"}

@mdlob.get('/mdlob/docs')
async def find_all_documents():
    return   line_of_business_entities(connection.devPhoenixDB.md_line_of_business.find())



@mdlob.post('/mdlob/create/')
async def create_md_lob(new_mdlob_doc:LineOfBusiness ):
    new_doc = connection.devPhoenixDB.md_line_of_business.insert_one(dict(new_mdlob_doc))
    
    return line_of_business_entities(connection.devPhoenixDB.md_line_of_business.find())
