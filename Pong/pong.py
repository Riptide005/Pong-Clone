import pygame
import math
import random

#initialize pygame
pygame.init()

#setting up the screen
window = pygame.display.set_mode((800,600))
pygame.display.set_caption("Testing Pygame")
font_normal = pygame.font.SysFont("Arial", size = 12)
font_large = pygame.font.SysFont("Arial", size = 36)
rect_y1 = 270
rect_y2 = 270
ball_x = 400
ball_y = 300
ball_speed_x = 5 * random.choice([1, -1])
ball_speed_y = 5 * random.choice([1, -1])
score1 = 0
score2 = 0
game_state = "MENU"

clock = pygame.time.Clock()

#Running LOOP
running = True
while(running):
    window.fill((255,255,255))
    
    if game_state == "MENU":
        
        menutext1 = font_large.render("PONG", True, (0,255,255))
        menutext2 = font_large.render("Press Space to Start", True, (0,255,255))
        window.blit(menutext1, (350,250))
        window.blit(menutext2, (260,282))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_state = "INITIALIZE"
    
    elif game_state == "INITIALIZE":
        pygame.draw.rect(window, (0,0,0),[20, rect_y1, 10, 60], 0)
        pygame.draw.rect(window, (0,0,0),[770, rect_y2, 10, 60], 0)
        pygame.draw.circle(window, (255,0,0),[ball_x, ball_y], 10, 0)
        score1_display = font_normal.render(f"Player 1 = {score1}", True, (0,0,255))
        score2_display = font_normal.render(f"Player 2 = {score2}", True, (0,255,0))
        window.blit(score1_display, (100, 10))
        window.blit(score2_display, (600, 10))
        
        paddle1_box = pygame.Rect(20, rect_y1, 10, 60)
        paddle2_box = pygame.Rect(770, rect_y2, 10, 60)
        ball_box = pygame.Rect(ball_x - 10, ball_y - 10, 20, 20)
        pygame.display.update()
        pygame.time.delay(1000)
        game_state = "PLAYING"
            
    elif game_state == "PLAYING":       
        pygame.draw.rect(window, (0,0,0),[20, rect_y1, 10, 60], 0)
        pygame.draw.rect(window, (0,0,0),[770, rect_y2, 10, 60], 0)
        pygame.draw.circle(window, (255,0,0),[ball_x, ball_y], 10, 0)
        score1_display = font_normal.render(f"Player 1 = {score1}", True, (0,0,255))
        score2_display = font_normal.render(f"Player 2 = {score2}", True, (0,255,0))
        window.blit(score1_display, (100, 10))
        window.blit(score2_display, (600, 10))
        
        paddle1_box = pygame.Rect(20, rect_y1, 10, 60)
        paddle2_box = pygame.Rect(770, rect_y2, 10, 60)
        ball_box = pygame.Rect(ball_x - 10, ball_y - 10, 20, 20)
        keys = pygame.key.get_pressed()
        ball_x += ball_speed_x
        ball_y += ball_speed_y
        if keys[pygame.K_w]:
            rect_y1 -= 10
        if keys[pygame.K_s]:
            rect_y1 += 10
        if keys[pygame.K_i]:
            rect_y2 -= 10
        if keys[pygame.K_k]:
            rect_y2 += 10    
            
        # To fast forward the game to end screen.   
        # if keys[pygame.K_g]:
        #   score1 = 5
        # if keys[pygame.K_v]:
        #   score2 = 5
        
        if ball_box.colliderect(paddle1_box) and ball_speed_x < 0:
            ball_speed_x *= -1
        if ball_box.colliderect(paddle2_box) and ball_speed_x > 0:
            ball_speed_x *= -1
        
        if ball_x < 25 :
            window.fill((255,255,255))
            pygame.draw.rect(window, (0,0,0),[20, 270, 10, 60], 0)
            pygame.draw.rect(window, (0,0,0),[770, 270, 10, 60], 0)
            pygame.draw.circle(window, (255,0,0),[400, 300], 10, 0)
            pygame.display.update()
            ball_x = 400
            ball_y = 300
            rect_y1 = 270
            rect_y2 = 270
            score2 += 1
            pygame.time.delay(1000)
            ball_speed_x = 5
        
        if ball_x > 780 :
            window.fill((255,255,255))
            pygame.draw.rect(window, (0,0,0),[20, 270, 10, 60], 0)
            pygame.draw.rect(window, (0,0,0),[770, 270, 10, 60], 0)
            pygame.draw.circle(window, (255,0,0),[400, 300], 10, 0)
            pygame.display.update()
            ball_x = 400
            ball_y = 300
            rect_y1 = 270
            rect_y2 = 270
            score1 += 1
            pygame.time.delay(1000)
            ball_speed_x = -5

        if ball_y < 5 or ball_y > 595:
            ball_speed_y *= -1
        if rect_y1 < 0:
            rect_y1 = 0
        if rect_y1 > 540:
            rect_y1 = 540  
        if rect_y2 < 0:
            rect_y2 = 0
        if rect_y2 > 540:
            rect_y2 = 540 
        
        if score1 == 5:
            window.fill((255,255,255))
            pygame.draw.rect(window, (0,0,0),[20, 270, 10, 60], 0)
            pygame.draw.rect(window, (0,0,0),[770, 270, 10, 60], 0)
            pygame.draw.circle(window, (255,0,0),[400, 300], 10, 0)
            ball_x = 400
            ball_y = 300
            rect_y1 = 270
            rect_y2 = 270
            victory = font_large.render("PLAYER 1 WINS!!", True, (255,0,255))
            window.blit(victory, (280, 200))
            pygame.display.update()
            pygame.time.delay(5000)
            score1 = 0
            score2 = 0
            game_state = "MENU"

        if score2 == 5:
            window.fill((255,255,255))
            pygame.draw.rect(window, (0,0,0),[20, 270, 10, 60], 0)
            pygame.draw.rect(window, (0,0,0),[770, 270, 10, 60], 0)
            pygame.draw.circle(window, (255,0,0),[400, 300], 10, 0)
            ball_x = 400
            ball_y = 300
            rect_y1 = 270
            rect_y2 = 270
            victory = font_large.render("PLAYER 2 WINS!!", True, (255,0,255))
            window.blit(victory, (280, 200))
            pygame.display.update()
            pygame.time.delay(5000)
            score1 = 0
            score2 = 0
            game_state = "MENU"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(60)
#Quit once the loop has ended
pygame.quit()