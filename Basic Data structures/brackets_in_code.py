from select import select


from collections import deque

def brackets_in_code(str):
    len_of_str = len(str)

    if len_of_str == 1:
        return 0
    
    selectedLeft = ['{','[','(']

    selectedRight = ['}',']',')']

    myStack = deque()
    indices_of_char = []

    for i in range(len_of_str):
        char = str[i]

        if char not in selectedLeft and char not in selectedRight:
            continue
        if char in selectedLeft:
            myStack.append(char)
            indices_of_char.append(i)
        else:
            if len(myStack) == 0:
                return i

            top = myStack.pop()
            indices_of_char.pop()

            bool_one = top == '[' and char != ']'
            bool_two = top == '{' and char != '}'
            bool_three = top == '(' and char != ')'
                       
            # print(f'{bool_one} {bool_two} {bool_three}')
            if bool_one or bool_two or bool_three:
                print('failed case')
                return i
        
    
    print(myStack)
    if len(myStack) == 0:
        return 'Success'
    else:
        return indices_of_char[0]



print(brackets_in_code(['{','}','(','[',']']))