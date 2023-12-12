allowed = {
    "blue":14,
    "green":13,
    "red":12
}
def possible(draw):
    ball_list = draw.split(",")
    for balls in ball_list:
        ball_ct, ball_color = balls.strip().split(" ")
        if int(ball_ct) > allowed[ball_color]:
            return False
    return True
def process(s):
    game_id, draws = s.split(":")
    draws = draws.split(";")
    for draw in draws:
        if not possible(draw):
            return 0
    return int(game_id.split(" ")[1])
ans = 0
with open('input.txt') as file:
    for line in file:
       ans += process(line)
print(ans)