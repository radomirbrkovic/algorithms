#Happy Ladybugs https://www.hackerrank.com/challenges/happy-ladybugs/problem



def happyLadybugs(bugs):
    maping = {}
    freeCell = False
    happy = True


    for i, bug in enumerate(bugs):

        if i == 0 and i + 1 < len(bugs):
            happy = bug == bugs[i+1]
        elif i == len(bugs) - 1:
            happy = bugs[i - 1] == bug and happy
        else:
            happy = happy and (bugs[i-1] == bug or bugs[i+1] == bug)


        if bug == '_':
            freeCell = True
        elif bug in maping:
            maping[bug] += 1
        else:
            maping[bug] = 1

    singles = 0

    for bug, count in maping.items():
        if count == 1:
            singles += 1

    if singles > 0:
        return 'NO'
    
    if not freeCell:
        return 'YES' if happy else 'NO'
    
    return 'YES'                                        





print happyLadybugs("AABBC")
print happyLadybugs("AABBC_C")
print happyLadybugs("_")
print happyLadybugs("DD__FQ_QQF")
print happyLadybugs("AABCBC")