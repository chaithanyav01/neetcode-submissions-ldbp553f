# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        count = 0
        max_Count = 100
        curr = head

        while count<max_Count and curr:
            count+=1
            curr = curr.next

        return not count<10