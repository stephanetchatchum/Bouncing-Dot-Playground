import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

ball_x = SCREEN_WIDTH//2
ball_y = SCREEN_HEIGHT//2

ball_rad = 25
ball_speed = 5

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bouncing dot playground")

clock = pygame.time.Clock()

run = True

while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((255,255,255))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball_x -= ball_speed
    if keys[pygame.K_RIGHT]:
        ball_x += ball_speed
    if keys[pygame.K_UP]:
        ball_y -= ball_speed
    if keys[pygame.K_DOWN]:
        ball_y += ball_speed

    pygame.draw.circle(screen, (0,0,255), (ball_x, ball_y), ball_rad)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()