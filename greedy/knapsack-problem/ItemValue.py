# Item  Value data class
class ItemValue:

    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.const = val // wt

    def __lt__(self, other):    
        return self.const < other.const