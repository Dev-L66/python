x = ("apple", "mango","orange")
y = enumerate(x)
print(y)
(print(list(y)))

file = open('text.py')
# file = open('test.py', 'w') if file not present will be created if opened in write mode

file = open('youtube.txt','w')


try:
    file.write('Hello world')
finally:
    file.close()


with open('youtue.txt', 'w') as file:
    file.write('Hello world')