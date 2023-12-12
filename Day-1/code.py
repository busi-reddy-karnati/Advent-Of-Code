def left(s):
    for i in range(len(s)):
        if s[i].isnumeric():
            return int(s[i])
    return 0
def right(s):
    for i in range(len(s)):
        if s[len(s)-1-i].isnumeric():
            return int(s[len(s)-1-i])
    return 0
def process(s):
    return left(s)*10+right(s)
ans = 0
with open('input.txt') as file:
    for line in file:
       ans += process(line)
print(ans)