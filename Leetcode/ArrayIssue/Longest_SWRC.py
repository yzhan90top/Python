#3-8 滑动窗口
#3 Longest Substring Without Repeating Characters
#课后题 438 76

class solution(object):

    def LSWRC(self, s: str):
        occ = set()
        n = len(s)

        r, ans = -1, 0
        for i in range(n):
            if i != 0:
                occ.remove(s[i-1])
            while r + 1 < n and s[r+1] not in occ:
                occ.add(s[r+1])
                r += 1 
            
            ans = max(ans, r - i + 1)
        return ans
    
    # using frequency not set
    def LSWRC1(self, s: str):
        Freq = [0] * 26
        n = len(s)

        r, ans = -1, 0
        for i in range(n):
            if i !=0:
                Freq[ord(s[i-1])-97] ==0
            while r + 1< n and Freq[ord(s[r+1])-97] == 0:
                Freq[ord(s[r+1])-97] += 1
                r += 1

            ans = max(ans, r -i +1)
        return ans
        
if __name__ == "__main__":
    s = solution()
    print(s.LSWRC1("abcabcbb"))