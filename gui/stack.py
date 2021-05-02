## stack

class StackClass():

    def __init__(self):  # constructor
        self.stack = []

    # accessors

    def get_stack_elements(self):       # accessor method to get stack
        return self.stack

    def get_stack_top_element(self):        # accessor method dedicated to top element of stack
        if not self.stack:
            return None

        return self.stack[-1]

    def get_stack_length(self):     # accessor method for length of stack
        return len(self.stack)

    # mutators

    def push_stack(self, item):     # mutator method for pushing into stack
        self.stack.append(item)

    def pop_stack(self):        # mutator method for popping from stack
        if not self.stack:
            return None
        top_item = self.get_stack_top_element()
        self.stack.pop()
        return top_item


if __name__ == '__main__':
    s = StackClass()

    print(s.get_stack_top_element())
    print(s.get_stack_length())
    s.pop_stack()
    s.push_stack(1)
    s.push_stack(3)
    print(s.get_stack_top_element())
    print(s.pop_stack())
    print(s.pop_stack())
    print(s.pop_stack())
