class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        
        for canddy in candies:
            amount = canddy + extraCandies
            if amount >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result