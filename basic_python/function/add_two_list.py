n   = int(input())
m   = int(input())
list = []
for i in range(n):
    x = int(input())
    list.append(x)
list2 = []
for i in range(m):
    y = int(input())
    list2.append(y)

new_list = list+list2

for  i in new_list:
    print(i)

