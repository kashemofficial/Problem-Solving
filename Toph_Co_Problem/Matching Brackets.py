def isBalanced(string):
    stack = []
    for char in string:
        if char in ['(', '{', '[']:
            stack.append(char)
        else:
            if not stack:
                return False
            last_char = stack.pop()
            if last_char == '(':
                if char != ')':
                    return False

            if last_char == '{':
                if char != '}':
                    return False

            if last_char == '[':
                if char != ']':
                    return False

    if stack:
        return False
    return True


if __name__ == '__main__':

    string = input()
    res = isBalanced(string)

    if isBalanced(string):
        print('Yes')
    else:
        print("No")
        