
secret_number = 12
entered_number = int(input("Enter the secret number: "))

if entered_number == secret_number:
    print(" Locker opened successfully!")
else:
    print("Wrong number! Locker remains closed.")
