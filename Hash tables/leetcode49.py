class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ht = {}
        for ele in strs:
            key = ''.join(sorted(ele))
            if (key not in ht):
                ht[key] = []
            ht[key].append(ele)

        ans = []
        for key in ht:
            ans.append(ht[key])

        return ans
