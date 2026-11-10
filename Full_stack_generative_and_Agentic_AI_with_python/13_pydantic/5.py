from pydantic import BaseModel, field_validator

class User(BaseModel):
    username: str

    @field_validator('username')
    def username(cls, v):
        if len(v) > 4:
            raise ValueError("Username must be at east 4 characters")
        return v


class SignupData(BaaseModel):
    password:str
    confirm_password: str

    @model_validator(mode='after')
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("Passwor dom't match")
        return values