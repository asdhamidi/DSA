class Conversion:
    def __init__(self):
        self.top = -1
        self.stack = []
        self.output = []
        self.result = []
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

    def is_empty(self):
        return self.top == -1

    def peek(self):
        return self.stack[self.top]

    def pop(self):
        if not self.is_empty():
            self.top -= 1
            return self.stack.pop()
    def show_output(self):
        [print(x, end="") for x in self.output]
        print(" = ", self.result[0])
    def push(self, data):
        self.top += 1
        self.stack.append(data)

    def is_operand(self, data):
        return data.isalpha() or data.isnumeric()

    def is_not_greater(self, data):
        try:
            a = self.precedence[data]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False
			
    
    def convert(self, infix):
        for c in infix:
            if self.is_operand(c):
                self.output.append(c)
            else:
                while (not self.is_empty() and self.is_not_greater(c)):
                    self.output.append(self.pop())
                self.push(c)
                
        while self.top != -1:
            self.output.append(self.stack[self.top])
            self.top -= 1
    
    def eval(self):
        for c in self.output:
            if self.is_operand(c):
                self.result.append(int(c))
            else:
                current = []
                for r in range(2):
                    current.append(self.result.pop())
                if c == "+":
                    self.result.append(current[1] + current[0])
                elif c == "-":
                    self.result.append(current[1] - current[0])
                elif c == "*":
                    self.result.append(current[1] * current[0])
                else:
                    self.result.append(current[1] / current[0])

if __name__ == "__main__":
    obj = Conversion()
    obj.convert("1+2-3*4")
    obj.eval()
    obj.show_output()