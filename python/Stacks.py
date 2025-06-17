class Stack:
    def __init__(self,size):
        self.top = 0
        self.size = size
    def __len__(self):
        return self.size
    
    def push_into(self,data):
        if self.top == self.size:
            print("STACK IS FULL")
        else:
            self.stack[self.top] = data
            self.top +=1
        return self.stack
    
     
