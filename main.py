from pygame import *
window = display.set_mode((700,500))
display.set_caption('Пинг понг')
window.fill((255,200,200))
fps = 60
game = True
clock = time.Clock()
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    display.update()
    clock.tick(fps)