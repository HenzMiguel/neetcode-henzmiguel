from typing import List
from multiprocessing import Pool, cpu_count

class Solution:
    @staticmethod
    def prefix_check(args):
        strs, n = args
        prefix = strs[0][:n]

        for word in strs:
            if not word.startswith(prefix):
                return ""

        return prefix

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        size = min(map(len, strs))

        with Pool(cpu_count()) as pool:
            prefixes = pool.map(
                Solution.prefix_check,
                [(strs, i) for i in range(1, size + 1)]
            )

        return max(prefixes, key=len, default="")