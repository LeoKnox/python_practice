def has_cycle(head):
    slow = head
    fast = head
    while fast.next != None and fast != slow:
        slow = slow.next
        fast = fast.next
        fast = fast.next
    if fast == slow:
        return (slow, fast)
    if fast.next == None:
        return ("none")
