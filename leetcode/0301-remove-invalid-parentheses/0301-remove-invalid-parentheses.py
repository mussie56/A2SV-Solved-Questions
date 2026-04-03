class Solution:
    def removeInvalidParentheses(self,s: str) -> List[str]:
        ans = []
        n = len(s)
        def isValid(s):
            stack = []
            for i in s:
                if i.isalpha():
                    continue
                if i == "(":
                    stack.append(i)
                else:
                    if stack:
                        stack.pop()
                    else:
                        return False
            return len(stack) == 0

        def backtrack(i,arr,count):
            nonlocal n
            if isValid(arr):
                ans.append("".join(arr))
            if i >= n:
                return
            if count > n-i or count < 0:
                return
                
            if s[i].isalpha():
                arr.append(s[i])
                backtrack(i+1,arr,count)
                arr.pop()
            else:
                if s[i] == '(':
                    arr.append(s[i])
                    backtrack(i+1,arr,count+1)
                    arr.pop()
                    backtrack(i+1,arr,count)
                else:
                    arr.append(s[i])
                    backtrack(i+1,arr,count-1)
                    arr.pop()
                    backtrack(i+1,arr,count)

        backtrack(0,[],0)
            
        ans.sort(key=lambda x:-len(x))
        k = len(ans[0])
        res = []
        for i in ans:
            if len(i) == k:
                if res and i in res:
                    continue
                res.append(i)
            else:
                break
        return res






    # def removeInvalidParentheses(self, s: str) -> List[str]:
    #     ans = []
    #     n = len(s)
    #     def isValid(s):
    #         stack = []
    #         for i in s:
    #             if i.isalpha():
    #                 continue
    #             if i == "(":
    #                 stack.append(i)
    #             else:
    #                 if stack:
    #                     stack.pop()
    #                 else:
    #                     return False
    #         return len(stack) == 0 # not stack


    #     def backtrack(i,arr):
    #         nonlocal n
    #         if isValid(arr) and arr:
    #             ans.append("".join(arr))
    #         if i >= n:
    #             return
            
    #         # for j in range(i,n):
    #         if s[j].isalpha():
    #             arr.append(s[j])
    #             backtrack(i+1,arr)
    #         else:
    #             arr.append(s[j])
    #             backtrack(i+1,arr)
    #             arr.pop()
    #             backtrack(i+1,arr)

    #     backtrack(0,[])


    #     # if ans:
    #         # print("[\"\"]")
    #     print(ans)
    #     ans.sort(key=lambda x:-len(x))
    #     # k = len(ans[0])
    #     # res = []
    #     # for i in ans:
    #         # if len(i) == k:
    #             # res.append(i)
    #         # else:
    #             # break
    #     return ans[:2] if len(ans)>=2 else ans