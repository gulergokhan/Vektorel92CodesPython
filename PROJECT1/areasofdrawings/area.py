def areamenu():

    print("╔════════════════════╗")
    print("║ AREAS OF DRAWINGS  ║")
    print("║                    ║")
    print("║1.CALCULATE AREA OF ║")
    print("║CIRCLE              ║")
    print("║2.CALCULATE AREA OF ║")
    print("║SQUARE              ║")
    print("╚════════════════════╝")


    choose = input()

    if choose == '1' :

        radius = int(input("Enter radius for calculation : "))

        pi = 3.14

        areaofcir = (pi*radius)

        print("The area of circle is : {}".format(areaofcir))
        



    if choose == '2' :

        side = int(input("Enter side for calculation : "))

        areaofsqr = side*side

        print("The area of square is : {}".format(areaofsqr))
