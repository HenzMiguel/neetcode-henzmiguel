class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for num in num_set:
            # Verifica se é o início de uma sequência
            if num - 1 not in num_set:
                current_length = 1

                # Conta quantos números consecutivos existem
                while num + current_length in num_set:
                    current_length += 1
                max_length = max(max_length, current_length)

        return max_length

