import pygame, random

pygame.init()

altura = 600
largura = 600

janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Aventura Idle!")

# POSIÇÔES ---
x = 300
y = 300

# VELOCIDADES ---
velX = random.uniform(-0.1, 0.1)
velY = random.uniform(-0.1, 0.1)

# BOLINHA ---
cor = (255, 255, 255)
raio = 20

rodando = True

while rodando:
    janela.fill((0, 0, 0))

    pygame.draw.circle(janela, cor, (x, y), raio)

    pygame.display.update()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    x += velX
    y += velY

    if x > (largura - raio) or x < raio:
        velX = -velX

    if y > (altura - raio) or y < raio:
        velY = -velY
    

pygame.quit()