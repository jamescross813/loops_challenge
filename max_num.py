#Write your function here
def max_num(nums):
    max_num = nums[0]
    for x in nums:
        if x > max_num:
            max_num = x
    return max_num
#Uncomment the line below when your function is done
#print(max_num([50, -10, 0, 75, 20]))