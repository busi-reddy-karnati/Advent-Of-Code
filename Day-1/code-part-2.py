list_of_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def left(s):
    ret = len(s)
    min_idx = len(s)
    for i in range(9):
        num = i+1
        num_in_str = list_of_nums[i]
        first_idx_num = s.find(str(num))
        first_idx_str = s.find(num_in_str)
        if first_idx_str != -1:
            if min_idx > first_idx_str:
                min_idx = first_idx_str
                ret = num
        if first_idx_num != -1:
            if min_idx > first_idx_num:
                min_idx = first_idx_num
                ret = num
    return ret
def right(s):
    ret = len(s)
    max_idx = -1
    for i in range(9):
        num = i + 1
        num_in_str = list_of_nums[i]
        last_idx_num = s.rfind(str(num))
        last_idx_str = s.rfind(num_in_str)
        maxi = max(last_idx_str, last_idx_num)
        if maxi > -1:
            if max_idx < maxi:
                max_idx = maxi
                ret = num
    return ret
def process(s):
    print(s, left(s), right(s))
    return left(s)*10+right(s)
ans = 0
with open('input.txt') as file:
    for line in file:
       ans += process(line)
print(ans)