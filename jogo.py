
# IMPORTAÇÕES DAS BIBLIOTECAS


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


# CRIAÇÃO DA JANELA


TELA = pygame.display.set_mode((LARGURA, ALTURA))  # Cria a janela do jogo com as dimensões definidas acima e armazena na variável TELA
pygame.display.set_caption("Dino Barrel")           # Define o título que aparece na barra superior da janela do jogo


# CONTROLE DE TEMPO


CLOCK = pygame.time.Clock()  # Cria um objeto de relógio que controla quantos frames por segundo o jogo roda
FPS = 60                     # Define a taxa de quadros por segundo em 60 FPS (frames per second)

# CARREGAMENTO DAS IMAGENS DE FUNDO 

fundo_img = pygame.image.load(r"C:\Users\rezen\Downloads\fundogame.jpg").convert() # Carrega a imagem de fundo da fase 1 do arquivo e converte para formato otimizado de renderização
fundo_img = pygame.transform.scale(fundo_img, (LARGURA, ALTURA))  # Redimensiona a imagem de fundo da fase 1 para cobrir exatamente o tamanho da tela (900x800)
 
fundo_fase2 = pygame.image.load(r"C:\Users\rezen\Downloads\fase final.webp").convert()  # Carrega a imagem de fundo da fase 2 (arquivo .webp) e converte para formato otimizado
fundo_fase2 = pygame.transform.scale(fundo_fase2, (LARGURA, ALTURA))  # Redimensiona a imagem de fundo da fase 2 para cobrir exatamente o tamanho da tela (900x800)
 
 #DEFINIÇÃO DE CORES

BRANCO       = (255, 255, 255)   # Cor branca: máximo nos três canais vermelho, verde e azul
PRETO        = (0, 0, 0)         # Cor preta: zero nos três canais
CINZA_ESC    = (30, 30, 30)      # Cinza muito escuro, quase preto, usado em fundos e sombras
AMARELO      = (255, 220, 0)     # Amarelo vivo, usado para o objetivo e textos de fase
VERMELHO     = (220, 50, 50)     # Vermelho médio, usado em elementos de perigo
AZUL_CLARO   = (80, 180, 255)    # Azul claro, usado em efeitos e itens de velocidade
LARANJA      = (255, 120, 30)    # Laranja usado em detalhes decorativos e efeitos de fogo
LARANJA_ESC  = (200, 80, 10)     # Laranja escuro, para contrastes e sombras de fogo
CINZA_PEDRA  = (90, 85, 80)      # Cinza com tom de pedra, usado para desenhar elementos do vulcão
CINZA_PEDRA2 = (120, 110, 100)   # Cinza pedra mais claro, para variações de textura no vulcão
VERMELHO_LAVA  = (255, 60, 0)    # Vermelho intenso que representa a lava do vulcão
AMARELO_LAVA   = (255, 200, 0)   # Amarelo quente que representa o brilho incandescente da lava


# FUNÇÃO: desenhar_vulcao


def desenhar_vulcao(surface, t):
    # Recebe a superfície onde vai desenhar (surface) e o contador de tempo (t) para animações
    
    surface.fill((15, 10, 30))  # Preenche o fundo da tela com azul escuro quase preto, simulando o céu noturno

    # --- Estrelas ---
    random.seed(42)              # Fixa a semente do gerador aleatório em 42 para que as estrelas apareçam sempre no mesmo lugar
    for _ in range(120):         # Repete o bloco 120 vezes, criando 120 estrelas no céu
        sx = random.randint(0, LARGURA)                   # Sorteia a posição horizontal da estrela dentro da largura da tela
        sy = random.randint(0, int(ALTURA * 0.55))        # Sorteia a posição vertical da estrela no topo (55% superior da tela)
        brilho = 100 + int(60 * abs(math.sin(t * 0.03 + sx)))  # Calcula o brilho da estrela usando seno para criar efeito de cintilação animada
        pygame.draw.circle(surface, (brilho, brilho, brilho), (sx, sy), 1)  # Desenha a estrela como um círculo de raio 1 pixel com o brilho calculado

    random.seed()  # Remove a semente fixa, voltando ao comportamento aleatório normal para o resto do código

    # --- Montanhas ao fundo ---
    montanha = [...]  # Define os vértices do polígono que forma as montanhas ao fundo (lista de tuplas com coordenadas x, y)
    pygame.draw.polygon(surface, (25, 20, 40), montanha)  # Desenha as montanhas como um polígono preenchido com cor azul-roxo muito escuro

    # A continuação desta função (corpo do vulcão, cratera, etc.) está omitida no trecho fornecido
    # mas seguiria o mesmo padrão: polígonos para as formas e elipses para a cratera
