import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definições da janela do jogo
largura_janela = 800
altura_janela = 600
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Minigame de Avião")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Definições do avião
aviao_img = pygame.image.load("aviao.png")
aviao_largura = 80
aviao_altura = 30
aviao_x = 100
aviao_y = altura_janela // 2 - aviao_altura // 2
aviao_velocidade = 5

# Definições dos obstáculos
obstaculo_largura = 50
obstaculo_altura = 300
obstaculo_x = largura_janela
obstaculo_y = random.randint(0, altura_janela - obstaculo_altura)
obstaculo_velocidade = 5

# Score
pontos = 0

# Fonte para o score
fonte = pygame.font.SysFont(None, 30)

# Função para desenhar o avião na tela
def desenhar_aviao(x, y):
    janela.blit(aviao_img, (x, y))

# Função para desenhar obstáculos na tela
def desenhar_obstaculo(x, y):
    pygame.draw.rect(janela, preto, (x, y, obstaculo_largura, obstaculo_altura))
    pygame.draw.rect(janela, preto, (x+100, y, obstaculo_largura, obstaculo_altura))

# Função para desenhar o score na tela
def desenhar_score(score):
    texto = fonte.render("Pontuação: " + str(score), True, preto)
    janela.blit(texto, (10, 10))

# Loop principal do jogo
jogo_ativo = True
while jogo_ativo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo_ativo = False

    # Controle do avião
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP]:
        aviao_y -= aviao_velocidade
    if teclas[pygame.K_DOWN]:
        aviao_y += aviao_velocidade

    # Movimento dos obstáculos
    obstaculo_x -= obstaculo_velocidade
    if obstaculo_x < 0:
        obstaculo_x = largura_janela
        obstaculo_y = random.randint(0, altura_janela - obstaculo_altura)
        pontos += 1  # Incrementa a pontuação quando um novo obstáculo é gerado
        obstaculo_velocidade += 0.5  # Aumenta a velocidade dos obstáculos conforme a pontuação

    # Colisão com os obstáculos
    if aviao_x < obstaculo_x + obstaculo_largura and aviao_x + aviao_largura > obstaculo_x:
        if aviao_y < obstaculo_y + obstaculo_altura and aviao_y + aviao_altura > obstaculo_y:
            print("Você bateu em um obstáculo! Fim de jogo.")
            jogo_ativo = False

    # Limpeza da tela
    janela.fill(branco)

    # Desenho do avião e obstáculos
    desenhar_aviao(aviao_x, aviao_y)
    desenhar_obstaculo(obstaculo_x, obstaculo_y)

    # Desenho do score
    desenhar_score(pontos)

    # Atualização da tela
    pygame.display.update()

    # Controle de FPS
    pygame.time.Clock().tick(60)

# Encerramento do Pygame
pygame.quit()

