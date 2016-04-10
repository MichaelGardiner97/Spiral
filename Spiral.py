import turtle
wn = turtle.Screen()
michael = turtle.Turtle()
michael.speed(0)
crush = turtle.Turtle()
crush.speed(0)
squirt = turtle.Turtle()
squirt.speed(0)
joe = turtle.Turtle()
joe.speed(0)

color1 = input("Please state your first color (red, green, purple, blue, yellow, orange, turquoise): ").lower()
color2 = input("Please state your second (differnt) color (red, green, purple, blue, yellow, orange, turquoise): ").lower()
color3 = input("Please state your third (differnt) color (red, green, purple, blue, yellow, orange, turquoise): ").lower()
color4 = input("Please state your last (differnt) color (red, green, purple, blue, yellow, orange, turquoise): ").lower()

x = .5
for i in range(425):
    if color1 == ("red"):
        michael.color("red")
    elif color1 == ("green"):
        michael.color("green")
    elif color1 == ("purple"):
        michael.color("purple")
    elif color1 == ("blue"):
        michael.color("blue")
    elif color1 == ("yellow"):
        michael.color("yellow")
    elif color1 == ("orange"):
        michael.color("orange")
    else:
        michael.color("turquoise")
        
    michael.forward(x)
    michael.left(175)
    x = x+.5
    
    if color2 == ("green"):
        crush.color("green")
    elif color2 == ("red"):
        crush.color("red")
    elif color2 == ("purple"):
        crush.color("purple")
    elif color2 == ("blue"):
        crush.color("blue")
    elif color2 == ("yellow"):
        crush.color("yellow")
    elif color2 == ("orange"):
        crush.color("orange")
    else:
        crush.color("turquoise")
        
    crush.forward(x)
    crush.left(140)
    x = x+.5
    
    if color3 == ("yellow"):
        squirt.color("yellow")
    elif color3 == ("red"):
        squirt.color("red")
    elif color3 == ("purple"):
        squirt.color("purple")
    elif color3 == ("blue"):
        squirt.color("blue")
    elif color3 == ("green"):
        squirt.color("green")
    elif color3 == ("orange"):
        squirt.color("orange")
    else:
        squirt.color("turquoise")
        
    squirt.forward(.35*x)
    squirt.left(155)
    x = x+.5
    
    if color4 == ("blue"):
        joe.color("blue")
    elif color4 == ("yellow"):
        joe.color("yellow")
    elif color4 == ("red"):
        joe.color("red")
    elif color4 == ("purple"):
        joe.color("purple")
    elif color4 == ("green"):
        joe.color("green")
    elif color4 == ("orange"):
        joe.color("orange")
    else:
        joe.color("turquoise")
        
    joe.forward(.7*x)
    joe.left(165)
    x = x+.5

wn.exitonclick()
