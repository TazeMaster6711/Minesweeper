import pygame
import random

pygame.init()

display = pygame.display.set_mode((800, 800))

mouse_x = 0
mouse_y = 0



click = False

tiles_num = []
bombs = []

check_x = 0
check_y = 0
check_rect = pygame.Rect(check_x, check_y, 40, 40)
bombs_near = 0

mouse = pygame.Rect(mouse_x, mouse_y, 5, 5)

#make tiles
tiles = []
tile_x = 0
tile_y = -50
for loop in range(16):
    tile_y += 50
    for i in range(16):
        tile_x = i*50
        tiles.append(pygame.Rect(tile_x, tile_y, 50, 50))

#make bombs
for i in range (30): 
    tile_x = random.randint(0, 15)*50
    tile_y = random.randint(0, 15)*50
    if pygame.Rect(tile_x, tile_y, 50, 50) in bombs:
        while pygame.Rect(tile_x, tile_y, 50, 50) in bombs:
            print("redo")
            tile_x = random.randint(0, 16)*50
            tile_y = random.randint(0, 16)*50
    bombs.append(pygame.Rect(tile_x, tile_y, 50, 50))


print(bombs)

for i in range(256):
    tiles_num.append(i)

times_looped = 0

pygame.display.set_caption("Minesweeper")
while True:
    display.fill((0, 0, 0))

    click = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("click")
                click = True
            if event.button == 3:
                print("flag")
        
    


    mouse = pygame.Rect(mouse_x, mouse_y, 1, 1)
    
    times_looped = 0
    for tile in tiles:
        times_looped += 1
        if tile.colliderect(mouse):
            pygame.draw.rect(display, (100, 100, 100), tile)
            if click:               
                # set the "bombs_near" variable to how many mines are near
                check_x = tile[0] - 50
                check_y = tile[1] - 50
                bombs_near = 0
                for y in range(3):
                    check_x = tile[0] - 50
                    for x in range(3):
                        check_rect = pygame.Rect(check_x + 5, check_y + 5, 40, 40) # update the position
                        for bomb in bombs:
                            if check_rect.colliderect(bomb):
                                bombs_near += 1
                        check_x += 50
                    check_y += 50
                print(bombs_near)
        else:
            pygame.draw.rect(display, (50, 50, 50), tile)

    for bomb in bombs:
        pygame.draw.rect(display, (250, 50, 50), bomb)        
    pygame.display.flip()
    