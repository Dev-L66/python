# Dictionary 

fruits = dict(type="apple", size="large", sugar="2")
print(f"{fruits}")


recipe = {}
recipe["base"] = "tea"
recipe["liquid"] = "coffee"
print(f"Recipe:{recipe['base']}")
print(recipe)
del recipe["base"]
print(f"del Recipe:{recipe}")
print(f"Is tea in recipe? {'tea' in recipe}")


fruits = {"type":"apple", "size":"large", "sugar":"2"}
print(fruits)

print(f"order details (keys) {fruits.keys()}")
print(f"order details (values) {fruits.values()}")
print(f"order details (items) {fruits.items()}")


last = fruits.popitem()
print(f"removed last item {last}")

veg = {"onion": "pizza", "tomato": "sliced"}

recipe.update(veg)

print(f"Updated recipe: {recipe}")

recipe_size = fruits["size"]
print(recipe_size)

# recipe_order = fruits["order"] error
# print(recipe_size)

recipe_note = fruits.get("note", "No note")
print(recipe_note)



# union, intersection and all that can be peroformed on sets can be performed on dict