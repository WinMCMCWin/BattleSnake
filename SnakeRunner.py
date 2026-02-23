import pygame
pygame.init()
TEST_WIDTH = 800
TEST_HEIGHT = 600
test_Screen = pygame.display.set_mode((TEST_WIDTH, TEST_HEIGHT))

run_cond = True
while run_cond == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_cond = False
pygame.quit()