names = [
    "Ali",
    "Hal",
    "Alex",
    "Alan",
    "Ali",
    "Hal"
]


unique_names = {name for name in names}
print(unique_names)

unique_names = {name for name in names if len(name)>3}
print(unique_names)


recipes = {
    "MAsala chai": ["ginger","cardamom", "clove"],
    "elaichi chai":["cardamom", "milk"],
    "spicy chai":["ginger", "black pepper", "clove"]
}


uniqe_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(uniqe_spices)