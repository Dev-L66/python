# class Hello:
#     pass

# class Helloworld:
#     pass

# print(type(Hello))

# greeting = Hello()

# print(type(greeting))
# print(type(greeting) is Hello)
# print(type(greeting) is Helloworld)

# class Hello:
#     greeting = "Hi"

# print(Hello.greeting)

# Hello.bye = "Good bye"
# print(Hello.bye)

# helloworld = Hello()
# print(helloworld.greeting)
# print(helloworld.bye)

# helloworld.language = "Python"
# print(helloworld.language)

# helloworld.bye = "BYE!!!!!"
# print(helloworld.bye)
# print(Hello.bye)

# print(f"Class: {Hello.bye}")
# print(f"Object: {helloworld.bye}")

# class Hello:
#     greeting = "HIII"
#     bye = "Good bye"

# helloworld = Hello()
# print(helloworld.greeting)
# helloworld.greeting = "HELLO WORLD"
# print(helloworld.greeting)
# print(Hello.greeting)

# del helloworld.greeting
# print(helloworld.greeting)

# helloworld.size = "large"
# print(helloworld.size)

# del helloworld.size
# print(helloworld.size)

# class Coffee:
#     size = 150

#     def describe(self):
#         return f"A{self.size}ml cup"

# cup = Coffee()
# print(cup.describe())
# print(Coffee.describe(cup))

# cup_two = Coffee()
# cup_two.size = 100
# print(cup_two.describe())
# print(Coffee.describe(cup_two))


# class CoffeeOrder:
#     def __init__(self, type_, size):
#         self.type = type_
#         self.size = size

#     def summary(self):
#         return f"{self.size} ml of {self.type} coffee"

# order = CoffeeOrder("Latte", 100)
# print(order.summary())

# order_two = CoffeeOrder("Black", 100)
# print(order_two.summary())


# class BaseChai:
#     def __init__(self, type_):
#         self.type_ = type_

#     def prepare(self):
#         print(f"Preparing {self.type_} coffee...")


# class MasalaChai(BaseChai):
#     def add_spices(self):
#         print("Adding cardamom")

# class ChaiShop:
#     chai_cls = BaseChai

#     def __init__(self):
#         self.chai = self.chai_cls("Regular")

#     def serve(self):
#         print(f"Serving {self.chai.type_} chai in the shop")
#         self.chai.prepare()


# class FancyChaiShop(ChaiShop):
#     chai_cls = MasalaChai



# shop = ChaiShop()

# fancy = FancyChaiShop()
# shop.serve()
# fancy.serve()
# fancy.chai.add_spices()


class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength

# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level


# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self, type_, strength)
#         self.spice_level = spice_level


# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         super().__init__(type_, strength)
#         self.spice_level = spice_level
        