import turtle


def get_pos_list(x,y):
    x_new = x+10
    y_new = y+10
    return (x_new, y_new)

def get_screen_pos(x,y):
    global x_pos
    x_pos = x

    global y_pos
    y_pos = y
    


turtle.onscreenclick(get_screen_pos)

my_var = get_pos_list(x_pos, y_pos)



print(my_var)
