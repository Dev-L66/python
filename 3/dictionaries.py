fruits = {"apple":"red", "banana":"yellow", "cherry":"red", 1:True}
print(fruits)

print(fruits.keys())
print(fruits["apple"])
print(fruits.get("apple"))
# print(fruits.get("ginger")) None
# print(fruits["ginger"]) error

fruits["apple"] = "green"
print(fruits)

for fruit in fruits:
    print(fruit)

for fruit in fruits:
    print(fruits[fruit])

for key, value in fruits.items():
    print(key, value)

if "apple" in fruits:
    print("yes")
else:
    print("no")


print(len(fruits))
fruits["kiwi"]= "green"
print(fruits)
fruits.pop("kiwi")
print(fruits)
fruits.popitem()
print(fruits)
del fruits["apple"]
print(fruits)

fruits_copy = fruits.copy()
fruits_copy2 = fruits
print(fruits)
print(fruits_copy)
print(fruits_copy2)
fruits["apple"] = "red"
print(fruits)
print(fruits_copy)
print(fruits_copy2)


shop = {"fruits":{"apple": "red", "banana": "yellow", "cherry": "red"}, "vegetables": {"carrot": "orange", "spinach": "green"}}
print(shop)
print(shop["fruits"])
print(shop["fruits"]["apple"])
print(shop["vegetables"])
print(shop["vegetables"]["spinach"])


squared_nums = {x:x**2 for x in range(10)}
print(squared_nums)
squared_nums.clear()
print(squared_nums)


keys = ["apple", "orange", "mango"]
values = "red"

new_dict = dict.fromkeys(keys, values)
print(new_dict)
new_dict2 = dict.fromkeys(keys, keys)
print(new_dict2)