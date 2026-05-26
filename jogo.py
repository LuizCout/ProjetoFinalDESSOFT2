
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

 #ESTADO DO JOGO

vidas     = 3  # Número de vidas do jogador; ao chegar a zero, o jogo termina
pontuacao = 0  # Pontuação acumulada pelo jogador ao longo do jogo


# VARIÁVEIS DOS PODERES


poder_vel_ativo  = False  # Flag que indica se o poder de velocidade (turbo) está ativo no momento
poder_vel_timer  = 0      # Contador regressivo em frames que controla a duração do turbo ativo
PODER_VEL_DURACAO = 300   # Duração total do turbo em frames (300 frames = 5 segundos a 60 FPS)

poder_bomb_ativo  = False  # Flag que indica se o poder bomba (destruição de barris) está ativo
poder_bomb_timer  = 0      # Contador regressivo em frames que controla a duração da bomba ativa
PODER_BOMB_DURACAO = 240   # Duração total da bomba em frames (240 frames = 4 segundos a 60 FPS)

# FUNÇÃO: criar_andares


def criar_andares():
    # Reconstrói toda a estrutura de plataformas e escadas da fase atual
    # Alterna o lado do buraco em cada andar, imitando a estrutura do Donkey Kong original

    andares.clear()    # Remove todos os andares existentes da lista
    plataformas.clear()  # Remove todas as plataformas existentes da lista
    escadas.clear()    # Remove todas as escadas existentes da lista

    y = 1350                    # Define a posição y do primeiro andar (mais baixo), perto do fundo do mundo
    lado_buraco_esquerda = False  # Controla qual lado tem o buraco; começa com buraco à direita

    for _ in range(12):  # Cria 12 andares empilhados verticalmente

        if fase_atual == 1:
            # Na fase 1 as plataformas são maiores (720px de largura)
            plat = pygame.Rect(80, y, 720, ESPESSURA) if lado_buraco_esquerda else pygame.Rect(0, y, 720, ESPESSURA)
            # Se o buraco está à esquerda, a plataforma começa em x=80; senão começa em x=0
        else:
            # Na fase 2 as plataformas são menores (620px), tornando o jogo mais difícil
            plat = pygame.Rect(130, y, 620, ESPESSURA) if lado_buraco_esquerda else pygame.Rect(0, y, 620, ESPESSURA)

        andares.append({"rect": plat, "y": y, "buraco_esquerda": lado_buraco_esquerda})
        # Adiciona um dicionário com o rect da plataforma, sua posição y e qual lado tem o buraco

        plataformas.append(plat)  # Adiciona o rect da plataforma também à lista simples usada para colisões

        y -= ALTURA_ANDAR                          # Sobe a posição y para o próximo andar (subtrai porque y aumenta para baixo)
        lado_buraco_esquerda = not lado_buraco_esquerda  # Alterna o lado do buraco para criar o padrão zigue-zague

    for i in range(len(andares) - 1):  # Itera pelos andares criando uma escada entre cada par de andares adjacentes
        baixo, cima = andares[i], andares[i + 1]  # Define andar inferior e andar superior do par atual

        x = 100 if i % 2 == 0 else 550 if fase_atual == 1 else 150 if i % 2 == 0 else 600
        # Posiciona a escada: nos andares pares à esquerda, nos ímpares à direita; valores diferentes por fase

        escadas.append(pygame.Rect(x, cima["y"], 30, baixo["y"] - cima["y"]))
        # Cria o rect da escada: começa no topo do andar superior, tem 30px de largura e vai até o andar inferior


 #FUNÇÃO: spawnar_itens


