orders = ["red", "pizza", "ball"]
# print(orders[5])


chai_menu = {"masla": 30, "ginger": 40}
try:
  chai_menu["elaichi"]
except KeyError:
  print("The key doesn't exist")

print("Hello")

def serve_chai(flavor):
   try:
    print(f"Preparing {flavor}")
    if flavor == "unknown":
      raise ValueError(f"We don't have {flavor}")
   except ValueError as e:
     print("error", e)
   else:
     print(f"{flavor} served")
   finally:
     print("NExt order")


serve_chai("masla")
serve_chai("unknown")