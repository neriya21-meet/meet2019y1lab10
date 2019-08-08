##import turtle
##
##
##
##turtle.register_shape("gif1.gif")
##p1= turtle.clone()
##p1.shape("gif1.gif")
##
##turtle.register_shape("gif2.gif")
##p2= turtle.clone()
##p2.shape("gif2.gif")
##
##turtle.register_shape("gif3.gif")
##p3=turtle.clone()
##p3.shape("gif3.gif")
##
##turtle.register_shape("gif4.gif")
##p4 = turtle.clone()
##p4.shape("gif4.gif")
##
##turtle.register_shape("gif5.gif")
##p5= turtle.clone()
##p5.shape("gif5.gif")
##
##turtle.register_shape("gif6.gif")
##p6 = turtle.clone()
##p6.shape("gif6.gif")
##
##turtle.register_shape("gif7.gif")
##p7= turtle.clone()
##p7.shape("gif7.gif")
##
##turtle.register_shape("gif8.gif")
##p8 = turtle.clone()
##p8.shape("gif8.gif")
##
##turtle.register_shape("gif9.gif")
##p9 = turtle.clone()
##p9.shape("gif9.gif")
##                      
##
##
##
##
#####new turtle for piece num5
####turtle_5.shape(p5)
####turtle.register_shape(p6)
#####to each piece we have a turtle
####turtle_6 = turtle.clone()
#####new turtle for piece num6
####turtle_6.shape(p6)
####turtle.register_shape(p7)
#####to each piece we have a turtle
####turtle_7 = turtle.clone()
#####new turtle for piece num7
####turtle_7.shape(p7)
####turtle.register_shape(p8)
#####to each piece we have a turtle
####turtle_8 = turtle.clone()
#####new turtle for piece num8
####turtle_8.shape(p8)
####turtle.register_shape(p9)
#####to each piece we have a turtle
####turtle_9 = turtle.clone()
#####new turtle for piece num9
####turtle_9.shape(p9)
##
##list_ piece[p1,p2,p3,p4,,p5,p6,p7,p8,p9]

import turtle
turtle.goto(0,200)
turtle.goto(200,200)
turtle.goto(200,0)
turtle.goto(0,0)

turtle.goto(-200,0)
turtle.goto(-200,200)
turtle.goto(0,200)
turtle.penup()
turtle.goto(-200,0)
turtle.pendown()
turtle.goto(-400,0)
turtle.goto(-400,200)
turtle.goto(-200,200)
turtle.penup()
turtle.goto(-400,0)
turtle.pendown()
turtle.goto(-400,-200)
turtle.goto(-200,-200)
turtle.goto(-200,0)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(0,-200)
turtle.goto(-200,-200)
turtle.goto(200,-200)
turtle.goto(200,0)
turtle.goto(200,-400)
turtle.goto(-400,-400)
turtle.goto(-400,-200)
turtle.goto(-200,-200)
turtle.goto(-200,-400)
turtle.goto(0,-400)
turtle.goto(0,-200)



p1= ("gif1.gif")
p2 = ("gif2.gif")
p3 = ("gif3.gif")
p4= ("gif4.gif")
p5 = ("gif5.gif")
p6 = ("gif6.gif")
p7= ("gif7.gif")
p8 = ("gif8.gif")
p9 = ("gif9.gif")
turtle.register_shape(p1)
                       	#to each piece we have a turtle
turtle_1 = turtle.clone()
                              	#new turtle for piece num1
turtle_1.shape(p1)
turtle_1.shape(p1)

turtle.register_shape(p2)
turtle_2 = turtle.clone()
turtle_2.shape(p2)


turtle.register_shape(p3)
turtle_3 = turtle.clone()
                             	#new turtle for piece num3
turtle_3.shape(p3)

turtle.register_shape(p4)
turtle_4 = turtle.clone()
turtle_4.shape(p4)

turtle.register_shape(p5)
turtle_5 = turtle.clone()
turtle_5.shape(p5)


turtle.register_shape(p6)
turtle_6 = turtle.clone()
turtle_6.shape(p6)


turtle.register_shape(p7)
turtle_7 = turtle.clone()
turtle_7.shape(p7)

turtle.register_shape(p8)
turtle_8 = turtle.clone()
turtle_8.shape(p8)


turtle.register_shape(p9)
turtle_9 = turtle.clone()
turtle_9.shape(p9)

#list_pieces[p1,p2,p3,p4,p5,p6,p7,p8,p9]
#turtle = Turtle()
#screen = Screen()
turtle.penup()
#turtle = Turtle()
#screen = Screen()
turtle.onscreenclick(turtle.goto)
turtle.getscreen()._root.mainloop()

def distance(x1, x2, y1, y2):
    distance= sqrt((y2-y1)**2 + (x2-x1)**2)
    return distance


def check_puzzle_pos(click_x, click_y, square_x, square_y):
    distance= sqrt((y2-y1)**2 + (x2-x1)**2)
    if distance < 15:
        return True
    else:
        return False

turtle.mainloop


###def puzzle_pieces
   ## if p1 == True
    ##goto (
