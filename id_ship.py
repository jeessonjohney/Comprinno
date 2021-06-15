'''
Pseudo Code:
loop from 1 to N
    ch = input
    if ch = c or C then 
        output Cruiser
        end if 
        end loop
    if ch = b or B then
        output Battleship
        end if 
        end loop

    if ch = d or D then
        output Destroyer
        end if 
        end loop
    if ch = f or F then 
        output Fregate
        end if 
        end loop
end loop

Time Complexity: O(N)
'''

N = int(input())

for _ in range(N):
    ch = input()
    
    if(ch == "c" or ch == "C"):
        print("Cruiser")
    elif(ch == "b" or ch == "B"):
        print("BattleShip")
    elif(ch == "d" or ch == "D"):
        print("Destroyer")
    elif(ch == "f" or ch == "F"):
        print("Frigate")
