from typing import Optional, List
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

address = Address(
    street="123 blah blah",
    city="jsdjna",
    postal_code="253523"
)

user = User(
id = 1,
name="Alex",
address=address
)


user_data={
    "id": 1,
    "name": "Alex",
    "address":{
        "street":"gwrgewr",
        "city":"jsdnfjn",
        "postal_code":"43534"
    }
}


user = User(**user_data)
print(user)