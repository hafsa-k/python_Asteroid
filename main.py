from if3_game.engine import init, Game , Layer
from game_objects import RESOLUTION, Spaceship, Asteroid


init(RESOLUTION, "Asteroid")



game = Game()

game_layer = Layer()  
spaceship = Spaceship( (400,300) )
#can be write like this 
#spaceship = Spaceship( position=(400,300) )   
asteroid = Asteroid((200,200), (-150,30)) 

game_layer.add(spaceship)
game_layer.add(asteroid)
game.add(game_layer)

#Last Line
game.run()