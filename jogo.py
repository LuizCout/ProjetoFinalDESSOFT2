
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



#FUNÇÃO: desenhar_texto_arcade


def desenhar_texto_arcade(surface, fonte, texto, cor, contorno, x, y, espaco_extra=6):
    # Desenha um texto com estilo arcade letra por letra, permitindo espaçamento personalizado
    # Parâmetros: surface = onde desenhar | fonte = objeto de fonte do pygame | texto = string a exibir
    #             cor = cor da letra | contorno = cor do contorno | x, y = posição central | espaco_extra = pixels extras entre letras

    chars = list(texto)  # Converte a string em uma lista de caracteres individuais para iterar letra por letra

    # Calcula a largura total do texto somando a largura de cada caractere mais o espaço extra entre eles
    largura_total = sum(fonte.size(c)[0] + espaco_extra for c in chars) - espaco_extra  # Subtrai um espaço_extra para não adicionar após a última letra
    cx = x - largura_total // 2  # Calcula a posição x inicial para que o texto fique centralizado na posição x fornecida

    for c in chars:                     # Itera sobre cada caractere da lista
        w = fonte.size(c)[0]            # Obtém a largura em pixels do caractere atual

        # --- Desenha o contorno ---
        letra_contorno = fonte.render(c, True, contorno)  # Renderiza o caractere com a cor de contorno (antialiasing ativado)
        for dx in (-2, 0, 2):           # Itera nos deslocamentos horizontais: -2, 0 e 2 pixels
            for dy in (-2, 0, 2):       # Itera nos deslocamentos verticais: -2, 0 e 2 pixels
                if dx != 0 or dy != 0:  # Ignora a posição central (0,0) para não sobrescrever a letra principal
                    surface.blit(letra_contorno, (cx + dx, y + dy))  # Desenha o contorno deslocado em 8 posições ao redor da letra

        # --- Desenha a letra principal ---
        surface.blit(fonte.render(c, True, cor), (cx, y))  # Renderiza e desenha a letra na cor principal sobre o contorno
        cx += w + espaco_extra  # Avança a posição x para a próxima letra, somando a largura da letra atual mais o espaço extra


# FUNÇÃO: tela_inicio

 
def tela_inicio(): 
    # Exibe a tela inicial animada do jogo e aguarda o jogador pressionar ENTER para iniciar
 
    fontes = ["Courier New", "Consolas", "Lucida Console", "monospace"]  # Lista de fontes monoespaçadas com estilo arcade preferidas
    nomes = [f.lower() for f in pygame.font.get_fonts()]                 # Obtém a lista de todas as fontes instaladas no sistema e converte para minúsculas
 
    # Seleciona a primeira fonte da lista preferida que esteja disponível no sistema; usa "monospace" como fallback
    fonte_nome = next((f for f in fontes if f.lower() in nomes), "monospace")
 
    # Cria objetos de fonte com tamanhos específicos para cada parte da tela inicial
    fonte_titulo = pygame.font.SysFont(fonte_nome, 88, bold=True)   # Fonte grande para o título principal (88px, negrito)
    fonte_sub    = pygame.font.SysFont(fonte_nome, 30, bold=True)   # Fonte média para subtítulo ou instrução (30px, negrito)
    fonte_cred   = pygame.font.SysFont("arial", 20)                 # Fonte menor para os créditos dos desenvolvedores (Arial 20px)
    fonte_press  = pygame.font.SysFont(fonte_nome, 26, bold=True)   # Fonte para a mensagem "pressione ENTER" (26px, negrito)
 
    t = 0  # Inicializa o contador de tempo em zero; será incrementado a cada frame para controlar animações
 
    while True:              # Loop infinito da tela inicial; só sai quando o jogador pressionar ENTER
        CLOCK.tick(FPS)      # Limita a execução a 60 frames por segundo, mantendo o ritmo do jogo constante
        t += 1               # Incrementa o contador de tempo em 1 a cada frame, usado nas animações da tela
 
        for event in pygame.event.get():                           # Lê todos os eventos pendentes do pygame (teclado, mouse, fechar janela)
            if event.type == pygame.QUIT:                          # Verifica se o evento é o botão de fechar a janela
                pygame.quit()                                      # Encerra todos os módulos do pygame corretamente
                sys.exit()                                         # Termina o processo Python completamente
 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  # Verifica se uma tecla foi pressionada E se essa tecla é o ENTER
                return  # Sai da função tela_inicio(), retornando ao fluxo principal do programa para iniciar o jogo
 
        # A parte de desenho do fundo animado, título, botão e créditos está omitida no trecho fornecido
        # mas acontece aqui dentro do loop, antes do pygame.display.flip()

        # FUNÇÃO: tela_transicao


