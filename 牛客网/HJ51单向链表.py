class Node(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None


while True:
    try:
        head = Node()
        count, num_list, k = int(input()), list(map(int, input().split())), int(input())
        while k:
            head.next = Node(num_list.pop())
            head = head.next
            k -= 1
        print(head.val)
    except EOFError:
        break