n  = int(input("Enter list size : "))
list = []
for i in range(n):
    x = int(input("Enter Element : "))
    list.append(x)
list.reverse()

for i in list:
   print(i)
      