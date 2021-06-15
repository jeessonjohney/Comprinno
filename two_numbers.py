'''
Pseudo code:


input = N
loop 1 to N
	a,b,n = input
    if n%2 = 0 then
        sol = max(a,b)//min(a,b)
    end if
    else
        sol = max(2*a,b)//min(2*a,b)
    end else
end loop
'''


N = int(input())
for _ in range (N):
    a,b,n=map(int, input().split())
    if n%2==0:
        ans=max(a,b)//min(a,b)
    else:
        ans=max(2*a,b)//min(2*a,b)
    print(ans)

