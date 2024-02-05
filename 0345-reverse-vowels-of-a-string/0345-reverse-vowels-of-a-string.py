class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        vol = [char for char in s if char in vowels]
        str = list(s)
        
        for i in range(len(s)):
            if str[i] in vowels:
                str[i] = vol.pop()
        return ''.join(str)
            