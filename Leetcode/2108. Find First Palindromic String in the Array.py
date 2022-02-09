'''class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if i == i[::-1]:
                return i
        else:
            return "" '''

def solve(w):
    for i in w:
        if i == i[::-1]:
            return i
    else:
        return ""

if __name__ == '__main__':
    w = list(map(str,input().split()))
    result = solve(w)
    print(result)
