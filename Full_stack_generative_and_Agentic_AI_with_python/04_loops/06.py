fruits = [('mango', 10), ('apple', 90), ('cherries', 9)]


for fruit, price in fruits:
    if price >= 100:
       print(f"{fruit}")
       break
else:
        print("Expensive")