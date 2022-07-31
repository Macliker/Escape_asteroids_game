from random import randint
import pygame 
import os
import datetime

pygame.init()
pygame.font.init()
pygame.mixer.init()

WIN = pygame.display.set_mode((900 , 560))
pygame.display.set_caption("asteroid game!")

health_font = pygame.font.SysFont("comicsans" , 30)

winner_font = pygame.font.SysFont("comicsans" ,200)

Blue_character_image = pygame.image.load(os.path.join("Assets" , "Blue.png"))
Grey_character_image = pygame.image.load(os.path.join("Assets" , "Grey.png"))
asteroid_image = pygame.image.load(os.path.join("Assets" , "astéroide.png"))
background = pygame.transform.scale(pygame.image.load(os.path.join("Assets" , "space.png")), (900,560))
Ball = pygame.transform.scale(pygame.image.load(os.path.join("Assets" , "Ball.png")),(120 , 120))
Blue_character = Blue_character_image


Grey_character = Grey_character_image 
asteroid = pygame.transform.scale(asteroid_image , (120, 120))

Blue_HIT  = pygame.USEREVENT+9
Grey_HIT  = pygame.USEREVENT+10
WINNER_HIT = pygame.USEREVENT+11

fps = 60
vel = 4
vel2 =4

# ------------------------------------first loop functions-----------------------------------------

def draw_window(Blue_character , Grey_character , Blue_rect , Grey_rect, Blue_health , Grey_health , asteroids_list) :
    WIN.fill((0 , 0 ,0))
    WIN.blit(background,(0,0))
    WIN.blit(Grey_character , (Grey_rect.x , Grey_rect.y) )
    WIN.blit(Blue_character , (Blue_rect.x , Blue_rect.y) )
    Blue_health_text = health_font.render("Blue :" +str(Blue_health), 1 , (255,255,255))
    Grey_health_text = health_font.render("Grey :" +str(Grey_health), 1 , (255,255,255))
    WIN.blit(Blue_health_text , (0, 0))
    WIN.blit(Grey_health_text , (900 - Grey_health_text.get_width(), 0))
    for asteroid_rect in asteroids_list : 
        WIN.blit(asteroid, (asteroid_rect.x,asteroid_rect.y))
    pygame.display.update()

def draw_winner(winner_text) : 
    winner_text_fonted = winner_font.render(winner_text , 1 , (255,255,255))
    WIN.blit(winner_text_fonted,(450 - (winner_text_fonted.get_width()/2),280-(winner_text_fonted.get_height()/2)) )
    pygame.display.update()

def Blue_handle_movements(keys_pressed , Blue_rect):
    if keys_pressed[pygame.K_UP]  and Blue_rect.y - vel > 0 :
        Blue_rect.y -= vel 
    if keys_pressed[pygame.K_DOWN] and Blue_rect.y + vel+ Blue_rect.height <560:
        Blue_rect.y += vel
    if keys_pressed[pygame.K_RIGHT] and Blue_rect.x + vel+ Blue_rect.width < 900 : 
        Blue_rect.x += vel
    if keys_pressed[pygame.K_LEFT] and Blue_rect.x - vel >0 : 
        Blue_rect.x-=vel
    

def Grey_handle_movements(keys_pressed , Grey_rect) : 

    if keys_pressed[pygame.K_z]  and Grey_rect.y - vel > 0 : 
        Grey_rect.y -= vel 
    if keys_pressed[pygame.K_s] and Grey_rect.y + vel+ Grey_rect.height <560:
        Grey_rect.y += vel
    if keys_pressed[pygame.K_d] and Grey_rect.x + vel+ Grey_rect.width < 900 : 
        Grey_rect.x += vel
    if keys_pressed[pygame.K_q] and Grey_rect.x - vel > 0 : 
        Grey_rect.x-=vel

