nums = [3, 2, 4]
target = 6

for num1 in nums:
    i = nums.index(num1)+1
    for num2 in nums[i:]:
        target1 = num1 + num2
        if target1 == target:
            print('Output:[ '+str(nums.index(num1))+',', nums.index(num2), ']')
