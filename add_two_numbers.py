# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            v1= l1.val if l1 else 0 #if(l1 not null)->v1=l1.val else v1=0
            v2 = l2.val if l2 else 0
            
            val = v1+v2+carry
            carry = val//10
            val = val%10
            #connecting the new value
            curr.next = ListNode(val)
            #updating ptrs
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next