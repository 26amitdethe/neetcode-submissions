class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            print(s)
            if t=="+" or t=="-" or t=="*" or t=="/":
                a = int(s.pop())
                b = int(s.pop())
                if t=="+":
                    s.append(b+a)
                elif t=="-":
                    s.append(b-a)
                elif t=="*":
                    s.append(b*a)
                elif t=="/":
                    s.append(b/a)
            else:
                s.append(t)
        
        return int(s[-1])