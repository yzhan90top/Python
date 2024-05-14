# 4-2 
# leetcode 350
# 思考 有序的map或者set
# leetcode 242 202 290 205 451
import collections

class solution(object):

    def intersect(self, nums1: list[int], nums2: list[int]):
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        m = collections.Counter()
        for num in nums1:
            m[num] += 1

        intersection = list()
        for nums in nums2:
            if (count := m.get(num, 0)) > 0:
                intersection.append(num)
                m[num] -= 1
                if m[num] == 0:
                    m.pop(num)
    
        return intersection


if __name__ == "__main__":
    s = solution()
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(s.intersect(nums1, nums2))
