def isValid(s:str) -> bool:
    stack = [0] * len(s)
    cnt = -1
    for string in s:
        if string == '(' or string == '[' or string == '{':
            cnt += 1
            stack[cnt] = string
        else:
            checkString = stack[cnt]
            cnt -= 1
            if checkString == '(':
                if string != ')':
                    return False
            elif checkString == '{':
                if string != '}':
                    return False
            elif checkString == '[':
                if string != ']':
                    return False

    if cnt == -1:
        return True
    else:
        return False




a = isValid(s="][")
print(a)