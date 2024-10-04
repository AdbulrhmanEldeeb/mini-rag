from fastapi import FastAPI , APIRouter , Depends , UploadFile 
import os 
from controllers import DataController 
data_router=APIRouter(prefix='/api/v1/data',
                      tags=['api_v1','data'])
from helpers.config import get_settings , Settings 

@data_router.post('/upload/{project_id}')
async def upload_data(project_id:str, file:UploadFile ,app_settings : Settings =Depends(get_settings)): 
    
    is_valid=DataController().validate_uploaded_file(file=file)
    return is_valid 