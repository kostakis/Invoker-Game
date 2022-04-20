import pygame

width = 500
height = 500
fps = 60

pygame.init()
global screen
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

class Icon(Sprite):
        def __init__(self, image, x, y, speed):
                self.image = pygame.image.load(image)
                self.rect = image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.speed = speed

        def blit(self):
                screen.blit(self.image, (self.rect.x, self.rect.y))

        def move(self):
                self.rect.y += speed

icons = list()
ticks = 60
while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        quit()

        

        pygame.display.update()
