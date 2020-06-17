class multifilter:
    
    def judge_half(pos, neg):
        return pos >= neg
    
    def judge_any(pos, neg):
        return pos >= 1

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, a, *funcs, judge=judge_any):
        self.a = a
        self.judge = judge
        self.funcs = funcs
 
    def __iter__(self):
        pos, neg = 0, 0
    
        for i in self.a:
            for j in self.funcs:
                if j(i) == True:
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield i
            pos, neg = 0, 0


def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0



a = [i for i in range(31)]  # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5)))  

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
   
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
   