n = int(input())

list = []

for i in range(n):
    x = int(input())
    list.append(x)


for i in list :
    if i%2 == 0:
        print(i)
    