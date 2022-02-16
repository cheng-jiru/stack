class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop (self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
from pythonds.basic import Stack

def parChecker(symbolStrng):
    s=Stack()
    balanced = True
    i=0
    while i<len(symbolStrng) and balanced:
        symbol=symbolStrng[i]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced=False
            else:
                t=s.pop()
                if not matched(t,symbol):
                    balanced=False
        i=i+1
    if balanced and s.isEmpty():
        print("匹配成功")
    else:
        print("匹配不成功")
def matched(a,b):
    opens="([{"
    closers=")]}"
    return opens.index(a)==closers.index(b)
a="[)"
parChecker(a)

