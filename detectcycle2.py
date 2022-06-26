
def has_cycle(head):
    if (head == None):
        return 0
    slow = head
    fast = head.next
    while fast != None and fast != slow:
        slow = slow.next
        fast = fast.next
        fast = fast.next
    if fast == slow:
        return (1)
    if fast == None:
        return ("none")
