def fact(number):
    for i in range(1,number):
        number=number*i
    print("the factorial is",number)
fact(int(input("enter a number: ")))
