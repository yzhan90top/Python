#leetcode 242
import collections

class solution(object):

    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        m = collections.Counter()
        for i in s:
            m[i] += 1
        
        for j in t:
            m[j] -= 1
            if (count:= m.get(j, 0)) < 0:
                return False
        
        return True

if __name__ == "__main__":
    solu = solution()
    s = "anagram"
    t = "nagaram"
    print(solu.isAnagram(s, t))
