class Solution:
    def longestValidParentheses(self, s):
        # write code here
        stack = [-1]
        ans = 0
        for i, ch in enumerate(s):
            if ch == '(':
                # 左括号下标入栈
                stack.append(i)
            else:
                if len(stack) > 1:
                    # 匹配括号
                    stack.pop()
                    # 最大括号长度
                    ans = max(ans, i - stack[-1])
                else:
                    # 将其下标放入栈中
                    stack[-1] = i
        return ans


"""
将列表的下标利用起来
"""
