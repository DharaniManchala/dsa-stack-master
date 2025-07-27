"""
✅ Problem Statement: Stock Span Problem
Given a list of daily stock prices, the span of the stock's price on a given day is defined as:
  → the maximum number of consecutive days (starting from that day and going backwards)
     for which the stock price was **less than or equal** to the current day's price.

📥 Input:  prices = [100, 80, 60, 70, 60, 75, 85]
📤 Output: spans  = [1,   1,  1,  2,  1,  4,  6]

✅ Brute Force Approach
🧠 Logic:
For each day `i`, go backwards and count how many previous days had stock prices
less than or equal to `prices[i]`. Include the current day itself.

🔁 Outer loop → for each day
🔁 Inner loop → go back until price is greater

⏱️ Time Complexity: O(n²) – Worst case: checking each day against all previous days
🧠 Space Complexity: O(n) – To store the span array
"""

# ✅ Brute Force Code
class StockSpan:
    def __init__(self):
        self.prices = []

    def next(self, price):
        self.prices.append(price)
        span = 1
        i = len(self.prices) - 2  # start from previous day
        while i >= 0 and self.prices[i] <= price:
            span += 1
            i -= 1
        return span

if __name__ == "__main__":
    s = StockSpan()
    print(s.next(100))  # Output: 1
    print(s.next(80))   # Output: 1
    print(s.next(60))   # Output: 1
    print(s.next(70))   # Output: 2
    print(s.next(60))   # Output: 1
    print(s.next(75))   # Output: 4
    print(s.next(85))   # Output: 6

# optimal approach
class stockspanner:
    def __init__(self):
      self.stack=[]
    def next(self,price):
        span=1
        while self.stack and self.stack[-1][0]<=price:
            span+=self.stack.pop()[1]
        self.stack.append((price,span))
        return span
if __name__=="__main__":
    s=stockspanner()
    print(s.next(100))  # Output: 1
    print(s.next(80))   # Output: 1
    print(s.next(60))   # Output: 1
    print(s.next(70))   # Output: 2
    print(s.next(60))   # Output: 1
    print(s.next(75))   # Output: 4
    print(s.next(85))   # Output: 6

    # time complexity: O(n)
    # space complexity: O(n)

