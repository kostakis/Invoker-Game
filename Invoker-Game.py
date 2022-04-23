from tkinter import N
import pygame
import random

width = 300
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
abilities = {'sunstrike' : sunstrike, 'tornado' : tornado, 'icewall' : icewall, 'ghostwalk' : ghostwalk, 'forgespirit' : forgespirit, 'emp' : emp, 'deafenningblast' : deafenningblast, 'coldsnap' : coldsnap, 'chaosmeteor' : chaosmeteor, 'alacrity' : alacrity}

quas = pygame.image.load('./assets/quas.png')
wex = pygame.image.load('./assets/wex.png')
exort = pygame.image.load('./assets/exort.png')

pygame.mixer.music.load('./assets/music.mp3')
pygame.mixer.music.play()
invoke = pygame.mixer.Sound('./assets/invoke.ogg')

icons = dict()
spheres = list()
spheresVisual = list()
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
                                spheresVisual.append(quas)
                        if event.key == pygame.K_w:
                                spheres.append('wex')
                                spheresVisual.append(wex)
                        if event.key == pygame.K_e:
                                spheres.append('exort')
                                spheresVisual.append(exort)
                        if len(spheresVisual) > 3:
                                spheres.pop(0)
                                spheresVisual.pop(0)
                        if event.key == pygame.K_r:
                                res = None
                                spheres.sort()
                                if ['exort', 'quas', 'wex'] == spheres:
                                        res = 'deafenningblast'
                                if ['exort', 'wex', 'wex'] == spheres:
                                        res = 'alacrity'
                                if ['exort', 'exort', 'wex'] == spheres:
                                        res = 'chaosmeteor'
                                if ['quas', 'quas', 'quas'] == spheres:
                                        res = 'coldsnap'
                                if ['wex', 'wex', 'wex'] == spheres:
                                        res = 'emp'
                                if ['exort', 'exort', 'quas'] == spheres:
                                        res = 'forgespirit'
                                if ['quas', 'quas', 'wex'] == spheres:
                                        res = 'ghostwalk'
                                if ['exort', 'quas', 'quas'] == spheres:
                                        res = 'icewall'
                                if ['exort', 'exort', 'exort'] == spheres:
                                        res = 'sunstrike'
                                if ['quas', 'wex', 'wex'] == spheres:
                                        res = 'tornado'
                                if icons.get(res) != None:
                                        icons.__delitem__(res)
                                        invoke.play()

        screen.fill((50, 50, 50))
        screen.blit(bg, (0, 0))

        if ticks == 0:
                ticks = 300
                speed += 1

        pops = list()
        for i in icons:
                icons[i][1].blit()
                icons[i][1].move()
                if icons[i][1].rect.y > 300:
                        pops.append(i)
        for i in pops:
                icons.pop(i)
        pops.clear()

        if len(icons) < 3:
                a = random.choices(list(abilities.keys()), k=3)
                if len(icons) > 0:
                        if 1 not in list(icons.values())[0]:
                                icons[a[0]] = [1, Icon(abilities[a[0]], 0, 0)]
                        if 2 not in list(icons.values())[0]:
                                icons[a[1]] = [2, Icon(abilities[a[1]], 100, 0)]
                        if 3 not in list(icons.values())[0]:
                                icons[a[2]] = [3, Icon(abilities[a[2]], 200, 0)]
                else:
                        icons[a[0]] = [1, Icon(abilities[a[0]], 0, 0)]
                        icons[a[1]] = [2, Icon(abilities[a[1]], 100, 0)]
                        icons[a[2]] = [3, Icon(abilities[a[2]], 200, 0)]
                
        coords = 0
        for i in spheresVisual:
                screen.blit(i, (coords, 400))
                coords += 100

        pygame.display.update()
        ticks -= 1