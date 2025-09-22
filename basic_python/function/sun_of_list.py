n = int(input("Enter Input size : "))

sum = 0

intpu_numbers = []

for i in range(n):
    x = int(input("Enter Input Element : "))
    intpu_numbers.append(x)
    

for i in intpu_numbers:
    sum = sum+i

print("Sum of = ",sum)
   