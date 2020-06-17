class MoneyBox:
    def __init__(self, cap):
        self.cap = cap
        self.nal = 0
            
    def can_add(self, v):
        return v <= (self.cap - self.nal)  
    
    def add(self, v):
        self.cap += v    
    