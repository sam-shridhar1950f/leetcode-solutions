def PalindromeNumber(x: int):
    if x < 0:
        return False
    else:
        if str(x)[::-1] == str(x): 
            return True
        else:
            return False
        
output = PalindromeNumber(818)
print(output)