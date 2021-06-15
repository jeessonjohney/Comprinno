'''
Pseudo code:

input = N
loop 1 to N
	heights = list()
	n = input
	heights = input of length n
	if length of heights is even then
	return no
	end if
	else
		if heights[1] and height[-1] is 1 then
			total+=1
			loop from 1 to length(height)//2 as i
				if height[i-1]+1 == height[i] then total+=1
			end loop
			loop from length(height)//2 to length(height)
				if height[i-1]-1 == height[i] then total+=1 
			end loop

			if length(height) == total then
			output yes
			end if
			else 
			output no
			end else

		end if
		else output no
	end else
end loop



	
    
end loop
'''



N = int(input())
for i in range(N):
    total = 0
    n = int(input())
    hgt = list(map(int, input().split()))[:n]
    if( len(hgt) %2 == 0): # if the given list has even number of elements, 
						   # then it means the given list does not have a middle element.
        print("no")
        pass
    else:
        if(hgt[0]==1 and hgt[-1]==1):
            total = total+1 

            for i in range(1,(len(hgt)//2)+1): # Loop to check left side 
                if(hgt[i-1]+1 == hgt[i]): # Check whether height increases by one
                    total = total+1 

            for i in range(len(hgt)//2 +1,len(hgt)): # loop to check right side
                if(hgt[i-1]-1 == hgt[i]): # Check whether height decreases by one
                    total = total+1

            if(total == len(hgt)): # if total is equal to length of height, 
								   # then we can say that the strip is valid
                print("yes")

            else:
                print("no")
                pass
        else:
            print("no")
