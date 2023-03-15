def rectangle(width, height):
    import turtle
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

w = int(input('Введити ширину = '))
h = int(input('Введити высоту = '))    

rectangle(w, h)
