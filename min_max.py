'''
Pseudo Code:
n = input
arr(list) = input 
min_cost = arr.sort
min_cost = min_cost[0] * (n-1)
output min_cost
Time Complexity: O(nlogn+N)
'''

N = int(input())

for _ in range(N):
    n = int(input())
    arr = list(map(int,input().split()))
    print(sorted(arr[:n])[0]*(n-1))
