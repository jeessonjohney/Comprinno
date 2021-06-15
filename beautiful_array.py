'''
Pseudo Code:

function solution(a)
    loop from 0 to length of a-2 as i
        if a[i] != a[i+1] then
            if a[i]*a[i+1] is not in list a then
                return False
            end if
            else continue loop
        enf if
    end loop and return True



input = N
loop 1 to N
    n = input
	a = list of length n
	a = input
	if length of a is 1 then
	    return no
	end if
	else
        if solution(a) returns True then
            output yes
        end if
        else
            output no
        end else
    end else
end loop

Time Complexity: O(N + (n-1))
'''


def solution(a):
    for i in range(0,len(a)-1):
        if a[i] != a[i+1]:
            if a[i]*a[i+1] not in a:  # check if the product is in the list a
                return False # if product is not in the list then the array is not beautiful array
    return True
            

N = int(input())
for i in range(N):
    n = int(input())

    a = list(map(int, input().split(" ")))
    if len(a) == 1:
        print("no")
    else:
        if solution(a):
            print("yes")
        else:
            print("no")
