# import sys
# from fractions import Fraction
# from decimal import Decimal
# # amount = 2
# # print(f"Initial amount: {amount}")

# # amount = 12
# # print(f"Second amount: {amount}")

# # print(f"ID of 2: {id(2)}")
# # print(f"ID of 12: {id(12)}")

# # # numbers are immutable

# # greetings = set()

# # print(f"Before adding: {id(greetings)}")

# # greetings.add("hi")
# # greetings.add("hello")

# # print(greetings)
# # print(f"After adding: {id(greetings)}")

# # sets are mutable





# # numbers - integers,booleans,floating,
# #  complex numbers


# # gold = 14
# # silver = 15

# # total = gold + silver
# # print(f"Total grams: {total}")

# # diff = gold - silver
# # print(f"Total diff: {diff}")


# # coffee = 5
# # servings = 4
# # coffee_per_servings = coffee/servings
# # coffee_per_servings2 = coffee//servings
# # print(f"Coffee per serving: {coffee_per_servings}")
# # print(f"Coffee per serving: {coffee_per_servings2}")

# # total_pods = 10
# # pods_per_cup = 2
# # leftover_pods = total_pods % pods_per_cup
# # print(f"Leftover pods: {leftover_pods}")

# # base_flavor_strength = 2
# # scale_factor = 3
# # powerful_flavor = base_flavor_strength ** scale_factor
# # print(f"Scaled flavor: {powerful_flavor}")

# # total_tea_harvested = 1_000_000_00
# # print(f"Total tea harvested {total_tea_harvested}")

# # is_boiling = True
# # stir_count = 5
# # # upcasting
# # total_actions = stir_count + is_boiling
# # print(f"Total actions: {total_actions}" )

# # milk_present = None
# # print(f"Is there milk? {bool(milk_present)}")

# # water_hot = True
# # tea_added = False

# # can_serve = water_hot and tea_added
# # print(f"Can tea be served? {can_serve}")

# # temp = 95.5
# # cureent_temp = 95.499999
# # print(f"temp {temp}")
# # print(f"current temp {cureent_temp}")
# # print(f"Difference {temp - cureent_temp}")
# # print(sys.float_info)



# # greeting = "hello"
# # name = "Alex"

# # print(f"Greetings: {greeting} {name}")

# # print(name[0])
# # print(name[3])
# # print(name[0:3])
# # print(name[0:4])
# # print(name[0:4:1])
# # print(name[0:4:2])
# # print(name[:4])
# # print(name[2:])
# # print(name[:-1])
# # print(name[::-1])


# # label_text = "Chai spécial"
# # encoded_label = label_text.encode("utf-8")
# # print(label_text)
# # print(encoded_label)
# # decoded_label = encoded_label.decode("utf-8")
# # print(decoded_label)

# # languages = ("Java", "Python","Javascript")
# # (language1, language2, language3) = languages
# # print(languages)
# # print(language1,language2,language3)

# # choco_ratio, coffee_ratio = 2,1
# # print(choco_ratio, coffee_ratio)

# # coffee_ratio, choco_ratio = choco_ratio, coffee_ratio
# # print(choco_ratio, coffee_ratio)


# # print(f"Is Java in languages? {'Java' in languages}")
# # print(f"Is java in languages? {'java' in languages}")
# # print(f"Is C in languages? {'C' in languages}")

# # tuple1= (1, "java", False)
# # print(tuple1)
# # print(type(tuple1))

# # # tuples are immutable

# # # lists are mutable

# # colors = ["red", "purple", "blue"]
# # colors.append("yellow")
# # print(colors)
# # colors.remove("purple")
# # print(colors)

# # things = ["table", "chair"]
# # stationary = ["pen", "pencil"]
# # print(things)
# # print(stationary)

# # things.extend(stationary)
# # print(things)
# # print(things[0])

# # things.insert(2,"eraser")
# # print(things)

# # last_added = things.pop()
# # print(last_added)
# # print(things)
# # things.reverse()
# # print(things)
# # things.sort()
# # print(things)

# # numbers = [1,2,3,4,5]
# # print(max(numbers))
# # print(min(numbers))


# # drinks = ["water", "milk"]
# # flavour = ["vanilla"]

# # mix = drinks + flavour
# # print(mix)

# # black_tea = ["strong"] * 3
# # print(black_tea)

# # black_tea = ["strong", "light"] * 3
# # print(black_tea)

# # word = bytearray(b"WONDERFUL")
# # word = word.replace(b"WONDER", b"BEAUTI")
# # print(word)






# # color_set = {"red", "green", "orange"}
# # color_set2 = {"pink", "green", "yellow"}

# # all_colors = color_set | color_set2
# # print(all_colors)

# # common_colors = color_set & color_set2
# # print(common_colors)

# # only_in_color_Set = color_set - color_set2
# # print(only_in_color_Set)

# # print(f"IS pink in color_set?{"pink" in color_set}")

# order = dict(type="coffee", size="large", sugar=2)
# print(f"Order: {order}")

# recipe = {}
# recipe["base"] = "coffee powder"
# recipe["liquid"] = "Milk"
# print(f"Recipe: {recipe["base"]}")
# del recipe["liquid"]
# print(f"Recipe: {recipe}")
# print(f"Is sugar in order? {"sugar" in order}")

# order2 = {"type": "green tea", "size":"Medium", "sugar":1}
# # print(f"Order details keys: {order2.keys()}")
# # print(f"Order details values: {order2.values()}")
# # print(f"Order details items: {order2.items()}")
# last_item = order2.popitem()
# print(f"Removed last item: {last_item}")
# print(order2)

# extra_flavours = {"carsamom":"crushed", "ginger":"sliced"}
# recipe.update(extra_flavours)
# print(f"Updated recipe: {recipe}")

# order_size = order2["size"]
# print(f"Order size:{order_size}")

# # order_note = order2["customer_note"]
# # print(f"Order note:{order_note}") error

# order_note = order2.get("note", "No note provided")
# print(f"Order note:{order_note}")

# union and intersection are available for dictionaries in python 3.9 and above

# advanced datatypes - datetime, time, calendar, timedelta



# import arrow
# brew_time = arrow.utcnow()
# brew_time.to("Europe")


from collections import namedtuple
profile = namedtuple("profile", ["flavour", "size"])
print(profile)