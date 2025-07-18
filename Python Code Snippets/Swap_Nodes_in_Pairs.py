class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def swapPairs(head):
    dummy=ListNode(0,head)
    prev=dummy
    while head and head.next:
        first=head
        second=head.next
        prev.next=second
        first.next=second.next
        second.next=first
        prev=first
        head=first.next
    return dummy.next