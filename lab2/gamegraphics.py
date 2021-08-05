#------------------------------------------------------
#This module contains all graphics-classes for the cannon game.
#The two primary classes have these responsibilities:
#  * GameGraphics is responsible for the main window
#  * Each PlayerGraphics is responsible for the graphics of a 
#    single player (score, cannon, projectile)
#In addition there are two UI-classes that have no 
#counterparts in the model:
#  * Button
#  * InputDialog
#------------------------------------------------------

# This is the only place where graphics should be imported!
from graphics import *

class GameGraphics:
    def __init__(self, game):
        self.game = game
        self.window = win = GraphWin("Cannon game", 640, 480, autoflush=False)
        win.setCoords(-110, -10, 110, 155)
        cannonSize = game.getCannonSize()
        ballSize = game.getBallSize()
        self.players = [
            PlayerGraphics(game.players[0], cannonSize, ballSize, win),
            PlayerGraphics(game.players[1], cannonSize, ballSize, win)]

    def sync(self):
        for player in self.players:
            player.sync()
    
    def getWindow(self):
        return self.window
# TODO: The class only needs two methods, sync() and getWindow(). 
# HINT: The constructor needs to create a window, a couple of graphic components and two 
#       PlayerGraphics-objects that in turn create additional components
# HINT: sync() needs to call sync() for the two PlayerGraphics-objects
# HINT: These lines are good for creating a window:
#       win = GraphWin("Cannon game" , 640, 480, autoflush=False)
#       win.setCoords(-110, -10, 110, 155)
# HINT: Don't forget to call draw() on every component you create, otherwise they will not be visible

class PlayerGraphics:
    def __init__(self, player, cannonSize, ballSize, window):
        self.player = player
        self.cannonSize = cannonSize
        self.ballSize = ballSize
        self.window = window
        self.sync()

    def sync(self):
        text = Text(Point(self.player.getX(), -5), self.player.getScore())
        rect = Rectangle(
            Point(self.player.getX() - self.cannonSize/2, 0),
            Point(self.player.getX() + self.cannonSize/2, self.cannonSize))
        text.draw(self.window)
        rect.draw(self.window)


# TODO: There needs to be a class called PlayerGraphics here.
# TODO: It needs only a constructor and a sync()-method
# HINT: Each PlayerGraphics should contain one Player object. 
# HINT: Should draw a cannon and a scoreboard immediately 
#       (the Player object knows its position)
# HINT: Typically doesn't draw a projectile when created, but creates one at some point
#       when sync() is called.
# HINT: sync() needs to update the score text and draw/update a circle for the projectile if there is one. 

""" A somewhat specific input dialog class (adapted from the book) """
class InputDialog:
    """ Creates an input dialog with initial values for angle and velocity and displaying windGraphicsObject() """
    def __init__ (self, angle, vel, wind):
        self.win = win = GraphWin("Fire", 200, 300)
        win.setCoords(0,4.5,4,.5)
        Text(Point(1,1), "Angle").draw(win)
        self.angle = Entry(Point(3,1), 5).draw(win)
        self.angle.setText(str(angle))
        
        Text(Point(1,2), "Velocity").draw(win)
        self.vel = Entry(Point(3,2), 5).draw(win)
        self.vel.setText(str(vel))
        
        Text(Point(1,3), "Wind").draw(win)
        self.height = Text(Point(3,3), 5).draw(win)
        self.height.setText("{0:.2f}".format(wind))
        
        self.fire = Button(win, Point(1,4), 1.25, .5, "Fire!")
        self.fire.activate()
        self.quit = Button(win, Point(3,4), 1.25, .5, "Quit")
        self.quit.activate()

    """ Waits for the player to enter values and click a button """
    def interact(self):
        while True:
            pt = self.win.getMouse()
            if self.quit.clicked(pt):
                return "Quit"
            if self.fire.clicked(pt):
                return "Fire!"

    """ Gets the values entered into this window, typically called after interact """
    def getValues(self):
        a = float(self.angle.getText())
        v = float(self.vel.getText())
        return a,v

    """ Closes the input window """
    def close(self):
        self.win.close()



""" A general button class (from the book) """
class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, Point(30,25), 20, 10, 'Quit') """ 

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "RETURNS true if button active and p is inside"
        return self.active and \
               self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax

    def getLabel(self):
        "RETURNS the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = 1

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = 0