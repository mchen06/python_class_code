from stack import Stack
stack_0 =Stack()
def run_stack():
    to_push = input("please input an integer\n")
    stack_0.push(to_push)
    stack_0.print()
    to_push = input("please input an integer\n")
    stack_0.push(to_push)
    stack_0.print()
    stack_0.pop()
    stack_0.print()
