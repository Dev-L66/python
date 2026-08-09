is_boiling = True
count = 5

# upcasting , boolean here is changed to 1 , so it is 5 + 1
total = count + is_boiling  
print(total)

print(is_boiling)

milk = 11
print(f"Is there milk? {bool(milk)}")

milk = 0
print(f"Is there milk? {bool(milk)}")

milk = None
print(f"Is there milk? {bool(milk)}")

# logical opertors
# and, or, not

hot = True
tea = False

serve = hot and tea
print(serve)

serve = hot or tea
print(serve)

serve = not hot
print(serve)