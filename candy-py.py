class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0

        candies = [1] * len(ratings)  

        # Left to right pass
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right to left pass
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1) # keeps min

        return sum(candies)