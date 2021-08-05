# A simple testing procedure for the game model

import graphics
import gamemodel
import gamegraphics

def runTests(game):

    players = game.getPlayers()

    assert len(players) == 2, "there should be two players"

    # Testing game initialization
    assert players[0].getColor()=="blue", "player 0 should be blue!"
    assert players[1].getColor()=="red", "player 1 should be red!"

    assert players[0].getX()== -90, "player 0 should stand at x=-90!"
    assert players[1].getX()== 90, "player 1 should stand at x=90!"

    assert players[0].getColor()=="blue"
    assert players[1].getColor()=="red"
    
    assert game.getCurrentPlayerNumber()==0, "player 0 should start!"
    
    assert game.getCurrentPlayer() == players[0], "player 0 should start! (2)"
    assert game.getOtherPlayer()==players[1], "getOtherPlayer() doesn't work"
    assert -10 <= game.getCurrentWind() <= 10, "wind should be a random value in [-10,10]"

    # Testing manually swapping player
    game.nextPlayer()
    assert game.getCurrentPlayerNumber()==1, "player 1 should go second!"
    assert game.getCurrentPlayer() == players[1]
    assert game.getOtherPlayer()==players[0], "getOtherPlayer() doesn't work"

    # Switch back to player 0
    game.nextPlayer()
    assert game.getCurrentPlayer() == players[0], "player 0 should go after player 1!"
    assert game.getOtherPlayer()==players[1], "getOtherPlayer() doesn't work"

    # Turn off wind
    game.setCurrentWind(0)
    assert game.getCurrentWind() == 0, "wind should be 0"


    #Testing "Manual fire" for player 0
    proj = game.getCurrentPlayer().fire(30,31)
    assert (proj.getX() == game.getCurrentPlayer().getX()), "Fired projectile should start at player X-position"
    assert (proj.getY() == 10/2), "Fired projectile Y-position should start half the cannon size"
    assert (proj.isMoving()), "projectile should be moving"

    assert game.getCurrentPlayer().getAim() == (30,31), "After firing, getAim() should give the latest (angle,velocity)-values"

    proj.update(1.0)
    assert (abs(proj.getX() + 63.1532124826824) < 0.01), "Projectile X-Position is {0:f}, should be -63.153212".format(proj.getX())
    assert (abs(proj.getY() - 15.6) < 0.01), "Projectile X-Position is {0:f}, should be 15.6".format(proj.getY())
    assert (proj.isMoving()), "projectile should be moving"

    ticks = 0
    while proj.isMoving():
        proj.update(0.1)
        ticks += 1
        assert ticks <= 25, "projectile should have stopped now..."
    assert ticks == 25, "Incorrect tick-count"

    assert proj.getY()==0.0, "projectile should stop at y=0"
    assert abs(proj.getX() - 3.9637563106115907) < 0.01, "Projectile X-Position is {0:f}, should be -3.9637563106115907".format(proj.getX())

    assert abs(players[1].projectileDistance(proj) - -78.03624368938841) < 0.01, "Projectile X-distance to player is {0:f}, should be -78.03624368938841".format(players[1].projectileDistance(proj))
    assert abs(players[0].projectileDistance(proj) - 85.96375631061159) < 0.01, "Projectile X-distance to player is {0:f}, should be 85.96375631061159".format(players[0].projectileDistance(proj))

    #Switching to player 1
    game.nextPlayer()
    assert game.getCurrentPlayerNumber()==1, "player 1 should go after player 0"
    assert game.getCurrentPlayer() == players[1], "player 1 should go after player 0"
    assert game.getOtherPlayer()==players[0], "getOtherPlayer() doesn't work"


    #Testing "Manual fire" for player 1
    proj = game.getCurrentPlayer().fire(45,41)
    assert(proj.getX() == game.getCurrentPlayer().getX()), "Fired projectile should start at player X-position"
    assert(proj.getY() == 10/2), "Fired projectile Y-position should start half the cannon size"
    assert(proj.isMoving()), "projectile should be moving"

    ticks = 0
    while proj.isMoving():
        proj.update(0.1)
        ticks += 1
        assert ticks <= 61, "projectile should have stopped now..."
    assert ticks == 61, "Incorrect tick-count"
    assert proj.getY()==0.0, "projectile should always stop at y=0"
    assert abs(proj.getX() - -86.84740597475547) < 0.01, "Projectile X-Position is {0:f}, should be -86.84740597475547".format(proj.getX())
    assert abs(players[1].projectileDistance(proj) - -168.84740597475547) < 0.01, "Projectile X-distance to player is {0:f}, should be 168.84740597475547".format(players[1].projectileDistance(proj))
    assert players[0].projectileDistance(proj) == 0, "Projectile X-distance to player is {0:f}, should be 0".format(players[0].projectileDistance(proj))

    # Test scoring
    assert players[0].getScore()==0, "Initial score should be 0"
    players[0].increaseScore()
    assert players[1].getScore()==0, "Score should be 0"
    assert players[0].getScore()==1, "Score should be 1"

    # Test new round
    game.setCurrentWind(1000)
    assert game.getCurrentWind()==1000, "Failed to set wind speed"
    game.newRound()
    assert game.getCurrentWind()!=1000, "Wind should be randomized each round"

    # Test firing with wind
    game.setCurrentWind(-1)
    proj = players[0].fire(45,41)
    assert(proj.getX() == players[0].getX()), "Fired projectile should start at player X-position"
    assert(proj.getY() == 10/2), "Fired projectile Y-position should start half the cannon size"
    assert(proj.isMoving()), "projectile should be moving"

    ticks = 0
    while proj.isMoving():
        proj.update(0.1)
        ticks += 1
        assert ticks <= 61, "projectile should have stopped now..."
        
    assert ticks == 61, "Incorrect tick-count"
    assert abs(proj.getX() - 68.2424059747553) < 0.01, "Projectile X-Position is {0:f}, should be 68.2424059747553".format(proj.getX())
    
    
    # A few additional hints
    gameAtts = len(game.__dict__.items())
    if (gameAtts > 5):
        print("Your Game object has {} attributes. This isn't necessarily wrong, but 5 seems like a nice number.".format(gameAtts))
        print("Make sure you are not representing the same information in multiple attributes.")
    playerAtts = len(game.getCurrentPlayer().__dict__.items())
    if (playerAtts > 8):
        print("Your Player object has {} attributes. This isn't necessarily wrong, but it seems a bit high.".format(playerAtts))



