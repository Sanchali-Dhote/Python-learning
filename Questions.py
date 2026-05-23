#Q22]Remove Leading zeros from a list of integers
#Write a function to remove leading zeros from a list of integers
#input: [0,0,1,2,0,3,0,0,4]
#output: 
# def remove_leading_zeros(lst):
#     while len(lst) > 0 and lst[0] == 0:
#         lst.pop(0)
#     return lst
# nums = [0,0,1,2,0,3,0,0,4]
# print(remove_leading_zeros(nums))
#================================================================
#Q24]Write a function to find the first missing positive integer in a list of unsorted integers.
#input:[3,4,-1,1]
#output:2
def first_missing_positive(nums):
    positive_nums = []

    for i in nums:
        if i > 0:
            positive_nums.append(i)

    missing = 1
    while missing in positive_nums:
        missing += 1
    return missing
nums = [3,4,-1,1]
print(first_missing_positive(nums))