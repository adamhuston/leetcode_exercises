'''
My solution is very resource inefficient:

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        def multiply_elements(numlist):
            product = 1
            for num in numlist:
                product *= num
            return product
        
        answer = nums[:]
        
        for i in range(len(nums)):
            factors = nums[:i] + nums[i+1:]
            injection = multiply_elements(factors)
            answer[number] = injection
        return answer
    
a = Solution()
print(
    a.productExceptSelf([1,2,3,4])
)

Copilot proposed this significantly less complex solution:

'''

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        length = len(nums)
        answer = [1] * length
        
        left = 1
        for i in range(length):
            answer[i] = left
            left *= nums[i]
        right = 1
        for i in range(length -1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer
    
a = Solution()
print(
    a.productExceptSelf([1,2,3,4])
)