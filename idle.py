import pygame, random

# INTERFACE ---
pygame.init()

altura = 600
largura = 600

janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Aventura Idle!")

fonte = pygame.font.Font(None, 30)

# BOLINHA ---
cor = (255, 255, 255)
raio = 20

vida = 10
velocidade = 0.1
dano = 1

moedas = 0

# POSIÇÔES ---
x = 300
y = 300

# VELOCIDADES ---
velX = random.uniform(-velocidade, velocidade)
velY = random.uniform(-velocidade, velocidade)

rodando = True

while rodando:
    janela.fill((0, 0, 0))

    pygame.draw.circle(janela, cor, (x, y), raio)

    textovida = fonte.render(f"Vida: {vida}", True, (255, 255, 255))
    textovel= fonte.render(f"Velocidade: {velocidade}", True, (255, 255, 255))
    textodano = fonte.render(f"Dano: {dano}", True, (255, 255, 255))
    textomoedas = fonte.render(f"Moedas: {moedas}", True, (255, 255, 255))

    janela.blit(textovida, (5, 1))
    janela.blit(textovel, (5, 25))
    janela.blit(textodano, (5, 50))
    janela.blit(textomoedas, (5, 100))

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