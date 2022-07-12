import pygame
from sys import exit


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_score
    score_surface = test_font.render(f"SCORE : {current_time}", False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(100, 50))
    screen.blit(score_surface, score_rect)
    return current_time


pygame.init()
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption('ROBO RUNNER')
Clock = pygame.time.Clock()
test_font = pygame.font.SysFont('Verdana', 35)

game_active = True
start_score = 0
score = 0

sky_surface = pygame.image.load('img/sky.png').convert()
land_surface = pygame.image.load('img/land.jpg').convert()
text_surface = test_font.render('ROBO-RUN', False, 'BLUE')

snail = pygame.image.load('img/snail.png').convert_alpha()
snail_rect = snail.get_rect(bottomright=(800, 410))

robo = pygame.image.load('img/robot.png').convert_alpha()
robo_rect = robo.get_rect(midbottom=(100, 420))

robo_grav = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and robo_rect.bottom == 420:
                    robo_grav = -24
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_active = True
                snail_rect.left = 800
                start_score = int(pygame.time.get_ticks() / 1000)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER:
                game_active = True
                snail_rect.left = 800
                start_score = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(land_surface, (0, 405))
        screen.blit(land_surface, (350, 405))
        screen.blit(text_surface, (460, 20))
        snail_rect.x -= 6
        if snail_rect.right <= 0: snail_rect.left = 800
        screen.blit(snail, snail_rect)
        screen.blit(robo, robo_rect)

        score = display_score()
        robo_grav += 1
        robo_rect.y += robo_grav
        if robo_rect.bottom >= 420:
            robo_rect.bottom = 420
        if snail_rect.colliderect(robo_rect):
            game_active = False
    else:
        screen.fill('#28bfc9')
        text_surface2 = test_font.render('GAME OVER', False, '#dce362')
        text_surface3 = test_font.render("press 'ENTER' to restart", False, '#f0f3fa')
        robo2 = pygame.image.load('img/robot2.png').convert_alpha()
        score_text = test_font.render(f'Your score is : {score}', False, '#0a43ff')
        score_text_rect = score_text.get_rect(center=(350, 140))
        screen.blit(text_surface2, (245, 35))
        screen.blit(score_text, score_text_rect)
        screen.blit(robo2, (270, 230))
        screen.blit(text_surface3, (150, 400))

    pygame.display.update()
    Clock.tick(80)
