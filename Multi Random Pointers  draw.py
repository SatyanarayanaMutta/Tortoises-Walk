import turtle,random
window=turtle.Screen()
t=turtle.Turtle()
t.penup()
t.shape('turtle')
t1=turtle.Turtle()
t1.shape("turtle")
t1.penup()
t2=turtle.Turtle()
t2.penup()
t2.shape("turtle")

c=turtle.Turtle()
c.shape("turtle")
c.penup()
s=turtle.Turtle()
s.shape("turtle")
s.penup()
tr=turtle.Turtle()
tr.shape("turtle")
tr.penup()
colors=["red","green","yellow","pink","blue"]
def rand():
    return random.randint(1,180)
def distance():
    return random.randint(-250,250)
def size():
    return random.randint(1,4)

while True:
    #window.bgcolor(random.choice(colors))
    t.left(rand())
    t.shapesize(size())
    t.color(random.choice(colors),"red")
    t.forward(distance())
    t1.left(rand())
    t1.shapesize(size())
    t1.color(random.choice(colors),"pink")
    t1.forward(distance())
    t2.left(rand())
    t2.shapesize(size())
    t2.color(random.choice(colors),"blue")
    t2.forward(distance())
    tr.left(rand())
    tr.shapesize(size())
    tr.color(random.choice(colors),"green")
    tr.forward(rand())

    c.left(rand())
    c.shapesize(size())
    c.color(random.choice(colors),"blue")
    c.forward(rand())

    s.left(rand())
    s.shapesize(size())
    s.color(random.choice(colors),"black")
    s.forward(rand())

