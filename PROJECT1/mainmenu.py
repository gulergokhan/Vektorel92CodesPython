import areasofdrawings.areas
import armstrong.armstrongnumbers
import circumferencesandperimeters.cirandper
import drawings.drawingswithturtle
import fibonaccisequence.fibonacci
import hollowsquare.hollowprogram
import hypotenus.calculatehypotenus
import palindrome.palindromenumbers
import perpendiculartriangle.drawpertri
import pyramid.drawpyramid



def mainmenu():
    
 print("╔══════════════════════════════╗")
 print("║           MAIN MENU          ║")
 print("║                              ║")
 print("║ 1.DRAWINGS                   ║")
 print("║ 2.AREAS OF DRAWINGS          ║")
 print("║ 3.CIRCUMFERENCES & PERIMETERS║")
 print("║ OF DRAWINGS                  ║")
 print("║ 4.CREATE A FIBONACCI SEQUENCE║")
 print("║ 5.FIND ARMSTRONG NUMBERS     ║")
 print("║ 6.FIND PALINDROME NUMBERS    ║")
 print("║ 7.BUILD A PYRAMID            ║")
 print("║ 8.HYPTOTENUS PROGRAM MENU    ║")
 print("║ 9.CREATE A PERPENDICULAR     ║")
 print("║ TRIANGLE                     ║")
 print("║ 10.CREATE A HOLLOW SQUARE    ║")
 print("║ 11.EXIT                      ║")
 print("╚══════════════════════════════╝")


 choose = input()

 if choose == '1' :

     drawings.drawingswithturtle.drawmenu()
     mainmenu()
    

 elif choose == '2' :
 
     areasofdrawings.area.areamenu()
     mainmenu()

 elif choose == '3' :

     circumferencesandperimeters.cirandper.cirandpermenu()
     mainmenu()
    
 elif choose == '4' :

     fibonaccisequence.fibonacci.fibmenu()
     mainmenu()
    
 elif choose == '5' :
    
     armstrong.armstrongnumbers.armmenu()
     mainmenu()
    
 elif choose == '6' :

     palindrome.palindromenumbers.palmenu()
     mainmenu()

 elif choose == '7' :

     pyramid.drawpyramid.pyrmenu()
     mainmenu()

 elif choose == '8' :

     hypotenus.calculatehypotenus.hypmenu()
     mainmenu()

 elif choose == '9' :

     perpendiculartriangle.drawpertri.trimenu()
     mainmenu()

 elif choose == '10' :

     hollowsquare.hollowprogram.holmenu()
     mainmenu()

 elif choose == '11' :

     exit()

 elif choose :

     print("The button you chose isn't exist.")

    
    
    


