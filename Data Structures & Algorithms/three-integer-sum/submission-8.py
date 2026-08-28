class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    triplet = ([nums[i], nums[j], nums[k]])
                    if triplet not in res:
                        res.append(triplet)
                    j += 1
                    k -= 1

                elif total > 0:
                    k -= 1
                
                else:
                    j += 1

        print(res)
        
        return [list(triplet) for triplet in res]







        