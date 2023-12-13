from pydantic import BaseModel 


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str


class UserInDB(User):
    hashed_password: str


class Currencies(BaseModel): 
    success: bool 
    query: dict 
    info: dict 
    result: int | float


class ErrorCurrencies(BaseModel): 
    success: bool 
    error: dict 







