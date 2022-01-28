"""
  /*
   某学校举行运动会,学生们按编号（1、2、3.....n)进行标识,
   现需要按照身高由低到高排列，
   对身高相同的人，按体重由轻到重排列，
   对于身高体重都相同的人，维持原有的编号顺序关系。
   请输出排列后的学生编号
   输入描述：
      两个序列，每个序列由N个正整数组成，(0<n<=100)。
      第一个序列中的数值代表身高，第二个序列中的数值代表体重，
   输出描述：
      排列结果，每个数据都是原始序列中的学生编号，编号从1开始，
   实例一：
      输入:
       5
       100 100 100 120 130
       40 30 30 60 50
      输出:
       23145
   */
"""


def solution():
    while True:
        try:
            in_num = int(input())
            high = list(map(int, input().split()))
            wei = list(map(int, input().split()))
        except:
            break
        else:
            message_dic = {}
            for item in range(1, in_num + 1):
                message_dic[item] = [high[item - 1], wei[item - 1]]
            """{1: [100, 40], 2: [100, 30], 3: [120, 60], 4: [130, 50]}"""
            res = sorted(message_dic.items(), key=lambda x: (x[1][0], x[1][1], x[0]))
            """[(2, [100, 30]), (1, [100, 40]), (3, [120, 60]), (4, [130, 50])]"""
            """[(1, [100, 40]), (2, [100, 30]), (3, [120, 60]), (4, [130, 50])]  -"""
            print(res)
            out_res = [str(x[0]) for x in res]
            print(''.join(out_res))



if __name__ == '__main__':
    solution()
