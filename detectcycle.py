def has_cycle(head):
    slow = head
    fast = head
    while fast.next != None and fast != slow:
        slow = slow.next
        fast = fast.next.next
    if fast == slow:
        return 1
    if fast.next == None:
        return 0
