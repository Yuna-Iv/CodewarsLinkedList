"""It still doesnt work for some reason"""
def loop_size(node):
    slow = node
    fast = node
    while True:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break

    count = 1
    cur = slow.next
    while cur is not fast:
        cur = cur.next
        count += 1

    return count
