class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word):
            ans = [0]*26
            for letter in word:
                ans[ord(letter) - ord("a")] += 1
            return ans

        bmax = [0]*26
        for b in words2:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)

        ans = []
        for a in words1:
            if all(x >= y for x,y in zip(count(a), bmax)):
                ans.append(a)
        
        return ans
        