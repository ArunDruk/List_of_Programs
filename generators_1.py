####################################################################################################
# def squares(nums):
#     for i in nums:
#         yield i*i


# nums=[1,5,6,2,3]

# mynum=squares(nums)
# print(mynum.__name__)
# for num in mynum:
#     print(num)
####################################################################################################

nums=[1,2,3,4]
# mynum=[num*num for num in nums] # list comprehension
# print(mynum)

mynum=(num*num for num in nums) # Generator 
print(mynum)  # Generator object
[print(num) for num in mynum]