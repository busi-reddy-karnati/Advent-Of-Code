
def possible(draw):
    required = {
        "blue": 0,
        "green": 0,
        "red": 0
    }
    ball_list = draw.split(",")
    for balls in ball_list:
        ball_ct, ball_color = balls.strip().split(" ")
        required[ball_color] = max(required[ball_color], int(ball_ct))
    return required
def process(s):
    game_id, draws = s.split(":")
    draws = draws.split(";")
    required = {
        "blue": 0,
        "green": 0,
        "red": 0
    }
    for draw in draws:
        reqd_temp = possible(draw)
        for k in required:
            required[k] = max(required[k], reqd_temp[k])
    pro = 1
    for k in required:
        pro *= required[k]
    return pro
ans = 0
with open('input.txt') as file:
    for line in file:
       ans += process(line)
print(ans)