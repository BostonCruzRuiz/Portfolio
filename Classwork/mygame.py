import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame Game')

WHITE = (255, 255, 255)

FPS = 60

def draw_windows():
    WIN.fill(WHITE)
    pygame.display.update()


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_windows()

    pygame.quit()


if __name__=='__main__':
    main()
