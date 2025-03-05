"""
Crear el joc d’arkanoid utilitzant la llibreria pygame.
Enllaç a les imatges que heu de posar al mateix directori que el fitxer.
Canviar la ruta absoluta de les imatges /home/cicles/AO/Tasca11/Nom.png
Es comença pitjant la barra d’espai i es juga pitjant les fletxes esquerra i dreta.
"""
import pygame
import sys

# Iniciar Pygame
pygame.init()

# Dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Arkanoid')

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Cargar imágenes
background = pygame.image.load('background.png')
paddle = pygame.image.load('paddle.png')
ball = pygame.image.load('ball.png')

# Posiciones iniciales
paddle_rect = paddle.get_rect(midbottom=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30))
ball_rect = ball.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
ball_speed = [5, -5]

# Bucle del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Comenzar el juego con la barra espaciadora
                pass

    # Mover la pala con las flechas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_rect.left > 0:
        paddle_rect.move_ip(-10, 0)
    if keys[pygame.K_RIGHT] and paddle_rect.right < SCREEN_WIDTH:
        paddle_rect.move_ip(10, 0)

    # Mover la bola
    ball_rect.move_ip(ball_speed)
    if ball_rect.left <= 0 or ball_rect.right >= SCREEN_WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball_rect.top <= 0 or ball_rect.bottom >= SCREEN_HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Dibujar elementos en la pantalla
    screen.fill(BLACK)
    screen.blit(background, (0, 0))
    screen.blit(paddle, paddle_rect)
    screen.blit(ball, ball_rect)
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.Clock().tick(60)