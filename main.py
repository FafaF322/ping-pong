from pygame import *
font.init()
window = display.set_mode((700,500))
display.set_caption('Пинг понг')
window.fill((255,255,255))
class GameSprite(sprite.Sprite):
    def __init__(self,player_speed,player_x,player_y,player_image,height,width):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width,height))
        self.player_speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def movement_left(self):
        key_presed = key.get_pressed()
        if key_presed[K_w] and self.rect.y > 0:
            self.rect.y -= self.player_speed
        if key_presed[K_s] and self.rect.y < 420:
            self.rect.y += self.player_speed
    def movement_right(self):
        key_presed = key.get_pressed()
        if key_presed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.player_speed
        if key_presed[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.player_speed
font1 = font.SysFont('Arial',50)
player_left = Player(7,0,170,'i.jpg',130,90)
player_right = Player(7,620,170,'i.jpg',130,90)
ball = GameSprite(3,350,250,'ball.jpg',65,65)
speed_x = 3
speed_y = 3
win = font1.render('PLAYER 1 WIN',True,(0,100,100))
lose_win = font1.render('PLAYER 2 WIN',True,(100,0,0))

fps = 60
game = True
finish = False
clock = time.Clock()
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        window.fill((255,255,255))
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y >= 435 or ball.rect.y <= 0:
            speed_y *= -1
        if sprite.collide_rect(player_left,ball) or sprite.collide_rect(player_right,ball):
            speed_x *= -1
        if ball.rect.x <= 0:
            window.blit(lose_win,(150,200))
            finish = True
        if ball.rect.x >= 650:
            window.blit(win,(150,200))
            finish = True
        player_left.movement_left()
        player_left.reset()
        player_right.movement_right()
        player_right.reset()
    display.update()
    clock.tick(fps)
