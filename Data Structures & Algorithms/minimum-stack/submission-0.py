class MinStack:
    # how can i keep track of the minimum value???
    # dictionary?? how would i know the next min if i pop the min val
    # linked list?? how would i maintain a ll and get the min in o(1) time
    # heap (log n)
    # another stack? have a regular stack and a minstack?
    # lets say i put 1 on the stack so thats on reg stack and minstack
    # lets say i now push 2. where would that go? 
    # i always need to know the MIN value?? 


    def __init__(self):
        self.stack = []
        self.minstack = [] # how would this work??? 
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            self.minstack.append(min(val, self.minstack[-1]))
        else:
            self.minstack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
