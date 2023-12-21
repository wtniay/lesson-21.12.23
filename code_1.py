from pygame import* 

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def update_first(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 85:
            self.rect.y += self.speed

    def update_second(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 85:
            self.rect.y += self.speed



win_height = 700
win_width = 700
display.set_caption('Ping - Pong')
window = display.set_mode((win_height, win_width))
back = transform.scale(image.load('eed.png'),(700, 700))

player1 = Player('eed.png', 30, 300, 30, 100, 6)
player2 = Player('eed.png', 640, 300, 30, 100, 6 )
run = True
game = True
clock = time.Clock()
fps = 60

while game == True:
    window.blit(back, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if run:
        player1.update_first()
        player2.update_second()
        player1.reset()
        player2.reset()
    display.update()
    clock.tick(fps)