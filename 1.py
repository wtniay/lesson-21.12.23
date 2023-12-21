from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # метод, що малює героя на вікні
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# клас головного гравця


    # метод "постріл" (використовуємо місце гравця, щоб створити там кулю)
    def fire(self):
        pass


# ігрова сцена
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))

# музика
mixer.init()
mixer.music.load('space.ogg')
# mixer.music.play()

# персонажі гри
ship = Player('rocket.png', 5, win_height - 100, 80, 100, 10)

game = True  # прапорець скидається кнопкою закриття вікна
finish = False  # змінна "гра закінчилася"

clock = time.Clock()
FPS = 60

while game:
    # подія натискання на кнопку Закрити
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))  # оновлюємо фон

        ship.update()  # рухи спрайтів
        ship.reset()  # відображення спрайта

    display.update()
    clock.tick(FPS)
