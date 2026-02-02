


# ----------------- Calculator Functions -----------------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"


# ----------------- String Operations -----------------
def string_length(s):
    return len(s)

def reverse_string(s):
    return s[::-1]

def to_upper(s):
    return s.upper()


# ----------------- Number Utilities -----------------
def is_even(n):
    return n % 2 == 0

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# ----------------- Main Menu Function -----------------
def main_menu():
    while True:
        print("\n----- Main Menu -----")
        print("1. Calculator")
        print("2. String Operations")
        print("3. Number Utilities")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Addition: {add(a, b)}")
            print(f"Subtraction: {subtract(a, b)}")
            print(f"Multiplication: {multiply(a, b)}")
            print(f"Division: {divide(a, b)}")

        elif choice == "2":
            s = input("Enter a string: ")
            print(f"Length: {string_length(s)}")
            print(f"Reversed: {reverse_string(s)}")
            print(f"Uppercase: {to_upper(s)}")

        elif choice == "3":
            n = int(input("Enter a number: "))
            print(f"Even? {is_even(n)}")
            print(f"Factorial: {factorial(n)}")
            print(f"Prime? {is_prime(n)}")

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


# ----------------- Program Starts Here -----------------
main_menu()



