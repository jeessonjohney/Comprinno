'''
Pseudo Code:

N = input
    loop 1 to n 
    n = input
    s = list
    append input to s
    fl = False
    loop elements is s as action
        if action == 'Cookies' then
            if fl == True then
                output no
            end if
            else
                fl = true
            end else
        if action == 'milk' then
            fl = False
        end if
    end loop and return output yes
        
time complexity : O(N+n)
'''

def solution(actions):

    fl = False
    for action in actions:
        if action == 'cookie':
            if fl: # check whether he ate a cookie at previous minute. if so return false, he was suppose to drink to milk.
                return False
            else: # set flag to true stating that he ate a cookie 
                fl = True
        else:
            fl = False # He drank milk, and so set the flag to false
    return True


N = int(input())
for i in range(N):
    n = int(input())
    actions = list(map(str, input().split()))[:n]
    if len(actions) == 1:
        if actions[0] == 'cookie':
            print("no")
        else:
            print("yes")
    else:
        if solution(actions):
            print("yes")
        else:
            print("no")
    
