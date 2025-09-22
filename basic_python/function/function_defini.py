# def dept():
#     print("Data science")

# dept()

# parameters 

# def dept_with_name(name):
#     print(f'My major is {name}')

# dept_with_name("CSE")

# return type function

# def dept_return(a , b):
#     return a+b

# print(dept_return(10 , 20))

# def fact(n):
#     if n == 0 or n ==1:
#         return 1
#     return n*fact(n-1)

# print(fact(5))

# def mulp1():
#     x = int(input("x = "))
#     y = int(input("y = "))

#     result = x*y
#     return result

# def mulp2():
#     total1 = mulp1()
#     z = int(input("z = "))
#     total2 = total1 * z
#     print("final Result =  " , total2)

# mulp2()

def fuct(x):
    result = 1
    i = 1

    if (x == 0 or x ==1):
        print(f'fact is {x}! = 1')
    else :
        while i<x:
            result = result*(i+1)
            i = i+1
        return result
print(fuct(5))