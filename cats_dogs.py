'''
Pseudo Code:

function solution(c,d,l)
    f=0
    min = 4*(d+max(f,c-(2*d)))
    max = 4*(c+d)
    if l%4=0 and l<=max and l>=min then
        end function and return true
    end function and return False

input = N
loop 1 to N
	c,d,l = input
	
    if solution(c,d,l) is True then
        output yes
    end if
    else 
        output no
    end else

Time Complexity: O(N)
'''


def solution(c,d,l):
    f = 0
    min_ = 4*(d+max(f,c-(2*d))) # check how many cats can be accomodated by dogs and count the minimum number of legs
    max_ = 4*(c+d) #check maximum amount of legs that can be seen
    if l%4==0 and l<=max_ and l>=min_:
        return True
    return False    
            

N = int(input())
for i in range(N):
    c,d,l = list(map(int, input().split(" ")))
    if solution(c,d,l):
        print('yes')
    else:
        print("no")
