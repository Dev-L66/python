from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

product_one = Product(id=1, name="Laptop", price =999.9, in_stock=True)
product_two= Product(id=2, name="Mouse", price =999.9)
# product_three = Product(name="keyboard")

print(product_one)
print(product_two)
# print(product_three)