## stack

class Stack():


    def __init__(self): # constructor
        self.stack = []


    # accessors

    def get_stack_elements(self):
        return self.stack

    def get_stack_top_element(self):
        return self.stack[-1]

    def get_stack_length(self):
        return len(self.stack)

    # mutators

    def push_stack(self, item):
        self.stack.append(item)

    def pop_stack(self):
        self.stack.pop()

