def isparanthesis(s):
    stack=[]
    #iterrating over the string
    for char in s:
        #if opening bracket is encountered we push it in to stack
        if char in ["(","{","["]:
            stack.append(char)
        #if closing bracket is encountered we compare it with top
        else:
            if len(stack)==0:
                return False
            #if top of the stack has the opening bracket
            #of same type we pop the top element continue iterating
            #else return false
            if char==")":
                if stack[-1]=="(":
                    stack.pop()
                    continue
                if char=="}":
                    if stack[-1]=="{":
                        stack.pop()
                        continue
                if char=="]":
                    if stack[-1]=="[":
                        stack.pop()
                        continue
                return False
    if len(stack)==0:
        return False
    return True
string="{()}}"

print(isparanthesis(string))