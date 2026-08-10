# Strings

# Strings are immutable

chai = "Ginger"

customer = "Alex"

print(f"Order for {customer}: {chai} please!")

greeting = "Hello world"

print(greeting[0])
print(greeting[0:4])
print(greeting[0:5])
print(greeting[0:5:2])
print(greeting[:5])
print(greeting[4:])
print(greeting[::-1])


# encoding and decoding
text = "Chañ"
encoded_text = text.encode("utf-8")

print(f"Non encoded label: {text}")
print(f"encoded label: {encoded_text}")     

decoded_text = encoded_text.decode("utf-8")
print(f"decoded label: {decoded_text}") 