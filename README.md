# Conversion-to-boolean-Unknown-operation
Conversion to boolean  Unknown operation
There is a function hidden_operation() which in every test case performs one of the logical operations: and, or and not.

def hidden_operation(operand):
    if oper == "and":
        return operand and hidden_operand
    elif oper == "or":
        return operand or hidden_operand
    elif oper == "not":
        return not operand
        
You don't have access to oper and hidden_operand variables, but you can call the hidden_operation() function any number of times and pass any objects to it. Your task is to find out which logical operation this function performs and what the hidden_operand is equal to (if the function performs the not operation, you don't have to find the hidden_operand).

Write your code inside the solve() function. In the first line print the name of the logical operation. If the logical operation is and or or, print hidden_operand in the second line.

Your program shouldn't read any input or call the function, just implement it.

Hint

Pass a random non-empty string to the hidden_operation() function. The "not" operator would return False; the "and" operator would return hidden_operand; the "or" operator would return the passed string. If the passed string is complicated enough not to match hidden_operand, this allows you to distinguish the "or" operator from other operators. Then, to distinguish the "and" and "not" operators, pass False to the function.
