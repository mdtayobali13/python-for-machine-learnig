# a  = " I love Dart "
# 1. Changing Case 
# print(a.capitalize())
# print(a.casefold())
# print(a.lower())
# print(a.upper())
# print(a.swapcase())
# print(a.title())

# 2. Checking Content 
# print(a.isalnum())
# print(a.isalpha())
# print(a.isdigit())
# print(a.isdecimal())
# print(a.isnumeric)
# print(a.isascii())
# print(a.islower())
# print(a.isupper())
# print(a.isspace())
# print(a.istitle())

#  Searching & Finding
# print(a.find("e"))
# print(a.rfind("a"))
# print(a.index("w"))
# print(a.count("w"))


# 4. Modifying / Replacing
# print(a.replace("Dart" , "python"))
# print(a.strip())
# print(a.rstrip())
# print(a.removeprefix("I "))
# print(a.removesuffix(" .png"))

# 5. Splitting & Joining
# text = "apple,banana,orange"
# parts = text.split(",")
# print(parts)

# text = "a-b-c-d"
# parts = text.rsplit("-" , 2)
# print(parts)
# text = "Hello\nHow are you?\nI am fine"
# lines = text.splitlines()
# print(lines)  

# text = "Python is fun"
# result = text.partition("is")
# print(result)

# text = "one-two-three-two"
# result = text.rpartition("two")
# print(result)

# worlds = ["I" , "love" , "Python"]
# sentence = " ".join(worlds)
# print(sentence)

# 6. Formatting
# text = "My name is {} and I am {} years old"
# result = text.format("Md.Tayob" , 22)
# print(result)

# data = {"Name" : "Arif" , "Age" : 30}
# text = "My name is {Name} and I am {Age} years old"
# result = text.format_map(data)
# print(result)

# num = "42"
# print(num.zfill(5))

# text = "Hello"
# print(text.center(11, "-"))
# text = "Hi"
# print(text.ljust(6,"."))

# text = "Hi"
# print(text.rjust(6,"."))

# text = "Name\tAge\tCity"
# print(text.expandtabs(10))

# text = "Hello Python"
# result = text.encode("utf-8")
# print(result)
# print(type(result))

# x = "abc"
# y = "123"
# table = str.maketrans(x , y)
# print(table)

# text = "abc cab"
# table = str.maketrans("abc" , "123")
# result = text.translate(table)
# print(result)

# text = "Hello World"
# table  = str.maketrans("ol" , "01")
# encoded = text.translate(table).encode("utf-8")
# print(encoded)

text = "Python programming"
# print(text.startswith("Py"))
# print(text.startswith("Java"))
print(text.endswith("ing"))
print(text.endswith("Java"))

