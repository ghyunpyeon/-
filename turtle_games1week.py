import turtle
import random # 랜덤 모듈 추가

wn = turtle.Screen()
wn.title("배고픈 거북이 게임 - 3주차")
wn.bgcolor("lightgreen")
wn.setup(width=600, height=600)
wn.tracer(0) # 화면 업데이트 지연 방지 (부드러운 움직임)

player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(100, 100)

move_speed = 20

def go_up(): player.setheading(90); player.forward(move_speed)
def go_down(): player.setheading(270); player.forward(move_speed)
def go_left(): player.setheading(180); player.forward(move_speed)
def go_right(): player.setheading(0); player.forward(move_speed)

wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# --- 3주차 추가 코드: 메인 루프 및 충돌 감지 ---
while True:
    wn.update() # 화면 갱신
    
    # 거북이와 먹이 사이의 거리가 20 미만이면 (닿으면)
    if player.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y) # 먹이를 새로운 랜덤 위치로 이동
