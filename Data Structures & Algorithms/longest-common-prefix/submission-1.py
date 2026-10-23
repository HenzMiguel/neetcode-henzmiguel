class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        longest = ""
        change = False
        size = min([len(s) for s in strs])

        for i in range(1, size + 1):
            prefix = ""
            for word in strs:
                if prefix == "":
                    prefix = word[:i]   
                if prefix != word[:i]:
                    change = True
                    break
            
            if change:
                break
            else:
                longest = prefix
        return longest
        