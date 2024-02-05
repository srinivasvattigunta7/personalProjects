nums = [2,7,11,15]
target = 9

dict={}

res={}

def twoSum(nums: list[int],target: int) -> list[int]:
    for i,n in dict.items():
        if target-n in res:
            return [res[target - n], i]
        else:
            res[n]=i


if __name__ == '__main__':

    #! creating enum without using enumerate(nums)
    for i in range(len(nums)):
        dict[i] = nums[i]

    print(dict[0],dict[1])
    print(twoSum(nums,target))
