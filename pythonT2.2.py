age = int(input("enter the age of passenger:"))

if age < 5:
    print("very younger passenger - travels free:")

elif age <= 18:
    print("student passenger - concession:")

else:
    print("adult passenger - full pay:")