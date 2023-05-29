from pydantic import BaseModel, validator


class UserCreate(BaseModel):
    name: str

    @validator('name')
    def correct_name(cls, v):
        if v == '':
            raise ValueError('Имя должно содержать как минимум одну букву')
        return v
