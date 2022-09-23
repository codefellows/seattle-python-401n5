
# Code Challenge
# Code challenge of:
#  - Given a list, reverse the list. In place, no built in methods / functions
#  - Once they get that, update the problem,
#  - Given a linked-list reverse the ll

def reverse_list(lst):
    # 2 pointers begining and end, one incrementing, other decrementing, swap the values
    # [1, 2, 5, 3, 4]
    #  ^        ^
    # [4, 2, 5, 3, 1]
    #     ^     ^
    # [4, 3, 5, 2, 1]
    #        ^
    for i in range(len(lst) // 2):
        lst[i], lst[- 1 - i] = lst[-1 - i], lst[i]
    return lst


print(reverse_list([1, 2, 3, 4]))
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list([1, 2]))
print(reverse_list([1]))
print(reverse_list([(1, ), (2,), (3, )]))
print(reverse_list([1, '_', 3, -4]))


def reverse_ll(ll):
    # [1]  [2]  [3] [4] None
    #                ^
    # [4] -> [3] -> [2] -> [1] -> None
    # current: None
    # previous: 4
    # temp_next: None
    previous = None
    current = ll.head

    while current:
        temp_next = current.next
        current.next = previous
        previous = current
        current = temp_next
    ll.head = previous
    return ll






    return ll
