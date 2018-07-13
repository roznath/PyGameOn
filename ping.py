‘’’
  @title: PyGameOn
  @author: RozNath
  @dev: Top down Pokemon style game
‘’’

import pygame


class Face(object):
    def __init__(self):
        self.face = pygame.image.load('face.png')
        self.x = 9
        self.y = 9
        self.orientation = "S"
        self.facerot = pygame.transform.rotate(self.face, 0)

    def controls(self):
        key = pygame.key.get_pressed()
        distance = 50
        if key[pygame.K_UP]:
            if self.orientation == "N":
                if self.y > 9:
                    self.y -= distance
            else:
                self.orientation = "N"
                self.facerot = pygame.transform.rotate(self.face, 180)
            pygame.time.delay(300)

        elif key[pygame.K_DOWN]:
            if self.orientation == "S":
                if self.y < 959:
                    self.y += distance
            else:
                self.orientation = "S"
                self.facerot = pygame.transform.rotate(self.face, 0)
            pygame.time.delay(300)

        if key[pygame.K_LEFT]:
            if self.orientation == "W":
                if self.x > 9:
                    self.x -= distance
            else:
                self.orientation = "W"
                self.facerot = pygame.transform.rotate(self.face, 270)
            pygame.time.delay(300)

        elif key[pygame.K_RIGHT]:
            if self.orientation == "E":
                if self.x < 959:
                    self.x += distance
            else:
                self.orientation = "E"
                self.facerot = pygame.transform.rotate(self.face, 90)
            pygame.time.delay(300)

    def draw(self, gameDisplay):
        gameDisplay.blit(self.facerot, (self.x, self.y))


pygame.init()
bg = pygame.image.load('grid.jpg')

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()

face = Face()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()

    face.controls()

    gameDisplay.blit(bg, (0, 0))
    face.draw(gameDisplay)
    pygame.display.update()


