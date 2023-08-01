import pygame

pygame.init()
pygame.mixer.music.load('extras/teste.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
