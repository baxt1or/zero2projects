from pydantic import BaseModel, validator

languages = ['English', 'French', 'German', 'Romanian', "Russian"]

class Translation(BaseModel):
    text : str
    base_lang : str 
    final_lang : str 

    @validator('base_lang', 'final_lang')
    def valid_lang(cls, lang):
        if lang not in languages:
            raise ValueError("Invalid language")
        return lang
