from .BaseController import BaseController 
from fastapi import UploadFile 

class DataController(BaseController): 
    def __init__(self):
        super().__init__()
        self.size_scale=1048576
    async def validate_uploaded_file(self, file: UploadFile):
        content = await file.read()  # Read the file content
        file_size = len(content)  # Get the file size in bytes

        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False

        if file_size > self.size_scale * int(self.app_settings.FILE_MAX_SIZE):
            return False

        return True