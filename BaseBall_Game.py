class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0
        record = []
        for i in range(len(operations)):
            try:
                int(operations[i])
                record.append(int(operations[i]))
            except:
                break

        print(record)
   
        ops = operations[len(record):]
        print(ops)

        for op in ops:
            if op == 'C':
                record.pop()
                print(record)
            elif op == 'D':
                record.append(2*int(record[-1]))
                print(record)
            elif op == '+':
                record.append(int(record[-1])+ int(record[-2]))
            elif op.lstrip('-').isdigit():
                record.append(int(op))

        print(record)
        return sum(record)
