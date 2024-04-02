# Write a function for a calculator that takes a string as input, containing two integers and one arithmetic
# operator (+, -, *, /), and returns the result of performing that operation
# if the numbers are not integers or if the operator is missing, it should raise a ValueError

def calculator(expression):
    allowed = '+-/*'
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'The expression must contain at least one operator ({allowed})')
    for sign in allowed:
        if sign in expression:

            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)
                if sign == '+':
                    return left + right
                elif sign == '-':
                    return left - right
                elif sign == '*':
                    return left * right
                elif sign == '/':
                    return left / right
            except(ValueError, TypeError):
                raise ValueError('The expression must contain 2 integers and 1 operator')


if __name__ == '__main__':
    print(calculator('10-2'))
