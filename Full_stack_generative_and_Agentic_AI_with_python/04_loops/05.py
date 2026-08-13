# break, continue

flavors = ["vanilla", "Out of stock", "choclate", "discontinued"]


for flavor in flavors:
    if flavor == "Out of stock":
       continue
    if flavor == "discontinued":
        break
    print(f"{flavor} discontinued")

print("outside loop")
