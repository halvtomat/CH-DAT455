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
    game = gamemodel.Game(10, 3)
    graphics = gamegraphics.GameGraphics(game)
    inputDialog = gamegraphics.InputDialog(45, 40)
    while True:
        _input = inputDialog.interact()
        if(_input == "Quit"):
            inputDialog.close()
            graphics.close()
        elif(_input == "Fire!"):
            angle, vel = inputDialog.getValues()
            proj = graphicFire(game, graphics, angle, vel)
            

# Run the game with graphical interface
graphicPlay()