def make_asteroid_rect(street_list,asteroids_list) :
    # wGreyle len(asteroids_list)<=8 : 
        # i = randint(0,3)
        j = randint(20 , 480)
        # if street_list[i] == "a" : 
        #     asteroid_rect = pygame.Rect(900,20,80,80)
        #     asteroids_list.append(asteroid_rect)
        
        # if street_list[i] == "b" : 
        #     asteroid_rect = pygame.Rect(900,160,80,80)
        #     asteroids_list.append(asteroid_rect)

        # if street_list[i] == "c" : 
        #     asteroid_rect = pygame.Rect(900,300,80,80)
        #     asteroids_list.append(asteroid_rect)

        # if street_list[i] == "d" : 
        #     asteroid_rect = pygame.Rect(900,440,80,80)
        #     asteroids_list.append(asteroid_rect)
        asteroid_rect = pygame.Rect(900 ,j , 80 , 80)
        asteroids_list.append(asteroid_rect)
            
def asteroid_handle_movement(asteroids_list, Blue_rect , Grey_rect) : 
    for asteroid_rect in asteroids_list :
        asteroid_rect.x -=9
        if asteroid_rect.x-9 <=0 : 
            asteroids_list.remove(asteroid_rect)
        if Blue_rect.colliderect(asteroid_rect) and Blue_rect.x != Grey_rect.x: 
            asteroids_list.remove(asteroid_rect)
            pygame.event.post(pygame.event.Event(Blue_HIT))
        if Grey_rect.colliderect(asteroid_rect) and Blue_rect.x != Grey_rect.x:
            asteroids_list.remove(asteroid_rect)
            pygame.event.post(pygame.event.Event(Grey_HIT))
        if Grey_rect.colliderect(asteroid_rect) and Blue_rect.x == Grey_rect.x : 
            asteroids_list.remove(asteroid_rect)
            pygame.event.post(pygame.event.Event(Grey_HIT))
            pygame.event.post(pygame.event.Event(Blue_HIT))

#--------------------------------------Second loop functions -------------------------------------------
def draw_window2(winner , winner_rect ,winner_health, Ball, Ball_rect) :
        WIN.blit(background,(0,0))
        WIN.blit(winner , (winner_rect.x , winner_rect.y) )
        winner_health_text = health_font.render("First round's winner :" +str(winner_health), 1 , (255,255,255))
        WIN.blit(winner_health_text , (450-winner_health_text.get_width()/2, 0))
        WIN.blit(Ball,(Ball_rect.x , Ball_rect.y))
        pygame.display.update()

def Ball_handle_movement(keys_pressed, Ball_rect,winner, winner_rect) : 
    if winner == Grey_character : 
        if keys_pressed[pygame.K_UP] and Ball_rect.y-vel2>0 : 
            Ball_rect.y-=vel2
        if keys_pressed[pygame.K_DOWN] and Ball_rect.y+Ball_rect.height+vel2 < 560 : 
            Ball_rect.y+=vel2
        if Ball_rect.x - vel2 >=0 : 
            Ball_rect.x-=vel2
    if winner == Blue_character :
        if keys_pressed[pygame.K_z] and Ball_rect.y-vel2>0 :  
            Ball_rect.y-=vel2
        if keys_pressed[pygame.K_s] and Ball_rect.y+Ball_rect.height+vel2 < 560 : 
            Ball_rect.y+=vel2
        if Ball_rect.x - vel2 >=0 : 
            Ball_rect.x-=vel2
    if Ball_rect.colliderect(winner_rect) : 
            pygame.event.post(pygame.event.Event(WINNER_HIT))

def draw_winner2(winner_text2) :     
        WIN.fill((0,0,0))
        winner_text2_ = health_font.render(f"{winner_text2} wins" , 1 , (255,255,255))
        WIN.blit(winner_text2_, (450 - (winner_text2_.get_width()/2),280-(winner_text2_.get_height()/2)))
        pygame.display.update()


