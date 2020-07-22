def rotateArray(nums, k):
    x = None

    if k < 0 or len(nums) < 1:
        return print(x)


    if k > len(nums):
        k = k - len(nums)


    lis = []
    for i in range(0, k):
        lis.append(nums[len(nums) -1 - i]) # For loop adding elements to be shifted to a list

    good_lis = lis[::-1] + nums[0:len(nums) - k]
    nums.clear()
    nums.extend(good_lis)
    # nums = lis[::-1] + nums[0:len(nums) - k]
    


    return print(nums) # list of elements needed to be shifted reversed, so that elements not to be shifted can be added back
    # Can do this with one for loop by combining two lists, one with shifted values and one with inplace values


rotateArray([1, 2], 3)

