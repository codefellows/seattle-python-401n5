# Write a function called zip lists
# Arguments: 2 linked lists
# Return: New Linked List, zipped as noted below
# Zip the two linked lists together into one so that the nodes alternate
# between the two lists and return a reference to the zipped list.
# Try and keep additional space down to O(1)
# You have access to the Node class and all the properties on the Linked List
# class as well as the methods created in previous challenges.

# Example:
#   ll1 [1] [3]  [5] None
#       |  / |  / | /
#   ll2 [2] [4]  [6] None
# Result
# [1] -> [2] -> [3] -> [4] -> [5] -> [6]
# current1 = 1 > 3 > 5 > None
# current2 = 2 > 4 > 6 > None
# temp1 = 3 > 5 > None
# temp2 = 4 > 6 > None
# Zipped LL
# [1] -> [2] -> [3] -> [4] -> [5] -> [6] - None
# 1 - None
# |
# 2 - 4 - None
# current1 = 1
# current2 = 2


def zip_ll(ll1, ll2):
    if ll1.head is None and ll2.head is None:
        return 'Need to provide at least 1 linked_list'
    elif ll1.head is None or ll2.head is None:
        return ll1 or ll2

    current1 = ll1.head
    current2 = ll2.head
    while current1 and current2:
        temp1 = current1.next
        temp2 = current2.next
        current1.next = current2
        if temp1:
            current2.next = temp1
        current1 = temp1
        current2 = temp2
    ll2.head = None
    return ll1

