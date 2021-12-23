import sys

def compute(str):
    res = ""
    number = int(float(str))
    foo_bar_qix = False

    chars = [char for char in str]

    # If the number is divisible by 3, write "Foo" instead of the number
    if number % 3 == 0:
        foo_bar_qix = True
        res = res + "Foo"
          
    # If the number is divisible by 5, add "Bar"
    if number % 5 == 0:
        foo_bar_qix = True
        res = res + "Bar"
    
    # If the number is divisible by 7, add "Qix"
    if number % 7 == 0:
        foo_bar_qix = True
        res = res + "Qix"

    # For each digit 3, 5, 7, add "Foo", "Bar", "Qix" in the digits order.
    for char in chars:
        if char == "5":
            foo_bar_qix = True
            res = res + "Bar"
        if char == "3":
            foo_bar_qix = True
            res = res + "Foo"
        if char == "7":
            foo_bar_qix = True
            res = res + "Qix"
            
    if  foo_bar_qix == False:
        res = str
    
    print(res)

compute(sys.argv[1])