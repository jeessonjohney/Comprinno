'''
Pseudo Code:

function smaller(s1,s2)
    fl=true
    loop from 1 to 3 as i
        if s1[i] > s2[i] then return False
        if s1[i < s2[i] then set fl =true
    if end loop return fl


input = N
loop 1 to N
    scores=list()
    s1,s2,s3 = input 
    append s1,s2,s3 to scores
end loop
loop from 1 to 3 as i
    loop from i+1 to 3
        if scores[i][0] > scores[j][0] or
        (scores[i][0] == scores[j][0] and scores[i][1] > scores[j][1]) or 
        (scores[i][0] == scores[j][0] and scores[i][1] == scores[j][1] and scores[i][2] > scores[j][2])
        swap score[i] and score[j]
    end loop
end loop

loop 0 to 2 as i
    fl = True
    if smaller(score[i],score[j]) return False
        fl=False
if fl:
    output yes
else:
    output no



'''

def smaller(x,y):
	fl = False
	for i in range(3):
		if x[i] > y[i]:
			return False
		if x[i] < y[i]:
			fl = True
	return fl

N = int(input())
for _ in range(N):
    scores = []
    for i in range(3):
        scores.append(list(map(int, input().split(' '))))
    for i in range(3):
        for j in range(i+1,3):
            if scores[i][0] > scores[j][0] or (scores[i][0] == scores[j][0] and scores[i][1] > scores[j][1]) or (scores[i][0] == scores[j][0] and scores[i][1] == scores[j][1] and scores[i][2] > scores[j][2]):
                (scores[i], scores[j]) = (scores[j], scores[i]) #swapping  

    fl = True
    for i in range(2):
        if not smaller(scores[i], scores[i+1]): #check whether a ranking can be formed from given two members  
            fl = False # Ranking cannot be formed

    if fl:
        print("yes")
    else:
        print("no")
