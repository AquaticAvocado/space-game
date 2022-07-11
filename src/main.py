import pygame
from ship import Ship
import constants as c

########## MAIN CODE ##########
pygame.init()
display = pygame.display.set_mode(c.SCREEN_SIZE)
clock = pygame.time.Clock()

player = Ship()

sprite_group = pygame.sprite.Group()
sprite_group.add(player)
run = True

laser_sound = pygame.mixer.Sound("sounds/laser_soft.wav")
hit_sound = pygame.mixer.Sound("sounds/hit_sound.wav")

# MAIN LOOP
while run:
    # CLOCK TICK
    clock.tick(c.FPS)
    
    # HANDLE EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                pygame.quit()
            if event.key == pygame.K_SPACE:
                pygame.mixer.Sound.play(laser_sound)
            if event.key == pygame.K_a:
                player.x_vel = -player.speed
            if event.key == pygame.K_d:
                player.x_vel = player.speed
    
    # UPDATE
    sprite_group.update()

    # RENDER
    display.fill(c.BLACK)
    sprite_group.draw(display)
    pygame.display.update()