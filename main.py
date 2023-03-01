import random
import turtle as t
canvas = t.Screen()
canvas.bgcolor('yellow')

caterpillar = t.Turtle()
caterpillar.shape("square")
caterpillar.color('red')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

leaf = t.Turtle()
leafShape = ((0,0), (14,2), (18,6), (20,20), (6,18), (2,14))
t.register_shape("leaf", leafShape)
leaf.shape("leaf")
leaf.color("green")
leaf.speed(0)
leaf.penup()
leaf.hideturtle()

apple = t.Turtle()
apple.shape("circle")
apple.color("red")
apple.speed(0)
apple.penup()
apple.hideturtle()

turtle = t.Turtle()
turtle.shape("turtle")
turtle.speed(0)
turtle.penup()
turtle.hideturtle()

square = t.Turtle()
square.shape("square")
square.color("black")
square.speed(0)
square.penup()
square.hideturtle()

triangle = t.Turtle()
triangle.shape("triangle")
triangle.color("blue")
triangle.speed(0)
triangle.penup()
triangle.hideturtle()

game_started = False
text_turtle = t.Turtle()
text_turtle.write("Press SPACE to start!",align='center', font=('Arial',16,'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.speed(0)
score_turtle.hideturtle()

def outside_window():
  leftWall = -t.window_width()/2
  rightWall = t.window_width()/2
  topWall = t.window_height()/2
  botWall = -t.window_height()/2
  (x,y) = caterpillar.pos()
  outside = x < leftWall or x > rightWall or y < botWall or y > topWall
  return outside

def gameOver():
  caterpillar.color("yellow")
  leaf.color("yellow")
  apple.color("yellow")
  t.penup()
  t.hideturtle()
  t.write("GAME OVER",align='center',font=("Arial",30,'bold'))

def displayScore(currentScore):
  score_turtle.clear()
  score_turtle.penup()
  x = (t.window_width()/2)-50
  y = (t.window_height()/2)-50
  score_turtle.setpos(x,y)
  score_turtle.write(str(currentScore),align='right',font=('Arial',40,'bold'))

def placeLeaf():
  leaf.hideturtle()
  leaf.setx(random.randint(-200,200))
  leaf.sety(random.randint(-200,200))
  leaf.showturtle()

def placeApple():
  apple.hideturtle()
  apple.setx(random.randint(-200,200))
  apple.sety(random.randint(-200,200))
  apple.showturtle()

def placeTurtle():
  turtle.hideturtle()
  turtle.setx(random.randint(-200,200))
  turtle.sety(random.randint(-200,200))
  turtle.showturtle()

def placeSquare():
  square.hideturtle()
  square.setx(random.randint(-200,200))
  square.sety(random.randint(-200,200))
  square.showturtle()

def placeTriangle():
  triangle.hideturtle()
  triangle.setx(random.randint(-200,200))
  triangle.showturtle()

def moveUp():
  caterpillar.setheading(90)

def moveDown():
  caterpillar.setheading(270)

def moveRight():
  caterpillar.setheading(0)

def moveLeft():
  caterpillar.setheading(180)

def startGame():
  global game_started
  game_started = True 
  score = 0
  text_turtle.clear()
  caterpillarSpeed = 2
  caterpillarLength = 3
  caterpillar.shapesize(1,caterpillarLength,1)
  caterpillar.showturtle()
  displayScore(score)

  while True:
    caterpillar.forward(caterpillarSpeed)
    if caterpillar.distance(leaf) < 20:
      placeLeaf()
      caterpillarLength += 1
      caterpillar.shapesize(1,caterpillarLength,1)
      caterpillarSpeed += 1
      score += 10
    if caterpillar.distance(apple) < 20:
      placeApple()
      caterpillarLength += 1
      caterpillar.shapesize(1,caterpillarLength,1)
      caterpillarSpeed += 1
      score += 15
    if caterpillar.distance(turtle) < 20:
      placeTurtle()
      caterpillarLength += 1
      caterpillar.shapesize(1,caterpillarLength,1)
      caterpillarSpeed += 1
      score += 25
    if caterpillar.distance(square) < 20:
      placeSquare()
      caterpillarLength += 1
      caterpillar.shapesize(1,caterpillarLength,1)
      caterpillarSpeed += 1
      score += 5
    if caterpillar.distance(triangle) < 20:
      placeTriangle()
      caterpillarLength += 1 
      caterpillar.shapesize(1,caterpillarLength,1)
      caterpillarSpeed += 1
      score += 30
    displayScore(score)
    if outside_window():
      gameOver()
      break

t.onkey(startGame, 'space')
t.onkey(moveUp, 'Up')
t.onkey(moveDown, 'Down')
t.onkey(moveLeft, 'Left')
t.onkey(moveRight, 'Right')
t.listen()
t.mainloop()
