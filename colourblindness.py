import pygame

pygame.init()

windowHeight = 451
windowWidth = 610

screen = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)
pygame.display.set_caption('Colour Blindness')

''' 
P = protonopia
D = deutranopia
T = tritanopia

G = grayscale
C = print colours
ESC = exit

At the moment, protonopia and deutranopia do the same thing.
I want protonopia to make the image slightly more red, but 
 things like '(old.r * 1.1)' aren't working. '''


def make_greyscale(matrix):
    for x in range(0, matrix.get_width()):
        for y in range(0, matrix.get_height()):
            old_colour = matrix.get_at((x, y))
            grey = (old_colour.r + old_colour.g + old_colour.b) / 3
            new_colour = (grey, grey, grey)
            matrix.set_at((x, y), new_colour)
    screen.blit(matrix, (0, 0))


def print_colours(pixel_matrix):
    for x in range(0, pixel_matrix.get_width()):
        for y in range(0, pixel_matrix.get_height()):
            old_colour = pixel_matrix.get_at((x, y))
            print(old_colour)


def simulate_protonopia(matrix):
    for x in range(0, matrix.get_width()):
        for y in range(0, matrix.get_height()):
            old = matrix.get_at((x, y))
            redgreen = (old.r + old.g) / 2
            # redboost = (old.r + old.g) / 1.9
            # new = (int(redboost), int(redgreen), old.b)
            new = (int(redgreen), int(redgreen), old.b)
            matrix.set_at((x, y), new)
    screen.blit(matrix, (0, 0))


def simulate_deutranopia(matrix):
    for x in range(0, matrix.get_width()):
        for y in range(0, matrix.get_height()):
            old = matrix.get_at((x, y))
            redgreen = (old.r + old.g) / 2
            new = (int(redgreen), int(redgreen), old.b)
            matrix.set_at((x, y), new)
    screen.blit(matrix, (0, 0))


def simulate_tritanopia(matrix):
    for x in range(0, matrix.get_width()):
        for y in range(0, matrix.get_height()):
            old = matrix.get_at((x, y))
            greenblue = ((old.b + old.g) / 2)
            new = (old.r, int(greenblue), int(greenblue))
            matrix.set_at((x, y), new)
    screen.blit(matrix, (0, 0))


image = pygame.image.load("download.jpg").convert()
screen.blit(image, (0, 0))
BLACK = (0, 0, 0)
finished = False

while finished is False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finished = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            make_greyscale(image)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            print_colours(image)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            simulate_protonopia(image)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            simulate_deutranopia(image)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
            simulate_tritanopia(image)

    pygame.display.update()


screen.fill(BLACK)
pygame.display.flip()
