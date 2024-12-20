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
        list_s = list(s)
        for i in reverse_s:
            if i in vowels:
                picked.append(i)
            print(picked)

        for index, i in enumerate(list_s):
            if i in vowels:
                
                list_s[index] = picked[0]
                
                picked.pop(0)

        return "".join(list_s)
                
    
a = Solution()

print(a.reverseVowels("hello genius"))