def testGraphics():
    game = gamemodel.Game(10,3)

    ggame = gamegraphics.GameGraphics(game)
    
    # For these tests to work, you need to have a getWindow-method in GraphicGame
    w = ggame.getWindow()

    if ggame.getWindow() is None:
        print("No game window yet, aborting graphics tests")
        return
    
    circ_type = type(graphics.Circle(graphics.Point(0,0), 10))
    rect_type = type(graphics.Rectangle(graphics.Point(0,0), graphics.Point(1,1)))

    if len(w.items) != 5:
        print("WARNING: your graphics does not start with five graphical components. This is likely an error. {0}".format(len(w.items)))
        print(w.items)

    # Run the standard tests for the model, then sync graphics
    runTests(game)
    ggame.sync()

    if len(w.items) != 7:
        print("WARNING: your graphics does not have seven graphical components after syncing. This is likely an error.")
    

    everything = w.items
    circles = [x for x in w.items if type(x) == circ_type]
    rectangles = [x for x in w.items if type(x) == rect_type]

    assert len(rectangles) == 2, "there should be two rectangles in the graphics"
    assert len(circles) == 2, "there should be two circles drawn after running tests"

    rect_pos = [x.getCenter().getX() for x in rectangles]
    assert -90 in rect_pos and 90 in rect_pos, "rectangles should be at x=-90 and x=90"

    # Fire a red projectile and move it a bit
    game.setCurrentWind(0)
    game.getCurrentPlayer().fire(30, 30).update(2)

    ggame.sync()

    circles = [x for x in w.items if type(x) == circ_type]
    assert len(circles) <= 2, "there should never be more than two circles! You need to undraw old cannonballs"


runTests(gamemodel.Game(10,3))

testGraphics()

# If your graphical window or close immediately after running test, try uncommenting this
#wait = input("Press Enter to terminate.")
