import pygame, sys, random, math, time
from pygame.locals import *

pygame.init()
vec = pygame.math.Vector2

SCALE = 10
WIDTH = 80
HEIGHT = 80
FPS = 12
FramesPerSecond = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH*SCALE, HEIGHT*SCALE))
pygame.display.set_caption('Evolution game')

class CellBase(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__()
        self.surf = pygame.Surface((SCALE, SCALE))
        self.surf.fill((221, 174, 126))
        self.rect = self.surf.get_rect(center = (posx, posy))

        self.pos = vec((posx, posy))

    def move(self, shifter, RL):
        if RL == 0:
            self.pos.y += shifter
        else:
            self.pos.x += shifter
        
        self.rect = self.surf.get_rect(center = (self.pos.x, self.pos.y))

        if self.pos.x > WIDTH*SCALE:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH*SCALE
        if self.pos.y > HEIGHT*SCALE:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = HEIGHT*SCALE

    def update(self):
        pass


class CellEat(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__()
        self.surf = pygame.Surface((SCALE, SCALE))
        self.surf.fill((116, 109, 117))
        self.rect = self.surf.get_rect(center = (posx, posy))

        self.health = 50
        self.pos = vec((posx, posy))


    def move(self, shifter, RL):
        self.health -= 0.1
        if self.health == 0:
            print('the guy should be dead')
        if RL == 0:
            self.pos.y += shifter
        else:
            self.pos.x += shifter
        
        self.rect = self.surf.get_rect(center = (self.pos.x, self.pos.y))

        if self.pos.x > WIDTH*SCALE:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH*SCALE
        if self.pos.y > HEIGHT*SCALE:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = HEIGHT*SCALE

    def update(self):
        eatFood = pygame.sprite.spritecollide(self, all_food, True)

        if eatFood:
            self.health += 10


class Food(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__()
        self.surf = pygame.Surface((SCALE, SCALE))
        self.surf.fill((138, 205, 234))
        self.rect = self.surf.get_rect(center = (posx, posy))

        self.pos = vec((posx, posy))

    def move(self, shifter, RL):
        pass

    def update(self):
        eaten = pygame.sprite.spritecollide(self, mouth, False)


def makeCreature():
    posx = random.randint(0, WIDTH*SCALE)
    posy = random.randint(0, HEIGHT*SCALE)
    mouths = random.randint(0, 9)
    print(mouths)
    makeCreature.creature = []
    base = CellBase(posx, posy)
    makeCreature.creature.append(base)
    for i in range(0, mouths):
        pos = vec((random.randint(0,3), random.randint(0,3)))
        
        

makeCreature()
T1 = makeCreature.creature

C1 = CellBase(400, 400)
C3 = CellEat(400, 410)
F1 = Food(random.randint(0, WIDTH*SCALE), random.randint(0, HEIGHT*SCALE))

all_sprites = pygame.sprite.Group()
all_sprites.add(C1)
all_sprites.add(F1)
all_sprites.add(C3)
all_sprites.add(T1)

all_food = pygame.sprite.Group()
all_food.add(F1)

mouth = pygame.sprite.Group()
mouth.add(C3)

for i in range(0, 20):
    food = Food(random.randint(0, WIDTH*SCALE), random.randint(0, HEIGHT*SCALE))
    all_sprites.add(food)
    all_food.add(food)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    screen.fill((0,0,0))

    shift = random.randint(-5, 5)
    binary = random.randint(0, 1)

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
        entity.update()
        entity.move(shift, binary)
        

    pygame.display.update()
    FramesPerSecond.tick(FPS)