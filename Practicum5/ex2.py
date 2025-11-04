import turtle
xc = int(input())
yc = int(input())
r = int(input())
x = int(input())
y = int(input())
pen = turtle.Turtle()
pen.up()
pen.goto(xc, yc-r)
pen.down()
pen.circle(r)
pen.up()
pen.goto(x, y)
pen.dot(7, "red")
location = (x-xc)**2 + (y-yc)**2
if location > r**2:
    print("Точка вне окружности")
elif location == r**2:
    print("Точка на окружности")
else:
    print("Точка внутри окружности")
turtle.done()