class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []
        max_candies = max(candies)
        for candy in candies:
            result.append(candy + extraCandies >= max_candies)
        
        return result
    
a = Solution()

print(a.kidsWithCandies([4, 3, 2, 1], 1))
