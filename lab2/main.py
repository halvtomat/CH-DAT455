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

def graphicFinishShot(game, proj):
    # The current player
    player = game.getCurrentPlayer()
    # The player opposing the current player
    other = game.getOtherPlayer()

    # Check if we won
    distance = other.projectileDistance(proj) 
    if distance == 0.0:
        player.increaseScore()
        game.newRound()
    # Switch active player
    game.nextPlayer()

def graphicPlay():
    game = Game(10, 3)
    graphics = GameGraphics(game)
    inputDialog = InputDialog(45, 40, game.getCurrentWind())
    while True:
        _input = inputDialog.interact()
        if(_input == "Quit"):
            inputDialog.close()
            graphics.close()
        elif(_input == "Fire!"):
            angle, vel = inputDialog.getValues()
            proj = graphicFire(game, graphics, angle, vel)
            graphicFinishShot(game, proj)
            

# Run the game with graphical interface
graphicPlay()
