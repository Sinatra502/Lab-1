# name = raw_input("what is your name ")
# print("hello "+ str(name))

number = input("input a number: ")
number = int(number)
if number % 2 == 0:
    print(str(number) + " is a EVEN number.")
else:  # number %2 ==1
    print(str(number)+ " is a ODD number.")