def spawnar_itens():
    # Distribui itens aleatoriamente pelos andares do cenário
    # Existem dois tipos de item: "velocidade" (turbo) e "bomba"

    itens.clear()  # Remove todos os itens existentes antes de criar novos

    indices = random.sample(range(1, len(andares) - 1), min(6, len(andares) - 2))
    # Seleciona aleatoriamente até 6 índices de andares (excluindo o primeiro e o último) para receber itens

    tipos = ["velocidade", "bomba"] * 10  # Cria uma lista com 10 pares alternados dos dois tipos de item
    random.shuffle(tipos)                  # Embaralha a lista de tipos para distribuição aleatória

    for i, idx in enumerate(indices):  # Itera pelos índices selecionados, com numeração (i) para acessar o tipo
        andar = andares[idx]           # Obtém o dicionário do andar correspondente ao índice sorteado
        x = random.randint(120, LARGURA - 120)  # Sorteia uma posição x aleatória dentro dos limites da tela
        y = andar["y"] - ITEM_RAIO * 2 - 4      # Calcula a posição y do item para ficar logo acima da plataforma

        itens.append({
            "rect":  pygame.Rect(x - ITEM_RAIO, y - ITEM_RAIO, ITEM_RAIO * 2, ITEM_RAIO * 2),
            # Cria o rect de colisão do item centralizado na posição (x, y) com tamanho igual ao diâmetro do item
            "tipo":  tipos[i % len(tipos)],  # Atribui o tipo do item acessando a lista embaralhada com índice circular
            "ativo": True,                   # Marca o item como ativo (visível e coletável)
            "pulso": random.uniform(0, 6.28),  # Define uma fase inicial aleatória para a animação de pulso (0 a 2π radianos)
        })
# FUNÇÃO: desenhar_item

def desenhar_item(item, cam_y):
    # Desenha um item na tela com animação de pulso (variação de tamanho)
    # Parâmetros: item = dicionário do item | cam_y = deslocamento vertical da câmera

    if not item["ativo"]:  # Se o item não está ativo (já foi coletado), encerra a função sem desenhar nada
        return

    item["pulso"] += 0.08  # Avança a fase da animação de pulso em 0.08 radianos por frame

    escala = 1.0 + 0.12 * abs(math.sin(item["pulso"]))
    # Calcula o fator de escala do item usando seno: varia entre 1.0 e 1.12, criando efeito de expansão e contração

    cx, cy = item["rect"].centerx, item["rect"].centery - cam_y
    # Obtém o centro horizontal do item e aplica o offset da câmera ao centro vertical

    # A parte de desenho (círculo azul para turbo, vermelho para bomba) está omitida no trecho fornecido


# FUNÇÃO: atualizar_camera


def atualizar_camera():
    # Calcula a posição vertical da câmera para seguir o jogador
    # Mantém o jogador próximo ao centro vertical da tela

    global camera_y  # Declara que vai modificar a variável global camera_y (não criar uma local)

    camera_y = player.y - ALTURA // 2
    # Posiciona a câmera para que o jogador fique no centro vertical da tela
    # Subtrai metade da altura da tela da posição y do jogador

    camera_y = max(0, min(camera_y, MUNDO_ALTURA - ALTURA))
    # Limita a câmera entre 0 e (MUNDO_ALTURA - ALTURA) para não mostrar além dos limites do mundo


# FUNÇÃO: resetar


def resetar():
    # Reposiciona o jogador no início do primeiro andar e limpa os barris da tela
    # Chamada ao perder uma vida ou avançar de fase

    global vel_x, vel_y, barris  # Declara que vai modificar as variáveis globais vel_x, vel_y e barris

    player.x = andares[0]["rect"].x + 50  # Reposiciona o jogador horizontalmente: início do primeiro andar + 50px
    player.y = andares[0]["y"] - player.height - 5
    # Reposiciona o jogador verticalmente logo acima da superfície do primeiro andar

    vel_x = 0  # Zera a velocidade horizontal para o jogador começar parado
    vel_y = 0  # Zera a velocidade vertical para o jogador não continuar caindo

    barris.clear()  # Remove todos os barris da tela para evitar colisão imediata ao respawnar


# FUNÇÃO: spawn_barril


def spawn_barril():
    # Cria um novo barril na posição do inimigo no topo do cenário
    # Na fase 2 há maior chance de barris rápidos, aumentando a dificuldade

    topo = andares[-1]  # Obtém o dicionário do andar mais alto (último da lista, que é o topo do cenário)

    chance_rapido = 0.3 if fase_atual == 1 else 0.55
    # Define 30% de chance de barril rápido na fase 1 e 55% na fase 2

    tipo = "rapido" if random.random() < chance_rapido else "normal"
    # Sorteia o tipo do barril: "rapido" se o número aleatório (0.0-1.0) for menor que a chance; senão "normal"

    barris.append({
        "rect": pygame.Rect(macaco_pos[0], topo["y"] - 40, 20, 20),
        # Cria o rect do barril na posição x do macaco, logo acima do andar do topo, com tamanho 20x20 pixels
        "dir": -1,   # Define direção inicial do barril como -1 (movendo para a esquerda)
        "tipo": tipo  # Armazena o tipo do barril ("rapido" ou "normal") no dicionário
    })


