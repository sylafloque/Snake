import pygame, sys, random
from pygame.locals import *

pygame.init()

# Initialisation des variables
W, H, s, white, black, red, green, blue, orange = 800, 600, 20, (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 165, 0)
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# Fonction pour afficher le texte
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

# Fonction pour afficher le serpent
def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, green, [x, y, s, s])

# Fonction pour lancer le jeu
def gameloop():
    # Initialisation des variables du jeu
    x, y, d, a = W // 2, H // 2, random.choice([0, s, -s]), random.choice([0, s, -s])
    snake_list = [(x, y)]
    food = (random.randrange(0, W, s), random.randrange(0, H, s))
    score = 0
    game_over = False
    while not game_over:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == K_q:
                    if d != s:
                        d, a = -s, 0
                elif event.key == K_RIGHT or event.key == K_d:
                    if d != -s:
                        d, a = s, 0
                elif event.key == K_UP or event.key == K_z:
                    if a != s:
                        d, a = 0, -s
                elif event.key == K_DOWN or event.key == K_s:
                    if a != -s:
                        d, a = 0, s

        # Mise à jour de la position du serpent
        x += d
        y += a
        snake_head = (x, y)
        snake_list.append(snake_head)

        # Si le serpent mange la nourriture
        if snake_head == food:
            food = (random.randrange(0, W, s), random.randrange(0, H, s))
            score += 1
        else:
            snake_list.pop(0)

        # Vérification si le serpent est en collision avec les bords de l'écran
        if x >= W or x < 0 or y >= H or y < 0:
            game_over = True

        # Vérification si le serpent se mord la queue
        if snake_head in snake_list[:-1]:
            game_over = True

        # Affichage des éléments du jeu
        screen.fill(black)
        draw_snake(snake_list)
        pygame.draw.rect(screen, orange, [food[0], food[1], s, s])
        draw_text(f"Score: {score}", pygame.font.SysFont(None, 30), white, screen, 10, 10)
        pygame.display.update()
        
        clock.tick(15)
gameloop()
