
names = []


for i in range(5):
    name = input(f"Enter your Name {i+1}: ")
    names.append(name)  

print("\nYou entered these names:")
for n in names:
    print(n)
