from pygame import *



font.init()
font1 = font.SysFont('Arial', 80)
win1 = font1.render('PLAYER 1 WIN!', True, (255, 255, 255))
win2 = font1.render('PLAYER 2 WIN!', True, (255, 255, 255))
font2 = font.SysFont('Arial', 36)

win_width = 1000
win_height = 700
window = display.set_mode((win_width, win_height))
display.set_caption("P1ng-P0ng")
wb = "background ping-pong.jpg"
background = transform.scale(image.load(wb), (win_width, win_height))
platform = "ginger.png"
image_ball = "pokeball.png"
heart3_image = "heart3.png"
heart2_image = "heart2.png"
heart1_image = "heart1.png"

class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в которой он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 



class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


game = True
finish = False
clock = time.Clock()
FPS = 60
life_l = 3
life_r = 3

heart3R = Player(heart3_image, 870, 10, 0, 130, 100)
heart2R = Player(heart2_image, 870, 30, 0, 80, 50)
heart1R = Player(heart1_image, 870, 40, 0, 40, 30)
heart3 = Player(heart3_image, 30, 10, 0, 130, 100)
heart2 = Player(heart2_image, 30, 20, 0, 80, 50)
heart1 = Player(heart1_image, 30, 40, 0, 40, 30)
racket1 = Player(platform, 30, 200, 7, 50, 150)
racket2 = Player(platform, 920, 200, 7, 50, 150)
ball = GameSprite(image_ball, 500, 350, 5, 50, 50)

speed_x = 3
speed_y = 3


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0,0))
        racket1.update1()
        racket2.update()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            life_l -= 1
            ball.kill()
            ball = GameSprite(image_ball, 500, 350, 5, 50, 50)
            ball.rect.x += speed_x
            ball.rect.y += speed_y

        if ball.rect.x > win_width:
            life_r -= 1
            ball.kill()
            ball = GameSprite(image_ball, 500, 350, 5, 50, 50)
            ball.rect.x += speed_x
            ball.rect.y += speed_y
        if life_l == 0:
            finish = True
            window.blit(win2, (270, 270))
            game_over = True

        if life_r == 0:
            finish = True
            window.blit(win1, (270, 270))
            game_over = True

        if life_l >= 3:
            heart3.reset()  
        if life_l == 2:
            heart2.reset()
        if life_l == 1:
            heart1.reset() 

        if life_r >= 3:
            heart3R.reset()
        if life_r == 2:
            heart2R.reset()
        if life_r == 1:
            heart1R.reset()

        racket1.reset()
        racket2.reset()
        ball.reset()

        display.update()
    else:
        finish = False
        life_l = 3
        life_r = 3
        ball.kill()
        ball = GameSprite(image_ball, 500, 350, 5, 50, 50)
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
    display.update()
    clock.tick(FPS)