#--------------------------------------     Game loop     ----------------------------------------------------------- 
def main() : 
    run = True
    clock = pygame.time.Clock()
    Blue_rect = pygame.Rect( 100 , 400 , 65 , 40 )
    Grey_rect = pygame.Rect(100 , 200 , 65 , 40 )
    asteroids_list = []
    street_list = ["a" , "b" , "c" , "d"] 
    Blue_health = 10
    Grey_health = 10
    Ball_rect = pygame.Rect(900 , 280 ,120, 120)
    key = True 
    intro_text = health_font.render("First round : Escape asteroids" , 1 , (255 , 255 , 255))
    start = datetime.datetime.now().second

    #-------------------------first loop function-------------------------------: 
    while abs((datetime.datetime.now().second+1)-start)%7!=0 : 
        WIN.blit(intro_text , (450-intro_text.get_width()/2 , 320-intro_text.get_height()/2))
        pygame.display.update()
    while run : 
        a = randint(1 , 100)    
        clock.tick(fps)
        for event in pygame.event.get() : 
            if event.type==pygame.QUIT : 
                run = False 
                pygame.quit()
            
            winner_text = ""
            if event.type == Blue_HIT : 
                if Blue_health-1 > 0 : 
                    Blue_health -=1
                else : 
                    winner_text = "Grey wins"
                    winner = Grey_character
                    winner_rect = Grey_rect
                    winner_health = Grey_health
                    Blue_health =0 
            if event.type == Grey_HIT :
                if Grey_health-1 > 0 : 
                    Grey_health -=1
                else : 
                    winner_text = "Blue wins"
                    winner= Blue_character
                    winner_rect = Blue_rect
                    winner_health = Blue_health
                    Grey_health = 0
        keys_pressed = pygame.key.get_pressed()
        Blue_handle_movements(keys_pressed, Blue_rect)
        Grey_handle_movements(keys_pressed, Grey_rect)
        asteroid_handle_movement(asteroids_list , Blue_rect , Grey_rect)
        if a % 37 ==0 and key == True: 
            make_asteroid_rect(street_list , asteroids_list)
        draw_window(Blue_character , Grey_character , Blue_rect , Grey_rect,Blue_health , Grey_health,asteroids_list)
        if winner_text != "" : 
                draw_winner(winner_text)
                pygame.time.delay(3000)
                break
    
    run2 = True
    draw = True
    start2 = datetime.datetime.now().second
    intro_text2 = health_font.render("Last chance loser: touch your opponent" , 1 , (255, 255,255))

    while abs(datetime.datetime.now().second+1 - start2)%7!=0 : 
        WIN.fill((0 , 0 ,0))
        WIN.blit(intro_text2 , ((450-intro_text2.get_width()/2 , 280-intro_text2.get_height()/2)))
        pygame.display.update()

    while run2 : 
        clock.tick(fps)
        key == False
        keys_pressed = pygame.key.get_pressed()
        winner_text2 = ""
        for event in pygame.event.get() : 
            if event.type==pygame.QUIT : 
                run = False 
                pygame.quit()

            if event.type == WINNER_HIT : 
                winner_health = 0

        if winner_health == 0 and winner == Blue_character : 
            winner_text2 = "Grey"
            
        if winner_health == 0 and winner == Grey_character : 
            winner_text2 = "Blue"

        if winner_health != 0 and winner == Grey_character and Ball_rect.x == 0: 
            winner_text2 = "Grey"
        
        if winner_health != 0 and winner == Blue_character and Ball_rect.x == 0: 
            winner_text2 = "Blue"

        if winner == Blue_character : 
            Blue_handle_movements(keys_pressed , Blue_rect)

        else : 
            Grey_handle_movements(keys_pressed , Grey_rect)

        Ball_handle_movement(keys_pressed, Ball_rect,winner , winner_rect)
        if draw == True :
            draw_window2(winner , winner_rect,winner_health , Ball, Ball_rect)
        if winner_text2 != "" : 
            draw = False
            draw_winner2(winner_text2)
            pygame.time.delay(4000)
            run2 = False
    main()
if __name__== "__main__" : 
    main()
