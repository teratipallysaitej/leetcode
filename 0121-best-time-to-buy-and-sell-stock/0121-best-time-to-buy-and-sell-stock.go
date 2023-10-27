func maxProfit(prices []int) int {
    mx := 0
    buy := prices[0]
    for i := 0;i<len(prices);i++ {
        if buy > prices[i] {
            buy = prices[i]
        }
        if prices[i] - buy > mx {
            mx = prices[i] - buy
        }
    }
    return mx
}