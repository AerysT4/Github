num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
def EvenOdd(num):
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")

EvenOdd(num1)
EvenOdd(num2)
print("test")