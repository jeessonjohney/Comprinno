'''
Pseudo Code:
loop from 1 to N
    n = input
    if n < 1500 then
        sol = 2*n
        output sol
    end if
    else
    sol = n+500+0.98*n
        output sol
    end else
end loop

Time Complexity: O(N)

'''

N = int(input())
for _ in range(N):
    n=int(input())
    if(n < 1500):
        print(2 * n)
    else:
        print(n + 500 + 0.98 * n)
