# Imports everything from both model and graphics
from gamemodel import *
from gamegraphics import *


# Here is a nice little method you get for free
# It fires a shot for the current player and animates it until it stops
def graphicFire(game, graphics, angle, vel):
    player = game.getCurrentPlayer()
    # create a shot and track until it hits ground or leaves window
    proj = player.fire(angle, vel)
    while proj.isMoving():
        proj.update(1/50)
        graphics.sync() # This deals with all graphics-related issues
        update(50) # Waits for a short amount of time before the next iteration
    return proj

def graphicPlay():
    # TODO: This is where you implement the game loop
    # HINT: Creating a Game and a GraphicGame is a good start. 
    # HINT: You can look at the text interface for some inspiration
    # Note that this code should not directly work with any drawing or such 
    #   all that is done by the methods in the classes.
    pass

# Run the game with graphical interface
graphicPlay()
