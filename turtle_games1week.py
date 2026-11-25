import turtle

wn = turtle.Screen()
wn.title("배고픈 거북이 게임 - 2주차")
wn.bgcolor("lightgreen")
wn.setup(width=600, height=600)

player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(100, 100)

# --- 2주차 추가 코드: 이동 함수 ---
move_speed = 20

def go_up():
    player.setheading(90)
    player.forward(move_speed)

def go_down():
    player.setheading(270)
    player.forward(move_speed)

def go_left():
    player.setheading(180)
    player.forward(move_speed)

def go_right():
    player.setheading(0)
    player.forward(move_speed)

# 키보드 이벤트 연결
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

wn.mainloop()
