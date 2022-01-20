def find_duplicate(nums):
    if '' in nums or not nums or len(nums) == 1:
        return False
    if len(nums) <= 2 and nums[0] != nums[1]:
        return False
    result = finde(nums, 0, 0)

    return result

# 1 - Percorrer o Array a
# 2 -  se o array[0], for igual ao array[1]
# 3 - adicione +1 ao count
# 4 - armazene o valor em value


def finde(nums, count, value):
    if len(nums) == 1:
        return value
    for n in nums[1:]:
        # print(n, nums[0])
        if not isinstance(nums[0], int) or nums[0] <= 0:
            return False
        if nums[0] == n and nums[0] > value:
            count += 1
            value = n
            return finde(nums[1:], count, value)
    return finde(nums[1:], count, value)


print(find_duplicate([3, 1, 3, 4, 2]))

# Agradecimentos a Ederson Pinheiro - pelo auxilio na criação do requisito