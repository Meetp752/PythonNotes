


def selectionSort(nums):

    for i in range(len(nums)-1):

        min_idx = i

        for j in range(i+1, len(nums)):
            print(j)
            if nums[j] < nums[min_idx]:
                min_idx = j

        print('J: ', j ,'i: ', i, 'INDEX : ', min_idx)

        print(nums)
        nums[i], nums[min_idx] = nums[min_idx], nums[i]



nums = [5, 3, 8, 6, 7, 2]
selectionSort(nums)
