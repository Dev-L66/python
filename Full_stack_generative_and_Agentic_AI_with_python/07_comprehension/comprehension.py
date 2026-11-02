# menu = ["Pizza", "Burger", "Lasagna", "Coke"]

# order = [item for item in menu if len(item) > 5]

# print(order)

# colors = ["red", "green", "blue", "pink","blue", "brown", "purple", "pink"]

# unique_colors = {color for color in colors}
# print(unique_colors)

# len_colors = {color for color in colors if len(color) > 5}
# print(len_colors)

# recipes = {
#     "Pizza": ["flour", "pepper", "salt", "yeast"],
#     "Burger":["flour", "yeast", "salt"],
#     "Cheesecake":["cheese", "biscuit", "butter"]
# }

# unique_ingredients = {spice for ingredients in recipes.values() for spice in ingredients }

# print(unique_ingredients)

# menu = {
#     "Burger": 30,
#     "Pizza": 50,
#     "Coke": 10
# }


# menu_usd = {item:price/3 for item, price in menu.items()}
# print(menu_usd)


daily_sales = [5,19,30,90,88,55,22]
total= sum(sale for sale in daily_sales if sale > 3)
print(total)