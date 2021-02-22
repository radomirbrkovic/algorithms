# Flipping bits https://www.hackerrank.com/challenges/flipping-bits/problem

def flippingBits(n):
    baseBin = bin(n).replace("0b", "") 
    outputBin = ""
    baseBin = "0" * (32 - len(baseBin)) + baseBin
    
    for i in baseBin:
        if i == '1':
            outputBin += '0'
        else:
            outputBin += '1'    

    return int(outputBin, 2) 


print flippingBits(4) # 4294967291
print flippingBits(123456) # 4294843839