# rpn.py

def evaluate_rpn(tokens):
    """
    Avalia uma expressão dada em notação pós-fixada (Reverse Polish Notation).
    tokens: lista de strings — cada string é ou um inteiro (possivelmente negativo) ou um operador '+', '-', '*', '/'
    Retorna: int, resultado da expressão, com a divisão truncando para zero.
    """
    stack = []
    
    for token in tokens:
        if token not in ('+', '-', '*', '/'):
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
            elif token == '*':
                stack.append(left * right)
            elif token == '/':
                stack.append(int(left / right))

    return stack.pop()
