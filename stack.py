## stack

class MathsStack():

    def __init__(self): # constructor
        self.stack = []


    # accessors

    def get_stack_elements(self):
        return self.stack

    def get_stack_length(self):
        return len(self.stack)

    # mutators

    def push_stack(self, item):
        self.stack.append(item)

    def pop_stack(self):
        self.stack.pop()


test_stack = MathsStack()

test_stack.push_stack('I')
test_stack.push_stack('wanna')
test_stack.push_stack('die')
test_stack.get_stack_elements()
test_stack.get_stack_length()

print(test_stack.get_stack_elements())
print(test_stack.get_stack_length())

test_stack.pop_stack()

print(test_stack.get_stack_elements())
print(test_stack.get_stack_length())