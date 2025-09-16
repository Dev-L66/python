import sys
print(sys.getrefcount(1))
a = 3
a = 'hello'
a = 3.14
a = 5
b = 2
print(a)
print(b)
a = a + 2
print(a)
print(b)

myList1 = [1,2,3]
myList2 = myList1
print(myList1)
print(myList2)

myList1 = 'hello'
print(myList1)
print(myList2)

myList1 = [1,2,3]
myList1[0] = 5
print(myList1)
print(myList2)

l1 =[7,8,9]
l2  = l1
print(l1)
print(l2)
l1[0] = 10
print(l1)
print(l2)


p1 = [2,3,1]
p2 = p1
p2 = [2,3,1]
p1[0] = 6
print(p1)
print(p2)


h1=[1,2,3]
h2 = h1[:] 
#  copy
print(h1)
print(h2)
h1[0] = 5
print(h1)
print(h2)





n =[4,5,6]
m = n
print(m)
print(n)
print(m == n)
print(m is n)

m = [4,5,6]
print(m)
print(n)
print(m == n)

# print(m is n)   false as memory referen changed