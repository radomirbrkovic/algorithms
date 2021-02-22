# Beautiful Binary String https://www.hackerrank.com/challenges/beautiful-binary-string/problem


def beautifulBinaryString(b):
    n = len(b)
    index = 0
    result = 0

    while index <= n - 3:
        if b[index] == '0' and b[index + 1] == '1' and b[index + 2] == '0':
            index += 3
            result += 1
        else: 
            index += 1    

    return result


print beautifulBinaryString('0101010')    
print beautifulBinaryString('01100')    
print beautifulBinaryString('0100101010')    