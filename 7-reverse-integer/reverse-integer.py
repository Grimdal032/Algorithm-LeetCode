class Solution:
    def reverse(self, x: int) -> int:
        if x>0: #양수
            value = int(str(x)[::-1])
        else:   #음수
            value = -1*int(str(x*-1)[::-1])
        if value not in range(-2**31-1, 2**31): # 범위 밖
            value = 0
        return value