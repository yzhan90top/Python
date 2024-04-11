# 438 找到字符串中所有的字母异位词

class solution(object):

    def FAG(self, s: str, p: str):
        s_len, p_len = len(s), len(p)
        
        # exclude s smaller situation
        if s_len < p_len:
            return []

        # 对比窗口内的字母 用于存储的数组
        ans = []
        s_count = [0] * 26
        p_count = [0] * 26

        for i in range(p_len):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1
        
        if s_count == p_count:
            ans.append(0)

        for i in range(s_len - p_len):
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1

            if s_count == p_count:
                ans.append(i + 1)
        
        return ans
    
    def FAG1(self, s: str, p: str):
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []

        ans = []
        count = [0] * 26
        for i in range(plen):
            count[ord(s[i]) - 97] += 1
            count[ord(p[i]) - 97] -= 1
        
        differ = [c != 0 for c in count].count(True)

        if differ == 0:
            ans.append(0)

        for i in range(s_len - p_len):
            if count[ord(s[i]) - 97] == 1:
                differ -= 1
            elif count[ord(s[i]) - 97] == 0:
                differ += 1
            count[ord(s[i]) - 97] -= 1

            if count[ord(s[i + p_len]) - 97] == -1:
                differ -= 1
            elif count[ord(s[i + p_len]) - 97] == 0:
                differ += 1

            count[ord(s[i + p_len]) - 97] += 1

if __name__== "__main__":
    s = solution()
    s1 = "cbaebabacd"
    p = "abc"
    print(s.FAG(s1, p))