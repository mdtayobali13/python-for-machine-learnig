row = int(input("Enter any Number : "))

for x in range(1,row+1):
    for y in range(x):
        print(y+1 ,end=" ")
    print(" ")