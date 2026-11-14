import turtle

# 1. 화면 설정
wn = turtle.Screen()
wn.title("배고픈 거북이 게임 - 1주차")
wn.bgcolor("lightgreen")
wn.setup(width=600, height=600)

# 2. 주인공 거북이(플레이어) 설정
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()

# 3. 먹이 설정
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(100, 100) # 임시 위치

wn.mainloop() # 창이 닫히지 않게 유지
