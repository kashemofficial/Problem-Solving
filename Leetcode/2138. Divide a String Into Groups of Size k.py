class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        l = len(s)
        r = l % k
        if r > 0:
            r = k - r
            for i in range(r):
                s += fill
        l = len(s)
        arr = []
        for i in range(0, l, k):
            arr.append(s[i:i + k:])
        return arr
