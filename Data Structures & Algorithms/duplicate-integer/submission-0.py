class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        teste = set()
        for n in nums:
            if n not in teste:
                teste.add(n)
            else:
                return True
        return False