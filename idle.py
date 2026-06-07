import pygame

pygame.init()

janela = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Aventura Idle!")

rodando = True

while rodando:
    pygame.display.update()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

pygame.quit()