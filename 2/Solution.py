from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 保存进位
        carry = 0
        node1 = l1
        node2 = l2
        while node1.next is not None:

            node1.val = node1.val + node2.val
            node1 = node1.next
            # 如果没有node2后面没有余数，跳出循环
            node2 = node2.next
            if node2 is None:
                break
            else:
                pass

        # 如果node2后还有节点，将这些节点插入node1尾部
        if node2 is not None:
            # 计算node1最后一个节点
            node1.val = node1.val + node2.val
            # 然后吧 node2后的节点全部插入到node1的尾部
            node1.next = node2.next
        # 开始调整进位
        node1 = l1

        while True:
            # 先加上上一步进位
            node1.val = node1.val + carry
            # 再计算这一步进位
            carry = node1.val // 10
            # 计算余数
            node1.val = node1.val % 10
            if node1.next is not None:
                node1 = node1.next
            else:
                break
        if carry > 0:
            node1.next = ListNode(carry)

        return l1


tn = ListNode(5)
tn2 = ListNode(5)

t2 = [5, 6, 4]
mytest = Solution()
result = mytest.addTwoNumbers(tn, tn2)
print(result)
