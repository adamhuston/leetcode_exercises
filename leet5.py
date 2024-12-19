'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u'
and they can appear in both lower and upper cases, more than once.
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        reverse_s = s[::-1]
        picked = []
        for i in reverse_s:
            if i in vowels:
                picked.append(i)
        print(picked)

        for i in s:
            if i in vowels:
                print("found " + i)
                # s[:i] = picked[0]
                # replace in place
                picked.pop(0)
                print("replaced with " + i)
                
    
a = Solution()

print(a.reverseVowels("hello genius"))