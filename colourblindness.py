import pygame

pygame.init()

windowHeight = 451
windowWidth = 610

screen = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)
pygame.display.set_caption('P = protonopia, D = deutranopia, T = tritanopia, G = grayscale, R = RESET')

''' 
Place an image in  C:\Program Files (x86)\Python36-32 , name it 'download.jpg'.

P = protonopia
D = deutranopia
T = tritanopia

G = grayscale
C = print colours
ESC = exit
'''


def make_greyscale(matrix):
    """ Monochromacy (seeing no colours at all, grayscale) is technically a form of colour-blindness too. """
    for x in range(0, matrix.get_width()):
        for y in range(0, matrix.get_height()):  # Using a nested for-loop to go through the image pixel-by-pixel.
            old_colour = matrix.get_at((x, y))
            grey = (
                               old_colour.r + old_colour.g + old_colour.b) / 3  # Setting R G and B to the same value creates gray.
            new_colour = (grey, grey, grey)  # The size of that gray value changes the brightness of that pixel.
            matrix.set_at((x, y), new_colour)
    screen.blit(matrix, (0, 0))


def print_colours(pixel_matrix):
    """ A debugging tool I decided to leave in, prints the RGBA value of each currently displayed pixel, one by one."""
    for x in range(0, pixel_matrix.get_width()):
        for y in range(0, pixel_matrix.get_height()):
            old_colour = pixel_matrix.get_at((x, y))
            print(old_colour)


def simulate_deutranopia(matrix):
    """ deuteranopia is red-green blind and it the most common form of colour-blindness. """
    for x in range(0, matrix.get_width()):
        for y in range(0, matrix.get_height()):
            old = matrix.get_at((x, y))
            redgreen = (old.r + old.g) / 2  # Equalizing red and green removes both, leaving only yellow and blue.
            new = (int(redgreen), int(redgreen), old.b)
            matrix.set_at((x, y), new)
    screen.blit(matrix, (0, 0))


def simulate_protonopia(matrix):
    """ protonopia is also red-green blind, though less sensitive to red light specifically. """
    for x in range(0, matrix.get_width()):
        for y in range(0, matrix.get_height()):
            old = matrix.get_at((x, y))
            green = (old.r + old.g) / 2  # Equalizing red and green removes both colours, leaving only yellow and blue.
            red = (old.r + old.g) / 1.6  # The red channel will be a little stronger to imitate the warmth needed.
            if red > 255:  # This is to prevent crashing in cases where 'red' would be above 255.
                red = 255
            new = (int(red), int(green), old.b)
            matrix.set_at((x, y), new)
    screen.blit(matrix, (0, 0))


def simulate_tritanopia(matrix):
    """ tritanopia is 'blue-yellow blind', all colours appear to be red and cyan. It is extremely rare."""
    for x in range(0, matrix.get_width()):
        for y in range(0, matrix.get_height()):
            old = matrix.get_at((x, y))
            greenblue = ((old.b + old.g) / 2)  # Equalizing the blue and green eliminates yellow and flattens blues.
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

        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            simulate_deutranopia(image)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            simulate_protonopia(image)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
            simulate_tritanopia(image)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            image = pygame.image.load("download.jpg").convert()  # Resetting is simply reloading the original image.
            screen.blit(image, (0, 0))

    pygame.display.update()

screen.fill(BLACK)
pygame.display.flip()
