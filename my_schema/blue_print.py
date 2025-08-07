from pydantic import BaseModel

class PoemSchema(BaseModel):
    title: str
    content: str
    short_summary:str