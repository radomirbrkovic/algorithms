# Separate the Numbers https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separateNumbers(s):
    if len(s) == 1:
        print "NO"
        return
    else:
        for i in range(1, len(s) // 2 + 1):
            genstr = s[:i]
            prev = int(genstr) 

            while len(genstr) < len(s):
                next = prev + 1
                genstr = genstr + str(next)
                prev = next

            if genstr == s:
                print "YES "+ s[:i]
                return
                

    print "NO"

separateNumbers("1234")
separateNumbers("91011")
separateNumbers("99100")
separateNumbers("101103")
separateNumbers("010203")
separateNumbers("010203")
separateNumbers("13")
separateNumbers("1")
