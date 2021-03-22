class Stack:
    """an attempt at a stack class that only takes integers"""
    def __init__(self):
        self.stack_list = []
    
    def pop(self):
        pop_int = self.stack_list[0]
        del self.stack_list[0]
        return pop_int
    
    def push(self, to_push):
        try:
            int(to_push)
            self.stack_list.insert(0, to_push)
            return self.stack_list
        except ValueError:
            print("please input an integer")

    def print(self):
        print("start of stack-----------")
        for x in self.stack_list:
            print(x)
        print("end of stack-------------")

