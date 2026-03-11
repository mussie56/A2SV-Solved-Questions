# found = True
        if stack:
            if stack[-1] == "(":
                stack.pop()
                stack.append(1)
            else:
                num = 0
                while stack and stack[-1] != "(":
                    num+=stack.pop()
                if stack:
                    stack.pop()
                    # if temp.isdigit():
                    #     ans.append(temp)
                # if num:
                    stack.append(num+1)
            if len(stack)==1 and stack[-1] != "(":
                ans.append(stack.pop()*2)
        else:
            ans.append(-1)
            # if len(stack)==1 and stack[-1] != "(":
            #     ans.append(stack.pop()*2)
    # print(stack)
while stack:
    num = 0
    while stack and stack[-1] != "(":
        num+=stack.pop()
    ans.append(-1)
    ans.append(num*2)
    # ans.append(-1)
    if stack:
        stack.pop()
# if stack:
#     stack.pop()
    # if temp.isdigit():
    #     ans.append(temp)
# if num:
#     stack.append(num+1)
# if len(stack)==1 and stack[-1] != "(":
#     ans.append(stack.pop()*2)
summ = 0
res = []
for i in ans:
    if i == -1:
        if summ:
            res.append(summ)
        summ =0
        continue
    summ+=i
if summ:
    res.append(summ)
if not res:
    print("0 1")
    exit()
res.sort(reverse=True)
maxx = res[0]
sub = 0
for i in res:
    if i < maxx:
        break
    sub+=1
print(maxx,sub)
# print(ans)
# print(res)