#5.5.4 Stack + Que = Deque
#Deque: Que who has stack and questionue's func. Actually is Que who has open/close
# funcs: pop(), leftpop()

def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

def another_palindrome(word):
    return word == word[::-1]

print(palindrome('a'))
print(palindrome('abc'))
print(palindrome('racecar'))
print(palindrome(''))
print(palindrome('radar'))
print(palindrome('halibut'))
print('\n')

print(another_palindrome('a'))
print(another_palindrome('abc'))
print(another_palindrome('racecar'))
print(another_palindrome(''))
print(another_palindrome('radar'))
print(another_palindrome('halibut'))
print('Spring'[::-1])