# FUNÇÃO: avancar_fase

    # Incrementa a fase atual e configura o jogo para a nova fase
    # Se ultrapassar a fase 2, exibe a tela de vitória e encerra o jogo

    global fase_atual, barris, macaco_pos, objetivo, tempo_spawn  # Declara variáveis globais que serão modificadas
    global poder_vel_ativo, poder_vel_timer, poder_bomb_ativo, poder_bomb_timer  # Mais variáveis globais de poder
    global item_respawn_timer  # Variável global do timer de reaparecimento de itens

    fase_atual += 1  # Incrementa o número da fase em 1

    if fase_atual > 2:    # Verifica se passou da última fase disponível (fase 2)
        tela_vitoria()    # Exibe a tela de vitória com a pontuação final
        pygame.quit()     # Encerra todos os módulos do pygame
        sys.exit()        # Finaliza o programa Python

    # Reseta todos os timers e poderes para o estado inicial da nova fase
    tempo_spawn         = 0      # Zera o contador de spawn de barris
    item_respawn_timer  = 0      # Zera o timer de reaparecimento de itens
    poder_vel_ativo     = False  # Desativa o poder de velocidade
    poder_vel_timer     = 0      # Zera o timer do poder de velocidade
    poder_bomb_ativo    = False  # Desativa o poder bomba
    poder_bomb_timer    = 0      # Zera o timer do poder bomba

    criar_andares()   # Reconstrói as plataformas e escadas com as configurações da nova fase
    spawnar_itens()   # Distribui novos itens pelos andares da nova fase

    resetar()         # Reposiciona o jogador e limpa os barris
    barris.clear()    # Garante que a lista de barris esteja completamente vazia (redundância de segurança)

    tela_transicao(fase_atual)  # Exibe a tela de transição com o número da nova fase antes de continuar

# LOOP PRINCIPAL DO JOGO
# ============================================================
# Este bloco roda continuamente enquanto o jogo estiver ativo.
# A cada iteração (frame): lê eventos, processa inputs, atualiza
# física, verifica colisões, e renderiza tudo na tela.
 
tempo_spawn = 0  # Inicializa o contador de tempo para controlar o intervalo entre spawns de barris
 
