def code(n1, n2):
    def add(n1, n2):
        return n1 + n2

    def subtract (n1, n2):
        return n1 - n2

    def multiply(n1, n2):
        return n1 * n2

    def divide(n1, n2):
        return n1 / n2

    all_functions = {"+":add,
                    "-":subtract,
                    "x":multiply,
                    "/":divide}

    return all_functions[operation](n1, n2)


operation = input("What is your operation? Type either +,-,x or /")
n1 = float(input("What is your first number?"))
n2 = float(input("What is your second number?"))
result = code(n1, n2)
print(result)
continuation = True
while continuation:
    want_to_continue = input("do you want to continue?")
    if want_to_continue == "yes":
        operation = input("What is your operation?")
        n1 = float(result)
        n2 = float(input("what is your other number?"))
        code1 = code(n1, n2)
        print(code1)
    else:
        operation = input("What is your operation?")
        n1 = float(input("What is your first number?"))
        n2 = float(input("What is your second number?"))
        code = code(n1, n2)
        print(code)