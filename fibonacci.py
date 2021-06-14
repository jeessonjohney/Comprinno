'''
Pseudo Code:

function fib(char,start)
ch = start
occ = 1
fl = False
loop ch from start to length(input)
if char != ch then
    if input[char] = input[ch] then
    occ = occ+1
else break

if ch = length(input) - 1 then
    fl = True
else
    fl = False
list[input[char]] + = occ
return ch, fl
end function


function solution()
i=0
j=1
fl=False
if length of input < = 1 then 
return "Dynamic"
loop from i to length of input - 1
if input[i] is not in list then 
    list[input[i]] = 0
j,fl = function fib(i,j) 
i=j
j=j+1
if i == len(input)-1 and  fl is false then
    if input[i] is not in list
        list[input[i]] = 0
    list[input[i]]+=1
    break
list = sorted list
i=0
loop 0 to length of input - 2
if list[i] + list[i+1] != list[i+2]
    return "Not"
i+=1
return "Dynamic"
end function 


loop 1 to N
input string
print  solution(string)
'''

class fib:
    def __init__(self):
        # l holds the number of occurences of each string
        # str_ holds the given input string
        self.l = {}
        self.str_ = ""

    def fib(self,char,start):
        # ch is set to start.if the forloops range is out of bounds, 
        # ch must be still be returned and must contain the value of start.
        # occ is used for counting the frequency of contineous occurence of given ch/start
        # fl is initially false, and its set true when start is equal to length of string -1.
        ch = start
        occ = 1
        fl = False
        # for loop to check continuity of a character, if ch is equal to char then occ incremented by 1,
        # else the loop is stopped, flag (fl) and index where the loop broke is returned
        # if we have reached -2 position of the string, then fl will be set True
        for ch in range(start,len(self.str_)):

            if char != ch:
                if self.str_[char] == self.str_[ch]:
                    occ+=1
                else:
                    break
            if ch == len(self.str_)-1:
                fl = True
            else:
                fl = False
        self.l[self.str_[char]] += occ
        return ch, fl
    
    def solution(self):
        # this function returns solution. if string is not given, it returns "Dynamic" if 
        # given string has length lesses than 1
        # i is set 0 and will be the index of string we search for continuity
        # j is set 1 (i+1) this is the index from where the we will compare string[i] with and check contunuity
        i=0
        j=1
        fl=False
        if len(self.str_) <=1 :
            return "Dynamic"
        while j < len(self.str_) and len(self.str_)>1:
            if self.str_[i] not in self.l: #if the given character is new, we need to add it to the dictionary with occurences 0
                self.l[self.str_[i]] = 0
            j,fl = self.fib(i,j) #function fib() is called
            i=j
            j=j+1
            if i == len(self.str_)-1 and not fl:
                if self.str_[i] not in self.l:
                    self.l[self.str_[i]] = 0
                self.l[self.str_[i]]+=1
                break
        # The values are added to a list and sorted in non-decreasing order
        self.l = sorted(list(self.l.values()))
        i=0
        while i < len(self.l)-2:
            if self.l[i]+self.l[i+1]!=self.l[i+2]:
                return "Not"
            
            i+=1
        return "Dynamic"

N = int(input())
i=1
fib = fib()
while i <= N:
    fib.str_ =  input()
    fib.l = {}
    print(fib.solution())
    i+=1
