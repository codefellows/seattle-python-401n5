def largest_value(ll):

    largest_val = 0  # 13
    current = ll.head
    while current:  # current
        if current.value > largest_val:
            largest_val = current.value
        current = current.next
    return largest_val


# - (7)->(2)->(13)->(9)->(3) -> None expected return (13)
#              ^

def largest_value2(ll):

    largest_val = ll.head.value
    current = ll.head.next  # Problem? None
    while current:  # current
        if current.value > largest_val:
            largest_val = current.value
        current = current.next
    return largest_val
