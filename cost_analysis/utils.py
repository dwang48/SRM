def tokenize(expression):
    tokens = []
    num = ''
    for char in expression:
        if char.isdigit():
            num += char
        else:
            if num:
                tokens.append(num)
                num = ''
            tokens.append(char)
    if num:
        tokens.append(num)
    return tokens

def to_postfix(tokens):
    def precedence(op):
        return {'+': 1, '-': 1, '*': 2, '/': 2}.get(op, 0)

    output = []
    operators = []
    
    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in "+-*/":
            while operators and precedence(operators[-1]) >= precedence(token):
                output.append(operators.pop())
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()  # remove the '('

    while operators:
        output.append(operators.pop())
        
    return output

def evaluate_postfix(postfix_tokens):
    stack = []
    for token in postfix_tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
    return stack[0]

def evaluate_expression(expression):
    tokens = tokenize(expression)
    postfix_tokens = to_postfix(tokens)
    return evaluate_postfix(postfix_tokens)

# Test
def tokenize_variables(expression):
    tokens = []
    term = ''
    for char in expression:
        if char.isalnum() or char == '_':  # Considering terms can have underscores
            term += char
        else:
            if term:
                tokens.append(term)
                term = ''
            tokens.append(char)
    if term:
        tokens.append(term)
    
    # Extract variables (non-numeric terms) from tokens
    variables = [token for token in tokens if not (token.isdigit() or token in "+-*/()")]
    
    return tokens, variables

# expression = "产品毛重*(原材料价格/1000000)-(产品毛重-产品净重)*废料价格/1000000"
# tokens, variables = tokenize_variables(expression)
# variables

