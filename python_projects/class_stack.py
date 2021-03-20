class Stack:
    """an attempt at a stack class that only takes integers"""
    def __init__(self):
        self.stack_list = []
    
    def pop(self):
        self.stack_list.pop(0)
        return self.stack_list
    
    def push(self):
        to_push = input("what number are you pushing?\n")
        try:
            int(to_push)
            self.stack_list.insert(0, to_push)
            return self.stack_list
        except ValueError:
            print("please input an integer")

    def print_stack(self):
        print("start of stack-----------")
        for x in self.stack_list:
            print(x)
        print("end of stack-------------")
        
def run_stack():
    stack_0 = Stack()
    stack_0.push()
    stack_0.push()
    stack_0.print_stack()
    stack_0.pop()
    stack_0.print_stack()
