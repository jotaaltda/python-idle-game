import pygame, random

# INTERFACE ----
pygame.init()

altura = 600
largura = 600

janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Aventura Idle!")

fonte = pygame.font.Font(None, 30)

# JOGADOR ----
cor = (255, 255, 255)
raio = 20

vida = 10
velocidade = 0.1
dano = 1

moedas = 0

x = 300
y = 300

velX = random.uniform(-velocidade, velocidade)
velY = random.uniform(-velocidade, velocidade)
# ------------

# INIMIGO ----
corini = (255, 0, 0)
raioini = 20

vidaini = 1
velocidadeini = 0.1
danoini = 1

xini = random.randint(0, largura)
yini = random.randint(0, altura)

velXini = random.uniform(-velocidadeini, velocidadeini)
velYini = random.uniform(-velocidadeini, velocidadeini)
# ------------

rodando = True

while rodando:
    janela.fill((0, 0, 0))

    pygame.draw.circle(janela, cor, (x, y), raio)
    pygame.draw.circle(janela, corini, (xini, yini), raioini)

    textovida = fonte.render(f"Vida: {vida}", True, (255, 255, 255))
    textovel= fonte.render(f"Velocidade: {velocidade}", True, (255, 255, 255))
    textodano = fonte.render(f"Dano: {dano}", True, (255, 255, 255))
    textomoedas = fonte.render(f"Moedas: {moedas}", True, (255, 255, 255))

    textoVidaIni = fonte.render(f"{vidaini}", True, (255, 255, 255))

    janela.blit(textovida, (5, 1))
    janela.blit(textovel, (5, 25))
    janela.blit(textodano, (5, 50))
    janela.blit(textomoedas, (5, 100))

    retangulo = textoVidaIni.get_rect(center=(xini, yini))

    janela.blit(textoVidaIni, retangulo)

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

    xini += velXini
    yini += velYini

    if xini > (largura - raioini) or xini < raioini:
        velXini = -velXini

    if yini > (altura - raioini) or yini < raioini:
        velYini = -velYini
    

pygame.quit()