users = [
    {"id": 1,
     "total":100,
     "coupon":"p20"},
      {"id": 2,
          "total":200,
          "coupon":"f20"},
           {"id": 3,
               "total":300,
               "coupon":"g20"}
          
     
]


print(users)

discounts = {
    "p20": (0.2,0),
    "f20": (0.5,0),
    "g20":(0,10)}


for user in users:
    percent, fixed = discounts.get(user["coupon"], (0,0))
    discount = user["total"] * percent + fixed
    print(f"{user["id"]} paid {user["total"]} and discount of {discount}")