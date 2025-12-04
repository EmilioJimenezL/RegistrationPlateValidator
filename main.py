from lexer import lexer
from parser import parse_license


def is_valid_license(plate):
    tokens = lexer(plate)
    return parse_license(tokens)

# Example usage
menu = 1
print("Welcome to the plate validator, insert a plate:")
while menu != 0:
    plate = input()
    if is_valid_license(plate):
        print("Plate is valid")
    else:
        print("Plate is invalid")
    print("What would you like to do?\n"
          "1) Insert another plate\n"
          "0) Exit\n")
    menu = int(input())
    if menu == 0:
        break