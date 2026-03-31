class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        alredy = set()
        answer = []

        for i in range(len(nums) - 1):
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                t = f"{nums[i]}{nums[j]}{nums[k]}"
                if s == 0 and t not in alredy:
                    answer.append([nums[i], nums[j], nums[k]])
                    alredy.add(f"{nums[i]}{nums[j]}{nums[k]}")
                elif s < 0:
                    j+=1
                else:
                    k-=1
        return answer 