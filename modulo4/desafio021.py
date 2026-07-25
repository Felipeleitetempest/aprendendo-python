import pygame
pygame.init()
pygame.mixer.music.load('lowtiergod.mp3')
pygame.mixer.music.play()
pygame.event.wait()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
pygame.quit(S)
