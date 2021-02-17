# Game of Thrones - I https://www.hackerrank.com/challenges/game-of-thrones/problem

def gameOfThrones(s):
    cnt = {}
    for char in s:
        if char in cnt:
            cnt[char] += 1
        else:
            cnt[char] = 1

    odd = False
    for key in cnt:
        if cnt[key] % 2 == 1:
            if odd:
                return 'NO'
            odd = True
      
    return 'YES'   

print gameOfThrones('aaabbbb')  #YES   
print gameOfThrones('cdefghmnopqrstuvw')  #NO   
print gameOfThrones('cdcdcdcdeeeef')  #YES   

