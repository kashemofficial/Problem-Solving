class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = list(s)
        left, right = 0, len(arr) - 1
        vowels = "aeiouAEIOU"
        while left < right:
            if arr[left] not in vowels:
                left += 1
            elif arr[right] not in vowels:
                right -= 1
            else:
                arr[left],arr[right] = arr[right],arr[left]
                right -= 1
                left += 1
            return "".join(arr)




