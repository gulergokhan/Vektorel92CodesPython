def drawmenu():

print("╔═════════════════════╗")
print("║    DRAWING MENU     ║")
print("║                     ║")
print("║ 1.DRAW A CIRCLE     ║")
print("║ 2.DRAW A SQUARE     ║")
print("╚═════════════════════╝")


choose = input()

if choose == '1' :
    

    radius = int(input("Enter the radius for calculation : "))

    turtle.color("blue")
    turtle.fillcolor("yellow")
    turtle.goto(10,0)

    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(2*radius)
    turtle.end_fill()
    turtle.pendown()


elif choose == '2' :

    side = int(input("Enter the side for calculation : "))

    turtle.color("red")
    turtle.fillcolor("blue")
    turtle.goto(100,0)
    turtle.begin_fill()


    for i in range (4):

        turtle.forward(100)
        turtle.left(90)

    turtle.end_fill()
     turtle.setheading(0)
     


    
                

    
    
    

   
        
