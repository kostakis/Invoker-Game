import pygame
import random

width = 500
height = 500
fps = 30

pygame.init()
pygame.mixer.init()
global screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('QWE Trainer')
pygame.display.set_icon(pygame.image.load('./assets/icon.ico'))
clock = pygame.time.Clock()
bg = pygame.Surface((300, 400))

class Icon(pygame.sprite.Sprite):
        def __init__(self, image, x, y):
                self.image = image
                self.rect = image.get_rect()
                self.rect.x = x
                self.rect.y = y

        def blit(self):
                screen.blit(self.image, (self.rect.x, self.rect.y))

        def move(self):
                self.rect.y += speed

sunstrike = pygame.image.load('./assets/sunstrike.png')
tornado = pygame.image.load('./assets/tornado.png')
icewall = pygame.image.load('./assets/icewall.png')
ghostwalk = pygame.image.load('./assets/ghostwalk.png')
forgespirit = pygame.image.load('./assets/forgespirit.png')
emp = pygame.image.load('./assets/emp.png')
deafenningblast = pygame.image.load('./assets/deafenningblast.png')
coldsnap = pygame.image.load('./assets/coldsnap.png')
chaosmeteor = pygame.image.load('./assets/chaosmeteor.png')
alacrity = pygame.image.load('./assets/alacrity.png')
abilities = [sunstrike, tornado, icewall, ghostwalk, forgespirit, emp, deafenningblast, coldsnap, chaosmeteor, alacrity]
names = ['sunstrike', 'tornado', 'icewall', 'ghostwalk', 'forgespirit', 'emp', 'deafenningblast', 'coldsnap', 'chaosmeteor', 'alacrity']

quas = pygame.image.load('./assets/quas.png')
wex = pygame.image.load('./assets/wex.png')
exort = pygame.image.load('./assets/exort.png')

pygame.mixer.music.load('./assets/music.mp3')
pygame.mixer.music.play()
invoke = pygame.mixer.Sound('./assets/invoke.ogg')

icons = dict()
spheres = list()
ticks = 300
global speed
speed = 1
while True:
        clock.tick(fps)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        quit()
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                                spheres.append('quas')
                        if event.key == pygame.K_w:
                                spheres.append('wex')
                        if event.key == pygame.K_e:
                                spheres.append('exort')
                        if len(spheres) > 3:
                                spheres.pop(0)
                        if event.key == pygame.K_r:
                                invoke.play()
                                pops = None
                                current = spheres
                                if ['exort', 'quas', 'wex'].sort() == current.sort():
                                        pops = 'deafenningblast'
                                if ['wex', 'wex', 'exort'].sort() == current.sort():
                                        pops = 'alacrity'
                                if ['wex', 'exort', 'exort'].sort() == current.sort():
                                        pops = 'chaosmeteor'
                                if ['quas', 'quas', 'quas'].sort() == current.sort():
                                        pops = 'coldsnap'
                                if ['wex', 'wex', 'wex'].sort() == current.sort():
                                        pops = 'emp'
                                if ['quas', 'exort', 'exort'].sort() == current.sort():
                                        pops = 'forgespirit'
                                if ['quas', 'quas', 'wex'].sort() == current.sort():
                                        pops = 'ghostwalk'
                                if ['quas', 'quas', 'exort'].sort() == current.sort():
                                        pops = 'icewall'
                                if ['exort', 'exort', 'exort'].sort() == current.sort():
                                        pops = 'sunstrike'
                                if ['quas', 'wex', 'wex'].sort() == current.sort():
                                        pops = 'tornado'
                                icons.pop(pops, None)

        screen.fill((50, 50, 50))
        screen.blit(bg, (100, 0))

        if ticks == 0:
                ticks = 300
                speed += 1

        if len(icons) < 3:
                if 1 not in icons.values():
                        icons[random.choice(names)] = [1, Icon(random.choice(abilities), 100, 0)]
                if 2 not in icons.values():
                        icons[random.choice(names)] = [2, Icon(random.choice(abilities), 200, 0)]
                if 3 not in icons.values():
                        icons[random.choice(names)] = [3, Icon(random.choice(abilities), 300, 0)]
        
        coords = 100
        for i in spheres:
                if i == 'quas':
                        screen.blit(quas, (coords, 400))
                        coords += 100
                if i == 'wex':
                        screen.blit(wex, (coords, 400))
                        coords += 100
                if i == 'exort':
                        screen.blit(exort, (coords, 400))
                        coords += 100

        pops = list()
        for i in icons:
                icons[i][1].blit()
                icons[i][1].move()
                if icons[i][1].rect.y > 300:
                        pops.append(i)
        for i in pops:
                icons.pop(i)
        pops.clear()

        pygame.display.update()
        ticks -= 1