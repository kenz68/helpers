# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: Optional[ListNode]) -> bool:
    s = ''
    while head:
        s += str(head.val)
        head = head.next

    return s == s[::-1]


def addBinary(a: str, b: str) -> str:
    return str(bin(int(a, 2) + int(b, 2))).replace('0b', '')

# head = ListNode(val=1, next=ListNode(
#     val=2, next=ListNode(val=2, next=ListNode(val=1, next=None))))
# print(isPalindrome(head))


print(addBinary("11", "1"))
