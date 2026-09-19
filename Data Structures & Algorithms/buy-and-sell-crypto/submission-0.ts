class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices: number[]): number {
        let buy = prices[0];
        let maxPrice = 0;

        for (let i = 1; i < prices.length; i++) {
            if (prices[i] < buy) {
                buy = prices[i];
            }
            if (prices[i] - buy > maxPrice) {
                maxPrice = prices[i] - buy
            }
        }

        return maxPrice;
    }
}
