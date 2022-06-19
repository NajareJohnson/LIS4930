from graphics import * #Creating testing setting for Point() and graphics window. 
def main():
    win = GraphWin("Assignment 5",500,500)
    win.setBackground(color_rgb(255,255,255))
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({},{})" .format(self.x,self.y)
class Rectangle: #Creating the class rectangle
    def __init__(self,posn,w,h):
        self.corner = posn
        self.width = w
        self.height = h
    def __str__(self):
        return "({0},{1},{2})" .format(self.corner,self.width,self.height)
    def create_rectangle(x,y,width,height):
        posn = Point(x,y)
        rect = Rectangle(posn,width,height)
        return rect
#to str_rectangle
    def str_rectangle(rect):
        return rect.__str__(self.corner.x,self.corner.y,self.width,self.height)
# to shift rectangle
    def shift_rectangle(rect,dx,dy):
        rect.move(dx,dy)
# off_set rectangle
    def offset_rectangle(rect,dx,dy):
        x = coordinates.next(self.corner,dx)
        y = coordinates.next(self.corner,dy) 
        return(create_rectangle(x,y,w,h))
#Testing code with given functions
        r1 = create_rectangle(10,20,30,40)
        print(str_rectangle(r1))
        r1.setFill('red')

        shift_rectangle(r1,-10,-20).setFill('blue')
        print(str_rectangle(r1))

        print(str_rectangle(r1)).setFill('green')

        r2 = offset_rectangle(r1,100,100)
        print(str_rectangle(r2)).setFill('yellow')

        win.getMouse()
        win.close()
main()
