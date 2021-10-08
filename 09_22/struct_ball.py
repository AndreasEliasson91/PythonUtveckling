import pygame

WIDTH = 400
HEIGHT = 400
FPS = 60
RADIUS = 10

# R G B (0-255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    x_r = 100
    y_r = 100
    x_r_step = -1
    y_r_step = 1

    x_y = 200
    y_y = 250
    x_y_step = 1
    y_y_step = 1

    running = True

    while running:
        # Process input/events
        for event in pygame.event.get():        # Always looks the same in Pygame-games!
            if event.type == pygame.QUIT:
                running = False

        # Update
        x_r += x_r_step
        y_r += y_r_step

        if x_r <= RADIUS or x_r >= WIDTH - RADIUS:
            x_r_step *= -1
        if y_r <= RADIUS or y_r >= HEIGHT - RADIUS:
            y_r_step *= -1

        x_y += x_y_step
        y_y += y_y_step

        if x_y <= RADIUS or x_y >= WIDTH - RADIUS:
            x_y_step *= -1
        if y_y <= RADIUS or y_y >= HEIGHT - RADIUS:
            y_y_step *= -1

        # Draw
        screen.fill(BLACK)
        pygame.draw.circle(screen, RED, (x_r, y_r), RADIUS)
        pygame.draw.circle(screen, YELLOW, (x_y, y_y), RADIUS)

        # Control time
        clock.tick(FPS)

        # Show new content
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
