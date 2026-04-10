# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
- reverse the linked list
- return new head

input List[int]: [1,2,3]
output List[int]: [3,2,1]

head->1->2->3->null
head->3->2->1->null  
'''      

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

        return head