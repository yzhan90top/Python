#3-7 滑动窗口
#209 Minimum Size Subarray Sum

class solution(object):
        
    def Msss(self, target, nums):
       if not nums:
           return 0
       
       n = len(nums)
       ans = n + 1
       l, r = 0, 0
       sum += 1

       while r < n:
           sum += nums[r]
           while sum >= target:
               ans = min(ans, r - l + 1)
               sum -= nums[l]
               l += 1
           r += 1
       return 0 if ans == n+1 else ans

    def Msss1(self, target, nums):
        if not nums:
            return 0
        
        n = len(nums)
        l, r =0, -1
        sum = 0
        res = n+1

        while l < n:
            if r + 1 < n and sum < target:
                r += 1
                sum += nums[r]
            else:
                sum -= nums[l]
                l += 1
            
            if sum >= target:
                res = min (res, r - l +1)
        
        return 0 if res == n+1 else res


if __name__ == "__main__":
    
    s = solution()
    target = 7
    nums = [2,3,1,2,4,3]
    print(s.Msss1(target,nums))

