'''
Pseudo Code:

input  =  N
loop 1 to N
    n  =  input
    list_  =  input 
    r  =  1
    sa  =  dicttionar of list_
    new_list  =  sa.sort
    new_list  =  new_list.reversed
    sides  =  4
    m  =  0

    loop elements in new_list as element
        if element > 1 then
            if element > =  sides then
                m  =  element - (element-s)
            end if
            else
                m  =  s-(element-(element%2))
            end else
            s  =  s-m
            r  =  r*(element**(m//2)) 
            if sides  =  0 then 
                break
            end if
        end if
    end loop
if s  =  0 then
    output r
else output -1

Time Complexity: O(N+n)

'''
from collections import Counter

N = int(input())

for _ in range(N):

    n = int(input())
    list_ = list(map(int, input().split()))
    r = 1
    sa = Counter(list_)
    new_lst = list(reversed(sorted(list(sa.items())))) # sort in non-increasing way
    s = 4
    m = 0

    for i in new_lst:

        if(i[1] > 1):

            if(i[1] >= s):
                m = i[1]-(i[1]-s)

            else:
                m = s-(i[1]-(i[1]%2))
            s -= m
            r*= (i[0]**(m//2))  

            if(s == 0):
                break
                
    if s == 0:
        print(r)

    else:
        print(-1)