def tela_transicao(numero_fase):
    # Exibe uma tela intermediária entre fases mostrando o número da fase atual
    # O parâmetro numero_fase indica qual fase está começando

    while True:          # Loop infinito que mantém a tela de transição visível até o jogador pressionar ENTER
        CLOCK.tick(FPS)  # Limita a execução a 60 FPS para manter o jogo estável durante a transição

        for event in pygame.event.get():                           # Lê todos os eventos pygame disponíveis no momento
            if event.type == pygame.QUIT:                          # Verifica se o usuário clicou no botão de fechar a janela
                pygame.quit()                                      # Encerra todos os módulos do pygame
                sys.exit()                                         # Termina o programa Python

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  # Verifica se o ENTER foi pressionado
                return  # Sai da função de transição e retorna ao loop principal para iniciar a nova fase

        # Aqui seria desenhado o texto "FASE X" e "PREPARE-SE!" na tela
        pygame.display.flip()  # Atualiza a tela, exibindo tudo que foi desenhado neste frame


# EXECUÇÃO DA TELA INICIAL (antes de carregar o resto do jogo)


tela_inicio()  # Chama a função da tela inicial; o programa fica parado aqui até o jogador pressionar ENTER

#CARREGAMENTO DOS SPRITES E IMAGENS DO JOGO
sheet = pygame.image.load(r"C:\Users\rezen\Downloads\dinoCharactersVersion1.1\sheets\DinoSprites - doux.png").convert_alpha()
# Carrega a spritesheet do personagem dinossauro como superfície com transparência (canal alpha preservado)

barril_img = pygame.transform.scale(pygame.image.load(r"C:\Users\rezen\Downloads\Barrel 0011.png"), (40, 40))
# Carrega a imagem do barril e a redimensiona para 40x40 pixels

escada_img = pygame.transform.scale(pygame.image.load(r"C:\Users\rezen\Downloads\wood_set\ladder\28x128\1.png"), (50, 100))
# Carrega a imagem da escada e a redimensiona para 50x100 pixels

macaco_img = pygame.transform.scale(pygame.image.load(r"C:\Users\rezen\Downloads\enemy certo.png"), (90, 90)).convert_alpha()
# Carrega a imagem do inimigo (macaco), redimensiona para 90x90 pixels e converte preservando transparência

# DIVISÃO DA SPRITESHEET EM FRAMES DE ANIMAÇÃO
# ============================================================
 
FRAME_L, FRAME_A, NUM_FRAMES = 24, 24, 6
# Define: FRAME_L = largura de cada frame (24px), FRAME_A = altura de cada frame (24px), NUM_FRAMES = total de frames (6)
 
frames = []  # Cria uma lista vazia que vai armazenar os frames individuais do personagem
 
for i in range(NUM_FRAMES):                                      # Itera de 0 a 5, uma vez para cada frame da animação
    frame = pygame.Surface((FRAME_L, FRAME_A), pygame.SRCALPHA) # Cria uma superfície transparente de 24x24 para receber o frame recortado
 
    frame.blit(sheet, (0, 0), (i * FRAME_L, 0, FRAME_L, FRAME_A))
    # Copia da spritesheet (sheet) para a superfície (frame):
    # - Destino na superfície: (0, 0)
    # - Área de recorte na spritesheet: começa em (i * 24, 0), com tamanho 24x24
    # Cada iteração avança 24px horizontalmente, pegando o próximo frame
 
    frames.append(pygame.transform.scale(frame, (80, 80)))
    # Redimensiona o frame de 24x24 para 80x80 pixels e adiciona à lista de frames
 
frame_atual = 0    # Inicializa o índice do frame atual de animação em 0 (primeiro frame)
vel_anim    = 0.2  # Define a velocidade de troca entre frames (0.2 = avança 20% de um frame por tick)

# VARIÁVEIS PRINCIPAIS DO JOGADOR


fase_atual = 1  # Armazena o número da fase atual; começa em 1

player = pygame.Rect(650, 1330, 50, 50)
# Cria o retângulo de colisão do jogador na posição inicial x=650, y=1330, com tamanho 50x50 pixels

vel_x = 0  # Velocidade horizontal do jogador; positivo = direita, negativo = esquerda, zero = parado
vel_y = 0  # Velocidade vertical do jogador; positivo = caindo, negativo = subindo (pulando)

no_chao   = False  # Flag booleana: True se o jogador está em contato com uma plataforma abaixo dele
na_escada = False  # Flag booleana: True se o jogador está colidindo com uma escada


# CONSTANTES DE FÍSICA E MOVIMENTO

GRAVIDADE     = 0.6   # Aceleração da gravidade: somada à vel_y a cada frame quando o jogador está no ar
VEL_BASE      = 3     # Velocidade horizontal normal do jogador em pixels por frame
VEL_TURBINADA = 7     # Velocidade horizontal com o poder de turbo ativo em pixels por frame
VEL           = VEL_BASE  # Variável de velocidade atual; começa igual à velocidade base
PULO          = -7.5  # Velocidade vertical aplicada ao pular (negativa = para cima)
