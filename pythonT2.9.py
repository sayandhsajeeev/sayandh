def sum_of_divisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number:"))

sum1 = sum_of_divisors(num1)
sum2 = sum_of_divisors(num2)

if sum1 == num2 and sum2 == num1:
    print("The numbers are Friendly Partners")
else:
    print("The numbers are NOT Friendly Partners")
