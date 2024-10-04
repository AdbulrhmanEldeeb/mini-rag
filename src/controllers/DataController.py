from .BaseController import BaseContoller 
from fastapi import UploadFile 

class DataContoller(BaseContoller): 
    def __init__(self):
        super().__init__()

    def validate_uploaded_file(self, file : UploadFile): 
        pass 