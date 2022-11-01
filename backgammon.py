from cs1graphics import Canvas, Rectangle, Polygon, Point, Text, Circle

spacing = int(input())  # 25
width = spacing**0.5*100  # 500
height = width  # 500
board = Canvas(width, height)
board.setBackgroundColor("navajowhite")

temp = Rectangle(width, spacing, Point(width/2, spacing/2))
temp.setFillColor("burlywood4")
temp.setBorderWidth(0)
board.add(temp)  # Top
temp = Rectangle(width, spacing, Point(width/2, width-spacing/2))
temp.setFillColor("burlywood4")
temp.setBorderWidth(0)
board.add(temp)  # Bottom
temp = Rectangle(spacing, height, Point(spacing/2, height/2))
temp.setFillColor("burlywood4")
temp.setBorderWidth(0)
board.add(temp)  # Left
temp = Rectangle(spacing, height, Point(width-spacing/2, height/2))
temp.setFillColor("burlywood4")
temp.setBorderWidth(0)
board.add(temp)  # Right
temp = Rectangle(spacing, height, Point(width/2, height/2))
temp.setFillColor("burlywood4")
temp.setBorderWidth(0)
board.add(temp)  # Middle

triangles = 6
for i in range(triangles):
    temp = Polygon(Point(i/triangles*(width/2-spacing*1.5)+spacing, height-spacing),
                   Point((i+1)/triangles*(width/2-spacing*1.5)+spacing, height-spacing),
                   Point((i+0.5)/triangles*(width/2-spacing*1.5)+spacing, height/2+spacing/2))
    temp.setFillColor(["darkorange3", "tan"][i % 2])
    board.add(temp)  # Bottom Left
    temp = Text(str(i+1), 12, Point((i+0.5)/triangles*(width/2-spacing*1.5)+spacing, height-spacing/2))
    board.add(temp)  # Bottom Left Text
    temp = Polygon(Point(width-i/triangles*(width/2-spacing*1.5)-spacing, height-spacing),
                   Point(width-(i+1)/triangles*(width/2-spacing*1.5)-spacing, height-spacing),
                   Point(width-(i+0.5)/triangles*(width/2-spacing*1.5)-spacing, height/2+spacing/2))
    temp.setFillColor(["darkorange3", "tan"][(i+1) % 2])
    board.add(temp)  # Bottom Right
    temp = Text(str(triangles*2-i), 12, Point(width-(i+0.5)/triangles*(width/2-spacing*1.5)-spacing, height-spacing/2))
    board.add(temp)  # Bottom Right Text
    temp = Polygon(Point(width-i/triangles*(width/2-spacing*1.5)-spacing, spacing),
                   Point(width-(i+1)/triangles*(width/2-spacing*1.5)-spacing, spacing),
                   Point(width-(i+0.5)/triangles*(width/2-spacing*1.5)-spacing, height/2-spacing/2))
    temp.setFillColor(["darkorange3", "tan"][i % 2])
    board.add(temp)  # Top Right
    temp = Text(str(triangles*2+i+1), 12, Point(width-(i+0.5)/triangles*(width/2-spacing*1.5)-spacing, spacing/2))
    board.add(temp)  # Top Right Text
    temp = Polygon(Point(i/triangles*(width/2-spacing*1.5)+spacing, spacing),
                   Point((i+1)/triangles*(width/2-spacing*1.5)+spacing, spacing),
                   Point((i+0.5)/triangles*(width/2-spacing*1.5)+spacing, height/2-spacing/2))
    temp.setFillColor(["darkorange3", "tan"][(i+1) % 2])
    board.add(temp)  # Top Left
    temp = Text(str(triangles*4-i), 12, Point((i+0.5)/triangles*(width/2-spacing*1.5)+spacing, spacing/2))
    board.add(temp)  # Top Left Text

for x, y in [[1, 1], [1, 2], [6, 7], [6, 8], [6, 9], [6, 10], [6, 11], [9, 9], [9, 10], [9, 11], [13, 1], [13, 2], [13, 3], [13, 4], [13, 5]]:
    temp = Circle(width/(triangles*2+3-1)/2*0.9, Point(x*(width/(triangles*2+3-1))+((width/(triangles*2+3-1)/2*0.9)/2 if x < (triangles*2+3-1)/2 else -(width/(triangles*2+3-1)/2*0.9)/2), y*(height/(10+3-1))))
    temp.setFillColor("white")
    board.add(temp)
for x, y in [[1, 10], [1, 11], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [9, 1], [9, 2], [9, 3], [13, 7], [13, 8], [13, 9], [13, 10], [13, 11]]:
    temp = Circle(width/(triangles*2+3-1)/2*0.9, Point(x*(width/(triangles*2+3-1))+((width/(triangles*2+3-1)/2*0.9)/2 if x < (triangles*2+3-1)/2 else -(width/(triangles*2+3-1)/2*0.9)/2), y*(height/(10+3-1))))
    temp.setFillColor("black")
    board.add(temp)
