class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0, len(numbers) - 1

        while i<j:
            if numbers[i] + numbers[j] > target:
                j -= 1
                continue
            elif numbers[i] + numbers[j] < target:
                i += 1
                continue
            else:
                return [i+1,j+1]
            
            i += 1
            j -= 1
            
        