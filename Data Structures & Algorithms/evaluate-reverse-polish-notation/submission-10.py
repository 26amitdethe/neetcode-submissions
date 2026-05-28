class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t=="+" or t=="-" or t=="*" or t=="/":
                a = s.pop()
                b = s.pop()
                if t=="+":
                    s.append(b+a)
                elif t=="-":
                    s.append(b-a)
                elif t=="*":
                    s.append(b*a)
                elif t=="/":
                    s.append(int(b/a))
            else:
                s.append(int(t))
        
        return int(s[-1])