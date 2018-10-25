import pygame
import Classes

pygame.init()

windowHeight = 150
windowWidth = 450

screen = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)
pygame.display.set_caption('Debugger for weapon generation')

pygame.font.init()  # Initiating Font module
my_font = pygame.font.SysFont('Arial', 24)  # Creating a font

finished = False


def test_weapon_generator():
    """Creates a Weapon Object and displays it and its name on the screen"""

    # Screen is cleared in case we had something previously displayed
    screen.fill((0, 0, 0))

    weapon = Classes.Weapon()

    # Display of weapon texture
    screen.blit(weapon.weapon_texture, (0, 0))

    # Creation of new font image
    text_surface = my_font.render(weapon.name, False, (255, 255, 255))

    # Display of full weapon name beneath
    screen.blit(text_surface, (0, 36))


while finished is False:    # Basic game loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finished = True
        # when 'g' is pressed a random item is generated
        if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            test_weapon_generator()
        pygame.display.update()

screen.fill((255, 255, 255))
pygame.display.flip()
