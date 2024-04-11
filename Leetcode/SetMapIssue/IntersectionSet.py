# leetcode 349
# 4.1 

class solution(object):
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)

        return self.set_intersection(set1, set2)
    
    def set_intersection(self, set1, set2):
        if len(set1) > len(set2):
            return self.set_intersection(set2, set1)
        return [x for x in set1 if x in set2]
    
if __name__ == "__main__":
     s = solution()
     nums1 = [4,9,5]
     nums2 = [9,4,9,8,4]
     print(s.intersection(nums1, nums2))
