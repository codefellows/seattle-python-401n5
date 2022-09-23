# numss = [[1, 2, 3], [4, 5, 6]]

# Nested for loop


# def add_two_1(nums):
#     output = []
#     for arr in nums:
#         for num in arr:
#             output.append(num)

    # return output

# In Place


# [[1, 2, 3], [4, 5, 6]]
# def add_two_2(nums):
#     for arr in nums:
#         for i, num in enumerate(arr):
#             arr[i] = num + 2
#
#     return nums


# Nested list Comp

# def add_two_3(nums):
#     return [[num+2 for num in arr] for arr in nums]

# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

from calendar import month_name

months = list(name for name in month_name if name)


# print(months)
# i = 1
# for month in months:
#     print(month, i)
#     i += 1

for i, month in enumerate(months):
    print(month, i + 1)
