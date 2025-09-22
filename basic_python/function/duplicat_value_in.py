n = int(input())

list = []

for i in range(n):
    x = int(input())
    list.append(x)

uniq = []

for i in list:
    if i not in uniq:
        uniq.append(i)

for i in uniq:
    print(i)