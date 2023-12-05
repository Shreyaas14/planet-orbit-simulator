import pygame
import math
pygame.init() #initializes a game

#width & height variables
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("SOLAR SYSTEM SIMULATION")

#colors
BLACK = (0, 0, 0)
ORANGE = (244, 128, 55)
BLUE = hex('4f42b5')

class Planet:
    #defines an astronomical unit
    AU = 149.636 * 1000
    #gravity
    G = 6.67428e-11
    #scale
    SCALE = 250 / AU #1 AU = 100 pixels
    TIMESTEP = 3600 * 24 #1 day

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.x_velocity = 0
        self.y_velocity = 0

        #special to tell us if the planet is the sun --> if sun, no orbit needed
        self.sun = False
        self.distance_to_sun = 0
        self.orbit = []
    
    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        pygame.draw.circle(win, self.color, (x, y), self.radius)




#ensures that the "game" is always running
def main():
    running = True

    #initalizing a Sun
    sun = Planet(0, 0, 30, ORANGE, 1.9982 * 10 ** 30)
    sun.sun = True

    planets = [sun]

    earth = Planet(-1 * Planet.AU, 0, BLUE, 5.59742 * 10 ** 24)
    


    timer = pygame.time.Clock()

    while running:
        #runs simulation at computer speed
        timer.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #stops game if we X out of it
                run = False

        for planet in planets:
            planet.draw(WIN)
            
        pygame.display.update()

    pygame.quit()

main()

