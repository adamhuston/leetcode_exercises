'''
Given an integer array flowerbed containing 0's and 1's,
 where 0 means empty and 1 means not empty, and an integer n,
return true if n new flowers can be planted in the flowerbed
without violating the no-adjacent-flowers rule and false otherwise.
'''

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                count += 1
            if count >= n:
                return True
            i += 1
        return False