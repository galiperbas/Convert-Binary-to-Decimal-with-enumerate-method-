def convert_to_decimal():
    decimal_number = 0
    input_binary = input("Write a binary..:")
    for chr in input_binary:
        if chr != "0" and chr != "1":
            print("just use 0 and 1 to write a binary number!")
            return False

    for (ix, digit) in enumerate(input_binary):
        if digit == "1":
            decimal_number += 2 ** (len(input_binary) - 1 - ix)

    print(f"'{input_binary}' is {decimal_number} in decimal number system.")


while True:
    convert_to_decimal()
