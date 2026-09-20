# comprehension is way to create lists, sets, dictionaries or generators using single line of code

#  seen in filtering item, tranforming object, create a new collection, flatten nested structure
# purpose - clean code, faster execution

# types of comprehension- list, set, dictionary, generator




# list comprehension

names = [
    "Good Ali",
    "Alan",
    "Good Ellen"
]

good_boys = [boy for boy in names if "Good" in boy]

print(good_boys)

good_boys = [boy for boy in names if len(boy) > 4]

print(good_boys)
