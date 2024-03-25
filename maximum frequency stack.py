class FreqStack:

    def __init__(self):
        self.set = defaultdict(list)
        self.freq = defaultdict(int)
        self.maxfreq = 0
        
    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.maxfreq = max(self.maxfreq, self.freq[val])
        self.set[self.freq[val]].append(val)


            
    def pop(self) -> int:
        val = self.set[self.maxfreq].pop()
        self.freq[val] -= 1
        if not self.set[self.maxfreq]:
            self.maxfreq -= 1
        return val
            
        
   
