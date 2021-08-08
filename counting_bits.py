N = 5

def bits(N):
    ans = []
    for n in range(0, N + 1):
        if n == 0:
            ans.append(0)
        bits = list(bin(n)[2:])
        bits = list(filter(lambda a: a != '0', bits))
        if len(bits) != 0: ans.append(len(bits))
    return ans
print(bits(N))
        # extract num of 1s


