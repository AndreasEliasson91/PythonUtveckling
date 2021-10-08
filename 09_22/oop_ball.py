import pygame
import random

WIDTH = 400
HEIGHT = 400
FPS = 60
RADIUS = 10

RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


class Ball:
    def __init__(self, color, x, y, x_step, y_step):
        self.color = color
        self.x = x
        self.y = y
        self.x_step = x_step
        self.y_step = y_step

    def move(self):
        self.x += self.x_step
        self.y += self.y_step

    def check_bounce(self):
        if self.x <= RADIUS or self.x >= WIDTH - RADIUS:
            self.x_step *= -1
        if self.y <= RADIUS or self.y >= WIDTH - RADIUS:
            self.y_step *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), RADIUS)


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    colors = [RED, BLUE, GREEN, YELLOW, WHITE]

    balls = []
    for _ in range(100):
        color = random.choice(colors)
        x = random.randrange(RADIUS, WIDTH-RADIUS)
        y = random.randrange(RADIUS, HEIGHT-RADIUS)
        x_step = random.choice([-1, 1])
        y_step = random.choice([-1, 1])
        ball = Ball(color, x, y, x_step, y_step)
        balls.append(ball)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        for ball in balls:
            ball.move()
            ball.check_bounce()
            ball.draw(screen)

        clock.tick(FPS)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
