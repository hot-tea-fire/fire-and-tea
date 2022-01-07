"""
最长回文字符

Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，比如像这些ABBA，ABA，A，123321，
但是他们有时会在开始或结束时加入一些无关的字符以防止别国破解。比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214　
。因为截获的串太长了，而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），Cathcer的工作量实在是太大了，
他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？
"""

def solution():
    while True:
        try:
            i_list = list(input())
        except:
            break
        else:
            res_list =[]
            for i in range(len(i_list)):
                for j in range(i+1,len(i_list)):
                    if i_list[i] == i_list[j] and i_list[i+1:j] == i_list[j-1:i:-1]:
                        res_list.append(len(i_list[i:j+1]))
            if not res_list:
                print(0)
                continue
            print(max(res_list))


if __name__ == '__main__':
    solution()
