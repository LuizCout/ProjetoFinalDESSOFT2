# ============================================================
# IMPORTAÇÕES DAS BIBLIOTECAS
# ============================================================

import pygame        # Importa a biblioteca pygame, responsável por criar a janela, desenhar na tela, capturar teclas e reproduzir sons
import sys           # Importa o módulo sys, usado para encerrar o programa com sys.exit()
import random        # Importa o módulo random, usado para gerar números aleatórios (posição de itens, comportamento de barris, etc.)
import math          # Importa o módulo math, usado para funções matemáticas como seno e cosseno (animações de pulso, fumaça, brilho)

# INICIALIZAÇÃO DO PYGAME E DO SOM

pygame.init()        # Inicializa todos os módulos internos do pygame (gráficos, eventos, fonte, etc.)
pygame.mixer.init()  # Inicializa especificamente o módulo de áudio do pygame para permitir tocar sons e músicas
pygame.mixer.music.load(r"C:\Users\rezen\Downloads\hard_boss_battle_1_bpm200.ogg")  # Carrega o arquivo de música .ogg do caminho especificado para a memória
pygame.mixer.music.set_volume(0.3)   # Define o volume da música em 30% (0.0 = mudo, 1.0 = máximo)
pygame.mixer.music.play(-1)          # Começa a tocar a música; o argumento -1 significa que ela vai repetir em loop infinito

# CONFIGURAÇÕES DE TELA E MUNDO

LARGURA, ALTURA = 900, 800   # Define a largura (900 pixels) e a altura (800 pixels) da janela visível do jogo
MUNDO_ALTURA = 1400          # Define a altura total do mundo do jogo (maior que a tela), permitindo scroll vertical com câmera

# ============================================================
# CRIAÇÃO DA JANELA
# ============================================================

TELA = pygame.display.set_mode((LARGURA, ALTURA))  # Cria a janela do jogo com as dimensões definidas acima e armazena na variável TELA
pygame.display.set_caption("Dino Barrel")           # Define o título que aparece na barra superior da janela do jogo

# ============================================================
# CONTROLE DE TEMPO
# ============================================================

CLOCK = pygame.time.Clock()  # Cria um objeto de relógio que controla quantos frames por segundo o jogo roda
FPS = 60                     # Define a taxa de quadros por segundo em 60 FPS (frames per second)

# CARREGAMENTO DAS IMAGENS DE FUNDO 

fundo_img = pygame.image.load(r"C:\Users\rezen\Downloads\fundogame.jpg").convert() # Carrega a imagem de fundo da fase 1 do arquivo e converte para formato otimizado de renderização
fundo_img = pygame.transform.scale(fundo_img, (LARGURA, ALTURA))  # Redimensiona a imagem de fundo da fase 1 para cobrir exatamente o tamanho da tela (900x800)
 
fundo_fase2 = pygame.image.load(r"C:\Users\rezen\Downloads\fase final.webp").convert()  # Carrega a imagem de fundo da fase 2 (arquivo .webp) e converte para formato otimizado
fundo_fase2 = pygame.transform.scale(fundo_fase2, (LARGURA, ALTURA))  # Redimensiona a imagem de fundo da fase 2 para cobrir exatamente o tamanho da tela (900x800)
 