import turtle
import random


#screen settings
width, height = 1600, 900
screen = turtle.Screen()
screen.setup(width, height)
screen.screensize(3 * width, 3 * height)
screen.bgcolor('black')
screen.delay(0)

#turtle settings
nik = turtle.Turtle()
nik.pensize(2)
nik.speed(9)
nik.setpos(-width // 3, -height // 2)
nik.color('red')


#1-system settig
gens = 9
axiom = 'XY'
chr_1, rule_1 = 'X', 'F[@[-X]+X]'
step = 80
angle = lambda: random.randint(0, 45)
stack = []
color = [0.35, 0.2, 0.0]
thickness = 20

def apply_rules(axiom):
    return ''.join([rule_1 if chr == chr_1  else chr for chr in axiom])

def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom

turtle.pencolor('white')
turtle.goto(- width // 2 + 60, height // 2 - 100)
turtle.clear()
turtle.write(f'generation: {gens}', font=("Arial", 69, "normal"))

axiom = get_result(gens, axiom)
nik.left(90)
nik.pensize(thickness)
for chr in axiom:
    nik.color(color)
    if chr == 'F' or chr == "X":
        nik.forward(step)
    elif chr =='@':
        step -= 6
        color[1] += 0.04
        thickness -= 2
        thickness = max(1, thickness)
        nik.pensize(thickness)

    elif chr == '+':
        nik.right(angle())

    elif chr == '-':
        nik.left(angle())
    elif chr == '[':
        angle_, pos_, = nik.heading(), nik.pos()
        stack.append((angle_, pos_, thickness, step, color[1]))
    elif chr == ']':
        angle_, pos_, thickness, step, color[1] = stack.pop()
        nik.pensize(thickness)
        nik.setheading(angle_)
        nik.penup()
        nik.goto(pos_)
        nik.pendown()

screen.exitonclick()
