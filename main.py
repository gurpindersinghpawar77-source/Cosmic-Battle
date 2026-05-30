import pygame.examples.aliens as aliens
import pygame
aliens.main()
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
FONT_SIZE = 72

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")

clock = pygame.time.Clock()

running = True
won = False

font = pygame.font.Font(None, FONT_SIZE)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    if won:
        win_text = font.render("You win!", True, pygame.Color("black"))
        screen.blit(
            win_text,
            (
                (SCREEN_WIDTH - win_text.get_width()) // 2,
                (SCREEN_HEIGHT - win_text.get_height()) // 2,
            ),
        )

    pygame.display.flip()
    clock.tick(90)

pygame.quit()