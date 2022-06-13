class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        if amount==0:
            return 0
        INT_MAX=10001
        num_coins = [INT_MAX]*(amount+1)
        num_coins[0]=0
        for amt in range(1,amount+1):
            for coin in coins:
                if (amt-coin)>=0:
                    num_coins[amt] = min(num_coins[amt],1+num_coins[amt-coin])
        return num_coins[amt] if num_coins[amt]!=INT_MAX else -1






            
