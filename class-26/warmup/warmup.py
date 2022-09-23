
def reverse_list(alist):
    left = 0
    right = len(alist) - 1

    if left > right:
        alist[left], alist[right] = alist[right], alist[left]
        left += 1
        right -= 1

    return alist


print(reverse_list([1, 2, 3, 4, 5, 6]))
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list([1, 2]))
print(reverse_list([1]))
print(reverse_list([]))
