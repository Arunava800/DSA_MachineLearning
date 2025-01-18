"""
Amit has been working with an organization called "Money Traders" for the pase few years.
The organization assigned him a task. For a given array/list of stack prices for 'N' days,
find the stock span for each day.
The span of the stocks price today is defined as the maximum number of consecutive days
(Starting from today and going backward) for which the stock was less than today's price.
Example:
    Stock price for 7 days [100, 80, 60, 70, 60, 75, 85] stock span is [1, 1, 1, 2, 1, 4, 6].
    Amit has to return an array list of span corresponding to each day stock price.
"""


def stock_span(price, n):
    s = []
    ans = []
    for i in range(n):
        while s != [] and price[s[-1]] < price[i]:
            s.pop()
        if s == []:
            ans.append(i+1)
        else:
            ans.append(i-s[i-1])
        s.append(i)
    return ans


pri= list(map(int,input().split()))