while True:          # Loop infinito que mantém o jogo rodando até o programa ser encerrado
    CLOCK.tick(FPS)  # Aguarda o tempo necessário para manter exatamente 60 frames por segundo
 
    fundo_atual = fundo_img if fase_atual == 1 else fundo_fase2
    # Seleciona qual imagem de fundo usar: fase 1 usa fundo_img, fase 2 usa fundo_fase2
 
    TELA.blit(fundo_atual, (0, 0))  # Desenha o fundo selecionado na tela a partir da posição (0,0), cobrindo toda a janela
 
    for event in pygame.event.get():          # Lê e processa todos os eventos disponíveis na fila do pygame
        if event.type == pygame.QUIT:         # Verifica se o evento é o fechamento da janela
            pygame.quit()                     # Encerra todos os módulos do pygame
            sys.exit()                        # Termina o processo Python
 
    teclas = pygame.key.get_pressed()  # Captura o estado atual de todas as teclas (True se pressionada, False se não)
 
    VEL = VEL_TURBINADA if poder_vel_ativo else VEL_BASE
    # Define a velocidade atual: usa velocidade turbinada (7) se o turbo estiver ativo, senão usa a base (3)

    # ============================================================
    # MOVIMENTO HORIZONTAL DO JOGADOR
    # ============================================================

    vel_x = 0  # Zera a velocidade horizontal a cada frame para que o jogador pare ao soltar a tecla

    if teclas[pygame.K_LEFT]:   # Verifica se a tecla seta esquerda está pressionada
        vel_x = -VEL            # Define velocidade horizontal negativa (move para a esquerda)

    if teclas[pygame.K_RIGHT]:  # Verifica se a tecla seta direita está pressionada
        vel_x = VEL             # Define velocidade horizontal positiva (move para a direita)

    # ============================================================
    # DETECÇÃO DE ESCADA
    # ============================================================

    na_escada = any(player.colliderect(e) for e in escadas)
    # Verifica se o rect do jogador colide com qualquer escada da lista; retorna True se colidir com ao menos uma

    if na_escada:   # Se o jogador estiver em contato com uma escada
        vel_y = 0   # Zera a velocidade vertical para neutralizar a gravidade enquanto está na escada

        if teclas[pygame.K_UP]:    # Verifica se a seta para cima está pressionada
            vel_y = -VEL           # Move o jogador para cima na escada com a velocidade atual

        if teclas[pygame.K_DOWN]:  # Verifica se a seta para baixo está pressionada
            vel_y = VEL            # Move o jogador para baixo na escada com a velocidade atual

    else:               # Se o jogador NÃO está em uma escada
        vel_y += GRAVIDADE  # Aplica a gravidade: acumula velocidade para baixo a cada frame

    # ============================================================
    # PULO
    # ============================================================

    if teclas[pygame.K_SPACE] and no_chao and not na_escada:
    # Verifica: tecla espaço pressionada E jogador está no chão E jogador não está na escada
        vel_y = PULO  # Aplica a velocidade de pulo (-7.5), lançando o jogador para cima

    # ============================================================
    # ATUALIZAÇÃO DA POSIÇÃO DO JOGADOR
    # ============================================================

    player.x += vel_x        # Move o jogador horizontalmente somando a velocidade horizontal ao x atual
    player.y += int(vel_y)   # Move o jogador verticalmente somando a velocidade vertical (convertida para inteiro) ao y atual

    player.x = max(0, min(player.x, LARGURA - player.width))
    # Limita a posição x do jogador entre 0 e (LARGURA - largura do jogador) para não sair pelos lados da tela

    # ============================================================
    # COLISÃO COM PLATAFORMAS (por cima)
    # ============================================================

    no_chao = False  # Assume que o jogador está no ar até que uma colisão prove o contrário

    for plat in plataformas:                          # Itera por todas as plataformas do cenário
        if player.colliderect(plat) and vel_y > 0:   # Verifica colisão com a plataforma E se o jogador está caindo
            player.bottom = plat.top                  # Alinha o fundo do jogador com o topo da plataforma (pousa sobre ela)
            vel_y = 0                                 # Zera a velocidade vertical, parando a queda
            no_chao = True                            # Marca que o jogador está no chão

    # COLISÃO COM PLATAFORMAS (por baixo - batida na cabeça)
    # ============================================================
 
    if not na_escada:                                     # Só verifica batida na cabeça se não estiver na escada
        for plat in plataformas:                          # Itera por todas as plataformas
            if player.colliderect(plat) and vel_y < 0:   # Colisão com plataforma E jogador subindo (vel_y negativa)
                player.top = plat.bottom                  # Alinha o topo do jogador com o fundo da plataforma (bate a cabeça)
                vel_y = 0                                 # Zera a velocidade vertical, impedindo de continuar subindo
 
    # ============================================================
    # TIMERS DOS PODERES
    # ============================================================
 
    if poder_vel_ativo:           # Verifica se o poder de velocidade está ativo
        poder_vel_timer -= 1      # Decrementa o timer do turbo em 1 frame por iteração
        if poder_vel_timer <= 0:  # Quando o timer chegar a zero
            poder_vel_ativo = False  # Desativa o poder de velocidade
 
    if poder_bomb_ativo:           # Verifica se o poder bomba está ativo
        poder_bomb_timer -= 1      # Decrementa o timer da bomba em 1 frame por iteração
        if poder_bomb_timer <= 0:  # Quando o timer chegar a zero
            poder_bomb_ativo = False  # Desativa o poder bomba
 

    # COLETA DE ITENS
    
 
    for item in itens:                                     # Itera por todos os itens do cenário
        if item["ativo"] and player.colliderect(item["rect"]):
        # Verifica se o item está ativo E se o jogador colide com ele
 
            item["ativo"] = False  # Marca o item como inativo (coletado), impedindo que seja coletado novamente
 
            if item["tipo"] == "velocidade":         # Verifica se o item coletado é do tipo velocidade
                poder_vel_ativo = True               # Ativa o poder de velocidade
                poder_vel_timer = PODER_VEL_DURACAO  # Inicia o timer com a duração total do turbo
            else:                                    # Se não for velocidade, é bomba
                poder_bomb_ativo = True              # Ativa o poder bomba
                poder_bomb_timer = PODER_BOMB_DURACAO  # Inicia o timer com a duração total da bomba
    
    #SPAWN DE BARRIS
   

    intervalo_spawn = max(40, 120 - pontuacao // 10) if fase_atual == 1 else max(25, 90 - pontuacao // 10)
    # Calcula o intervalo entre spawns de barris: diminui conforme a pontuação aumenta (mais difícil)
    # Fase 1: mínimo de 40 frames; Fase 2: mínimo de 25 frames

    tempo_spawn += 1  # Incrementa o contador de tempo desde o último spawn em 1 frame

    if tempo_spawn > intervalo_spawn:  # Verifica se o intervalo de spawn foi atingido
        spawn_barril()    # Cria um novo barril na posição do inimigo
        tempo_spawn = 0   # Reinicia o contador de tempo para o próximo spawn

    
    # MOVIMENTAÇÃO DOS BARRIS
    

    for b in barris:       # Itera por cada barril presente na lista
        barril = b["rect"] # Obtém o rect do barril atual para facilitar o acesso

        if fase_atual == 1:
            velocidade = 6 if b["tipo"] == "rapido" else 3 + pontuacao // 200
            # Fase 1: barris rápidos movem a 6px/frame; normais têm velocidade crescente com a pontuação
        else:
            velocidade = 7 if b["tipo"] == "rapido" else 5 + pontuacao // 150
            # Fase 2: barris rápidos movem a 7px/frame; normais têm velocidade crescente mais agressiva

        barril.x += velocidade * b["dir"]  # Move o barril horizontalmente: velocidade * direção (-1 ou 1)
        barril.y += 5                      # Move o barril 5 pixels para baixo a cada frame (desce gradualmente)

        if random.random() < 0.01:  # Com 1% de chance a cada frame
            b["dir"] *= -1          # Inverte a direção horizontal do barril multiplicando por -1

    
    # COLISÃO DOS BARRIS COM O JOGADOR
    

    if barril.colliderect(player):       # Verifica se o barril atual colide com o rect do jogador
        if poder_bomb_ativo:             # Verifica se o poder bomba está ativo
            barris_remover.append(b)     # Adiciona o barril à lista de barris a serem removidos (destruído pela bomba)
            pontuacao += 10              # Adiciona 10 pontos por destruir o barril com a bomba
        else:                            # Se o poder bomba não está ativo
            vidas -= 1                   # Subtrai uma vida do jogador
            resetar()                    # Reposiciona o jogador e limpa os barris

            if vidas <= 0:               # Verifica se o jogador ficou sem vidas
                tela_game_over()         # Exibe a tela de game over
                pygame.quit()            # Encerra o pygame
                sys.exit()               # Termina o programa
 
# ============================================================
    # HUD (interface do usuário na tela)
    # ============================================================

    texto     = fonte.render(f"Pontuação: {pontuacao}", True, BRANCO)
    # Renderiza o texto de pontuação com o valor atual em cor branca com antialiasing ativado

    vidas_txt = fonte.render(f"Vidas: {vidas}", True, BRANCO)
    # Renderiza o texto de vidas com o valor atual em cor branca

    fase_txt  = fonte.render(f"Fase: {fase_atual}", True, AMARELO)
    # Renderiza o texto de fase com o número atual em cor amarela

    TELA.blit(texto, (x_pont, 10))
    # Desenha o texto de pontuação na tela na posição x_pont, 10 pixels do topo

    TELA.blit(vidas_txt, (10, 10))
    # Desenha o texto de vidas na tela no canto superior esquerdo (x=10, y=10)

    TELA.blit(fase_txt, (LARGURA // 2 - fase_txt.get_width() // 2, 10))
    # Desenha o texto de fase centralizado horizontalmente na tela, 10 pixels do topo

    # ============================================================
    # ATUALIZAÇÃO FINAL DA TELA
    # ============================================================

    pygame.display.flip()
    # Atualiza toda a janela com o conteúdo desenhado neste frame (exibe o frame ao jogador)