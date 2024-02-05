class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        copy = [0] + flowerbed + [0]
        
        for i in range(1, len(copy)-1):
            if copy[i-1] == 0 and copy[i] == 0 and copy[i+1] == 0:
                copy[i] = 1
                count += 1
        
        return count >= n