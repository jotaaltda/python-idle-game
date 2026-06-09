import pygame, random, math

# INTERFACE ----
pygame.init()

altura = 600
largura = 600

janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Aventura Idle!")

fonte = pygame.font.Font(None, 30)

clock = pygame.time.Clock()


# JOGADOR ----
cor = (255, 255, 255)
raio = 20

vida = 10
velocidade = 5
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
velocidadeini = 5
danoini = 1

xini = random.randint(0, largura)
yini = random.randint(0, altura)

velXini = random.uniform(-velocidadeini, velocidadeini)
velYini = random.uniform(-velocidadeini, velocidadeini)
# ------------

rodando = True
encostoux = False
encostouy = False
iniencostoux = False
iniencostouy = False

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
    clock.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    x += velX
    y += velY

    xini += velXini
    yini += velYini

    posicao = [x, y]
    posicaoini = [xini, yini]

    distancia = math.dist(posicao, posicaoini)

    if (x > (largura - raio) or x < raio or distancia < (raioini + raio)) and encostoux == False:
        velX = -velX
        encostoux = True
    elif (y > (altura - raio) or y < raio or distancia < (raioini + raio)) and encostouy == False:
        velY = -velY
        encostouy = True

    if (xini > (largura - raioini) or xini < raioini or distancia < (raioini + raio)) and iniencostoux == False:
        velXini = -velXini
        iniencostoux = True
    elif (yini > (altura - raioini) or yini < raioini or distancia < (raioini + raio)) and iniencostouy == False:
        velYini = -velYini
        iniencostouy = True

    if distancia > (raioini + raio):
        encostoux = False
        encostouy = False
        iniencostoux = False
        iniencostouy = False
    

pygame.quit()