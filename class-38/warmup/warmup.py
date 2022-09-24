
# Given a list of linked-lists with values of single, positive integers, create a function to traverse the list and
# convert the list to a number, add the lists together and return the total value of all lists.
#
# The lists will be passed as parameters.
#
# ll1: [5]->[9]->[9] = 599
# ll2: [2]->[1]->[1] = 211
# ll3: [1]->[4]->[1] = 141
#
# Should return 951

def add_ll(lists):
    # assign a variable to track the total
    total_sum = 0
    # check if the incoming list is empty
    if len(lists) == 0:
        return total_sum

    # iterate through the list grab each ll
    for ll in lists:
        list_number = ''
        # traverse the ll
        current = ll.head
        # need to grab the value from each node but add it as a string
        # ll1: [5]->[9]->[9] = 599
        # ll2: [2]->[1]->[1] = 211
        # list_number = '211'
        # total_sum = 810
        while current:
            list_number += str(current.value)
            current = current.next
        total_sum += int(list_number)
        # traverse the ll and concat the value to my string
        # once done with the ll, make a num and add to total variable
    return total_sum
    # return the total
