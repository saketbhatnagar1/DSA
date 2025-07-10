class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        def isvowel(word):
            vowels = 'a,e,i,o,u,A,E,I,O,U'.split(',')
            if word in vowels:
                return True
            else:
                return False
        right = len(s)-1
        left = 0
        while left<right:
            if isvowel(s[left]) and isvowel(s[right]):
                s[left],s[right] = s[right],s[left]
                left+=1
                right-=1
            elif isvowel(s[left]):
                right-=1
            elif isvowel(s[right]):
                left+=1
            else:
                left+=1
                right-=1
        return "".join(s)
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        flag = True
        ans = ""
        
        while i < len(word1) and j < len(word2):
            if flag:
                ans += word1[i]
                i += 1
            else:
                ans += word2[j]
                j += 1
            flag = not flag

        # Append remaining characters
        ans += word1[i:]
        ans += word2[j:]
        
        return ans
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
        return n <= 0           
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        return " ".join(s[::-1])
            
        