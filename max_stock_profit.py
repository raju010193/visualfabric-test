"""Find the max profit based on stock share value
"""
def max_profit(arr, buying_date):
    max_p = 0
    for i in range(len(arr)):
        if buying_date - 1 >= i:
            continue
        profit_value = arr[i] - arr[buying_date - 1]
        if max_p < profit_value:
            max_p = profit_value
    return max_p

# print("Enter stock prices")
# arr = list(map(int, input().split()))
# print("Enter stock purchased Date")
# purchased = int(input())
# profit = max_profit(arr, purchased)
# print("Total Profit ", profit)

print(max_profit([7,1,5,3,6,4], 2))
print(max_profit([], 4))
print(max_profit([7,6,-1,3,1], 4))