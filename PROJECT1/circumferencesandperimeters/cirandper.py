def cirandpermenu():

    print("╔════════════════════════════════════════╗")
    print("║ CIRCUMFERENCE AND PERIMETER OF DRAWINGS║")
    print("║                                        ║")
    print("║1.CALCULATE CIRCUMFERENCE OF CIRCLE     ║")
    print("║2.CALCULATE PERIMETER OF SQUARE         ║")
    print("╚════════════════════════════════════════╝")
 

    choose = input()

    if choose == '1' :

        radius = int(input("Enter radius for calculation : "))

        pi = 3.14

        circumofcir = 2*pi*r

        print("The circumference of circle is : {}".format(circumofcir))
        



    if choose == '2' :

        side = int(input("Enter side for calculation : "))

        periofsqr = side*4

        print("The area of square is : {}".format(periofsqr))

