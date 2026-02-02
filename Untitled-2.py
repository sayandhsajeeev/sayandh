text = input("enter any text:")

letters = 0
digits = 0
special_chars = 0

for ch in text:
    if ch.isalpha():
        letters+= 1
    elif ch.isdigit():
        digits+= 1
    else:
        special_chars+= 1

        totel = len(text)

        print("total letters:",letters)
        print("total digits:",digits)
        print("total special characters:",special_chars)
        print("total characters:",letters+digits+special_chars)