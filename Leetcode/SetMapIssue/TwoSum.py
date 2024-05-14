#leetcode 1
#practice 15 18 16

class solution:

    def twoSum(self, nums, target):
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i

        return []
    
if __name__ == "__main__":
    s = solution()
    nums = [2,7,11,15]
    target = 9
    print(s.twoSum(nums, target))