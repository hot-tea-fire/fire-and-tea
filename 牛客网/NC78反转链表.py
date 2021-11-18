class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def ReverseList(self, head: ListNode) -> ListNode:
        if not head:    # 如果非空
            return head
        a, a.next, b = head, None, head.next     # 初始化
        while b:
            b, a, a.next = b.next, b, a         # 遍历
        return a

