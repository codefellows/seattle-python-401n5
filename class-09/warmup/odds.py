# Write a function that takes a linked list and returns the sum of all odd values.


def sum_ll(ll):
    total_even = 0
    total_odd = 0
    current = ll.head
    # traverse the ll
    while current:
        # check if the value is odd or not
        if current.value % 2 != 0:
            total_odd += current.value
        elif current.value % 2 == 0:
            total_even += current.value
        current = current.next
    return total_odd, total_even
