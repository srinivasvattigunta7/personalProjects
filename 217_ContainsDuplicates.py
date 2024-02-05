

nums=[1,2,3,1]

def containsDuplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))


if __name__ == '__main__':
    print(containsDuplicate(nums))