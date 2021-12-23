import sys

def compute(str):
    res = ""
    number = int(float(str))

    chars = [char for char in str]

    # If the number is divisible by 3, write "Foo" instead of the number
    if number % 3 == 0:
        res = "Foo"
          
    # If the number is divisible by 5, add "Bar"
    if number % 5 == 0:
        res = res + "Bar"
    
    # If the number is divisible by 7, add "Qix"
    if number % 7 == 0:
        res = res + "Qix"

    # For each digit 3, 5, 7, add "Foo", "Bar", "Qix" in the digits order.
    for char in chars:
        if char == "5":
            res = res + "Bar"
        if char == "3":
            res = res + "Foo"
        if char == "7":
            res = res + "Qix"

    # default
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0 and "5" not in chars and "3" not in chars and "7" not in chars:
        res = str
            
    print(res)

compute(sys.argv[1])