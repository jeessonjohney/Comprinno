class fib:
    def __init__(self):
        self.l = {}
        self.str_ = ""

    def fib(self,char,start):

        ch = start
        occ = 1
        fl = False
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
        i=0
        j=1
        fl=None
        if len(self.str_) == 0:
            return False
        if len(self.str_) == 1:
            self.l[self.str_[i]] = 1
        while j < len(self.str_) and len(self.str_)>1:
            if self.str_[i] not in self.l:
                self.l[self.str_[i]] = 0
            j,fl = self.fib(i,j)
            i=j
            j=j+1
            if i == len(self.str_)-1 and not fl:
                if self.str_[i] not in self.l:
                    self.l[self.str_[i]] = 0
                self.l[self.str_[i]]+=1
                break
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
