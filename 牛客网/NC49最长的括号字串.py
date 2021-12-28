"""
描述
给出一个长度为 n 的，仅包含字符 '(' 和 ')' 的字符串，计算最长的格式正确的括号子串的长度。
例1: 对于字符串 "(()" 来说，最长的格式正确的子串是 "()" ，长度为 2 .
例2：对于字符串 ")()())" , 来说, 最长的格式正确的子串是 "()()" ，长度为 4 .
字符串长度：0<=n<=5*10^5
要求时间复杂度O(n) ,空间复杂度O(n).
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res_li = []
        for item in s:
            if item == '(':
                res_li.append(item)
            elif item == ')':
                if res_li:
                    if res_li[-1] == '(':
                        res_li.pop(-1)
                        res_li.append(2)
                        if len(res_li) >= 2:
                            while len(res_li) >= 2:
                                if type(res_li[-2]) == int:
                                    count = res_li[-1] + res_li[-2]
                                    res_li.pop(-1)
                                    res_li.pop(-1)
                                    res_li.append(count)
                                else:
                                    break
                    elif res_li[-1] == ')':
                        res_li.append(')')
                    elif type(res_li[-1]) == int:
                        if len(res_li) >= 2 and res_li[-2] == '(':
                            res_li.pop(-2)
                            res_li.append(2)
                            if len(res_li) >= 2:
                                while len(res_li) >= 2:
                                    if type(res_li[-2]) == int:
                                        count = res_li[-1] + res_li[-2]
                                        res_li.pop(-1)
                                        res_li.pop(-1)
                                        res_li.append(count)
                                    else:
                                        break
                        else:
                            res_li.append(')')
        for item in res_li[:]:
            if type(item) == str:
                res_li.remove(item)
        if not res_li:
            return 0
        return max(res_li)


if __name__ == '__main__':
    s = Solution()
    a = s.longestValidParentheses(")))))))))")
    print(a)

"""
能行，但运行超时
"""