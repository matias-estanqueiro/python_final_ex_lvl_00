import turtle                           #Importo la libreria para utilizarla

turtle.getscreen()                      #Creo la ventana de turtle
turtle.setup(width=600, height=600)     #Defino caracteristicas de ventana, birome y puntero
turtle.bgcolor("black")                         
turtle.color("white", "#D62AD0")
turtle.pensize("5")
turtle.penup()                          #Levanto la birome para luego determinar inicio de figura
turtle.setx(-250)
turtle.sety(-100)

cont=0                                  #Variable para condicion de While()

turtle.pendown()                        #Bajo la birome para que escriba
turtle.begin_fill()                      

while(cont<=7):                         #Indico tamaño de lineas y angulos del dibujo
    turtle.forward(500)
    turtle.left(135)
    cont+=1

turtle.end_fill()                       #Relleno la figura con color
turtle.exitonclick()                    #Click para cerrar la ventana