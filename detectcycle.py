def has_cycle(head):
    if head.next != None:
        slow = head
    else:
        return 0
    fast = head
    if fast.next != None:
        fast = fast.next
    else:
        return 1
    while fast.next != None and fast != slow:
        slow = slow.next
        fast = fast.next
        fast = fast.next
    if fast == slow:
        return (1)
    if fast.next == None:
        return ("none")
