# def greeting(name):
#     print(f"Hello, {name}")

# greeting("Alex")
# greeting("Hala")

# def fetch_sales():
#     print(f"Fetching the sales report.")

# def filter_valid_sales():
#     print("Filtering vaid sales data")

# def summarize_data():
#     print("Summarizing data")

# def generate_report():
#     fetch_sales()
#     filter_valid_sales()
#     summarize_data()
#     print("Generating report")

# generate_report()

# def get_input():
#     print("Getting user input")

# def validate_input():
#     print("Validating the user input")

# def save_to_db():
#     print("SAving to db")

# def register_user():
#     get_input()
#     validate_input()
#     save_to_db()
#     print("User registration complete")

# register_user()


# def calculate_bill(cups, price_per_cup):
#     return cups * price_per_cup

# my_bill = calculate_bill(3,15)
# print(my_bill)

# print(f"order for table 2: {calculate_bill(3,15)}")

# def add_vat(price, vat_rate):
#     return price *(100+vat_rate)/100

# orders = [100, 150, 200]

# for price in orders:
#     final_amt = add_vat(price, 10)
#     print(f"Original:{price}, final with VAT: {final_amt}")

# def serve_coffee():
#     coffee_type = "Cold"
#     print(f"Inside function: {coffee_type}")

# coffee_type = "Black coffee"
# serve_coffee()
# print(f"Outside function : {coffee_type}")



# def coffee_counter():
#     coffee_order = "Cold coffee"
#     def print_order():
#         coffee_order = "Blck coffee"
#         print(f"Inner: {coffee_order}")
#     print_order()
#     print(f"Inner: {coffee_order}")

# coffee_order = "Latte"
# coffee_counter()
# print(f"Global: {coffee_order}")


# def update_order():
#     coffee_order = "Spanish Latte"

#     def kitchen():
#         # nonlocal coffee_order
#         coffee_order = "Mocha"
#     kitchen()
#     print("After kitchen update", coffee_order)

# update_order()



# coffee_type = "Black"

# def front_desk():
#     def kitchen():
#         global coffee_type
#         # nonlocal coffee_type
#         coffee_type = "Latte"
#     kitchen()

# front_desk()
# print(f"Final global coffee {coffee_type}")

# coffee = "Latte"

# def prepare_coffee(order):
#     print("Preparing", order)

# prepare_coffee(coffee)
# print(coffee)



# numbers = [1,2,3]

# def edit_numbers(integers):
#     integers[1] = 42

# edit_numbers(numbers)
# print(numbers)


# def make_chai(tea, milk, sugar):
#     print(tea, milk, sugar)


# make_chai("Darjeeling", "Yes", "Low")
# make_chai(tea="Green", sugar="Medium", milk="Yes")



# def special_chai(*ingredients, **extras):
#     print("Ingredients", ingredients)
#     print("Extras", extras)


# special_chai("Cinnamon","Cardmom", sweetner= "honey", foam="yes")



# def chai_order(order = []):
#     order.append("Masla")
#     print(order)


# chai_order()
# chai_order()

# def chai_order(order = None):
#     if order is None:
#         order = []
#     print(order)


# chai_order()
# chai_order()



# def make_chai():
#     # return "Here is your chai"
#     print("Here's your chai")

# print(make_chai())

# return_value = make_chai()

# print(return_value)




# def idle_chai():
#     pass

# print(idle_chai())


# def sold_cups():
#     return 120

# total = sold_cups()
# print(total)




# def chai_status(cups_left):
#     if cups_left == 0:
#         return "Sorry chai over"
#     return "Chai ready"
#     print("chai")

# print(chai_status(0))
# print(chai_status(2))



# def chai_report():
#     return 20, 30, 10

# sold, remaining,not_paid = chai_report()
# print(f"Sold: {sold}, Remaining: {remaining}")


# def pure_chai(cups):
#     return cups * 10

# total_chai =0

# def impure_chai(cups):
#     global total_chai
#     total_chai += cups

# def pour_chai(n):
#     print(n)
#     if n == 0:
#         return "All cups poured"
#     return pour_chai(n-1)

# pour = pour_chai(3)
# print(pour)





# colors = ["red", "blue", "green", "blue"]

# color = list(filter(lambda color: color!="blue", colors))

# print(color)


