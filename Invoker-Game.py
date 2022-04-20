import pygame

width = 1920
height = 1080
fps = 60

pygame.init()
global screen
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

class GameSprite(Sprite):
        def __init__(self, image, x, y):
                self.image = pygame.image.load(image)
                self.rect = image.get_rect()
                self.rect.x = x
                self.rect.y = y

        def blit(self):
                screen.blit(self.image, (self.rect.x, self.rect.y))

class Icon(GameSprite)
        
while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        quit()
        pygame.display.update()
