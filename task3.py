def task3(nums: list, target: int):
    result_in_num = []
    dict_of_index = {}
    for num_index in range(0, len(nums)):
        second_num = target - nums[num_index]
        if second_num in dict_of_index:
            result_in_num.append(num_index)
            result_in_num.append(dict_of_index.get(second_num))
            return result_in_num
        dict_of_index[nums[num_index]] = num_index


nums = [3, 3, 3]
target = 6
print(task3(nums, target))
