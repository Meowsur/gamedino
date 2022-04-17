from pygame import *



font.init()
font1 = font.SysFont('Arial', 80)
win1 = font1.render('PLAYER 1', True, (255, 255, 255))
win2 = font1.render('PLAYER 2', True, (255, 255, 255))
font2 = font.SysFont('Arial', 36)

win_width = 1000
win_height = 700
window = display.set_mode((win_width, win_height))
display.set_caption("P1ng-P0ng")
wb = "background ping-pong.jpg"
background = transform.scale(image.load(wb), (win_width, win_height))
platform = "ginger.png"
image_ball = "pokeball.png"


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
        if keys[k_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[k_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update1(self):
        if keys[k_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player(platform, 30, 200, 7, 50, 150)
racket2 = Player(platform, 970, 200, 7, 50, 150)
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
            


