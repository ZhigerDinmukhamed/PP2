import pygame
from datetime import datetime

pygame.init()

screen = pygame.display.set_mode((829, 836))
done = False
main_image = pygame.image.load("C:\\Users\\zhige\\Downloads\\mainclock.png")
min_image = pygame.image.load("C:\\Users\\zhige\\Downloads\\rightarm.png")
sec_image = pygame.image.load("C:\\Users\\zhige\\Downloads\\leftarm.png")
rect = main_image.get_rect(center=(415, 418))

while not done:
    screen.blit(main_image, (-285, -110))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    time = datetime.now().time()

    sec_angle = -(time.second * 6)
    frame_sec = pygame.transform.rotate(sec_image, sec_angle)
    sec_rect = frame_sec.get_rect(center=rect.center)
    screen.blit(frame_sec, sec_rect.topleft)

    min_angle = -(time.minute * 6)
    frame_min = pygame.transform.rotate(min_image, min_angle)
    min_rect = frame_min.get_rect(center=rect.center)
    screen.blit(frame_min, min_rect.topleft)

    pygame.display.flip()