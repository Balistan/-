def main(input: str) -> int:
    parts = input.split()

    if len(parts) != 3:
        raise Exception("Invalid expression")

    a_str, operator, b_str = parts

    if not(a_str.isdigit() and b_str.isdigit()):
        raise Exception("Invalid expression")

    a,b = int(a_str), int(b_str)

    if not (1<=a<=10 and 1<=b<=10):
        raise Exception("Invalid expression")
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b
    elif operator == '/':
        return a//b
    else:
        raise Exception("Invalid operator")


try:
    print(main(input()))
except Exception as e:
    print(e)
