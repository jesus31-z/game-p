import turtle
import time

ventana = turtle.Screen()
ventana.title('Bolita')
ventana.bgcolor('purple')
ventana.setup(width=600, height=600)
ventana.tracer(0)

cosita = turtle.Turtle()
cosita.shape('square')
cosita.color('red')
cosita.shapesize(stretch_wid=1,stretch_len=5)
cosita.penup()
cosita.goto(0,-250)

bola = turtle.Turtle()
bola.shape('triangle')
bola.color('green')
bola.goto(0,0)
bola.dx = 4
bola.dy = -4

score = 0

gm = turtle.Turtle
gm.color('Red')
gm.penup
gm.speed(0)
gm.goto(0,0)
gm.hideturtle()

text = turtle.Turtle
text.color('white')
text.penup
text.speed(0)
text.goto(0,260)
text.hideturtle()
text.write('Score: 0', align='center', font= ('Courier',30,'normal'))

def mover_izquierda():
    x = cosita.xcor()
    if x > -240:
       cosita.setx(x - 50)
       
def mover_derecha():
    x = cosita.xcor()
    if x < 240:
       cosita.setx(x - 50)

ventana.listen()
ventana.onkeypress(mover_izquierda, 'Left')
ventana.onkeypress(mover_derecha, 'Right')

while True:
    ventana.update()
    time.sleep(0.02)

    bola.setx(bola.xcor()+bola.dx)
    bola.sety(bola.ycor()+bola.dy)

    if bola.xcor()>290 or bola.xcor()<-290:
        bola.dx *= -1
    
    if bola.ycor()>290:
        bola.dy *= -1

    if (bola.ycor()< -240 and bola.ycor()>-250) and (bola.xcor()< cosita.xcor()+ 55 and bola.xcor()> cosita.xcor()- 55):
        bola.sety(-240)
        bola.dy *= -1
        score *= 1
        text.clear()
        text.write(f'Puntos {score}', align='center',font= ('Arial',40,'bold'))

    if bola.ycor() < -290:
        gm.write('Que man tan malo', align='center', font=('Arial', 40, 'bold'))

        time.sleep(7)

        gm.clear
        bola.goto(0,0)
        bola.dy *= -1
        text.clear()
        text.write('Score: 0', align='center', font= ('Courier',30,'normal'))
