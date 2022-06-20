class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ways = [0]*(amount+1)
        ways[0]=1
        for coin in coins:
            for amt in range(coin,amount+1):
                ways[amt]+=ways[amt-coin]
        return ways[amount]
