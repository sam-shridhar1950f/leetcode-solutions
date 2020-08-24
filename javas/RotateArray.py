def rotateArray(nums, k):
    x = None

    if k < 0 or len(nums) < 1:
        return print(x)


    if k > len(nums):
        k = k - len(nums)


    lis = []
    for i in range(0, k):
        lis.append(nums[len(nums) -1 - i])

    good_lis = lis[::-1] + nums[0:len(nums) - k]
    nums.clear()
    nums.extend(good_lis)

    


    return nums


rotateArray([1, 2], 3)

