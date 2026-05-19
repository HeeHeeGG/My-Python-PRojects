from pydantic import BaseModel  # tool that validates data going in and out of API

class PasswordCreate(BaseModel):    # data going in expects website name, username, & password
    website: str
    username: str
    password: str

class PasswordResponse(BaseModel):  # data going out of API when reading passwords + id
    id: int
    website: str
    username: str
    password: str

    class Config:
        from_attributes = True  # pydantic can read data from database


# PasswordCreate = order form to fill in
# PasswordResponse = receipt returned 