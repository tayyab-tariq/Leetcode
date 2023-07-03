class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        ops = {'+': operator.add, '-': operator.sub, '/': operator.truediv, '*': operator.mul}
        for token in tokens:
            if token in ['+', '-', '/', '*']:
                a, b = numStack.pop(), numStack.pop()
                val = ops[token](b,a)
                numStack.append(int(val))
            else:
                numStack.append(int(token))
            
        return numStack[0]
