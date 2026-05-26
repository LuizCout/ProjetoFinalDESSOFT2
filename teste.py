import pygame
import sys
import random
import math

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\rezen\Downloads\hard_boss_battle_1_bpm200.ogg")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

LARGURA, ALTURA = 900, 800
MUNDO_ALTURA = 1400

TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Dino Barrel")

CLOCK = pygame.time.Clock()
FPS = 60

fundo_img = pygame.image.load(r"C:\Users\rezen\Downloads\fundogame.jpg").convert()
fundo_img = pygame.transform.scale(fundo_img, (LARGURA, ALTURA))

fundo_fase2 = pygame.image.load(r"C:\Users\rezen\Downloads\fase final.webp").convert()
fundo_fase2 = pygame.transform.scale(fundo_fase2, (LARGURA, ALTURA))

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA_ESC = (30, 30, 30)
AMARELO = (255, 220, 0)
VERMELHO = (220, 50, 50)
AZUL_CLARO = (80, 180, 255)
LARANJA = (255, 120, 30)
LARANJA_ESC = (200, 80, 10)
CINZA_PEDRA = (90, 85, 80)
CINZA_PEDRA2 = (120, 110, 100)
VERMELHO_LAVA = (255, 60, 0)
AMARELO_LAVA = (255, 200, 0)

def desenhar_vulcao(surface, t):
    surface.fill((15, 10, 30))
    random.seed(42)
    for _ in range(120):
        sx = random.randint(0, LARGURA)
        sy = random.randint(0, int(ALTURA * 0.55))
        brilho = 100 + int(60 * abs(math.sin(t * 0.03 + sx)))
        pygame.draw.circle(surface, (brilho, brilho, brilho), (sx, sy), 1)
    random.seed()
    montanha = [(0, ALTURA), (0, 500), (150, 320), (280, 420), (400, 200),
                (520, 380), (650, 290), (800, 430), (900, 380), (900, ALTURA)]
    pygame.draw.polygon(surface, (25, 20, 40), montanha)
    vx, vy_base, vy_topo = 450, ALTURA, 260
    largura_base, largura_topo = 380, 90
    vulcao = [(vx - largura_base // 2, vy_base), (vx - largura_topo // 2, vy_topo),
              (vx + largura_topo // 2, vy_topo), (vx + largura_base // 2, vy_base)]
    pygame.draw.polygon(surface, CINZA_PEDRA, vulcao)
    lado_claro = [(vx - largura_base // 2, vy_base), (vx - largura_topo // 2, vy_topo),
                  (vx - largura_topo // 2 + 30, vy_topo + 30), (vx - largura_base // 2 + 60, vy_base)]
    pygame.draw.polygon(surface, CINZA_PEDRA2, lado_claro)
    cratera_y = vy_topo + 10
    pygame.draw.ellipse(surface, (50, 20, 10), (vx - largura_topo // 2 - 10, cratera_y - 18, largura_topo + 20, 36))
    for lado in (-1, 1):
        for i in range(3):
            lx = vx + lado * (largura_topo // 2 - 10 + i * 12)
            for seg in range(8):
                seg_y = vy_topo + 20 + seg * 35
                cor = VERMELHO_LAVA if seg % 2 == 0 else AMARELO_LAVA
                pts = [(lx + lado * seg * 3, seg_y), (lx + lado * (seg * 3 + 8), seg_y + 18), (lx + lado * (seg * 3 + 4), seg_y + 35)]
                pygame.draw.lines(surface, cor, False, pts, 4)
    for i in range(14):
        angulo = -math.pi / 2 + math.sin(t * 0.05 + i * 0.8) * 0.6
        velocidade = 3 + (i % 5) * 0.8
        px = int(vx + math.cos(angulo) * velocidade * ((t % 40) + i * 5) % 120)
        py = int(cratera_y - 10 - (t * 2 + i * 18) % 180)
        if py <= cratera_y:
            cor = AMARELO_LAVA if i % 2 == 0 else VERMELHO_LAVA
            pygame.draw.circle(surface, cor, (px, py), max(1, 4 - (i % 3)))
    for i in range(5):
        sx = vx + int(math.sin(t * 0.04 + i * 1.2) * 20)
        sy = cratera_y - 30 - (t * 1.5 + i * 22) % 100
        if sy >= cratera_y - 130:
            raio = 12 + i * 4
            fuma = pygame.Surface((raio * 2, raio * 2), pygame.SRCALPHA)
            alfa = max(0, 180 - int((cratera_y - 30 - sy) * 1.5))
            pygame.draw.circle(fuma, (80, 70, 70, alfa), (raio, raio), raio)
            surface.blit(fuma, (sx - raio, int(sy) - raio))
    for i in range(6):
        rx = vx - 180 + i * 70 + int(math.sin(t * 0.03 + i) * 10)
        ry = ALTURA - 20 - (i % 3) * 8
        pygame.draw.ellipse(surface, (180 + i * 10, 40 + i * 5, 0), (rx, ry, 50 - i * 4, 12))

def desenhar_texto_arcade(surface, fonte, texto, cor, contorno, x, y, espaco_extra=6):
    chars = list(texto)
    largura_total = sum(fonte.size(c)[0] + espaco_extra for c in chars) - espaco_extra
    cx = x - largura_total // 2
    for c in chars:
        w = fonte.size(c)[0]
        letra_contorno = fonte.render(c, True, contorno)
        for dx in (-2, 0, 2):
            for dy in (-2, 0, 2):
                if dx != 0 or dy != 0:
                    surface.blit(letra_contorno, (cx + dx, y + dy))
        surface.blit(fonte.render(c, True, cor), (cx, y))
        cx += w + espaco_extra

def tela_inicio():
    fontes = ["Courier New", "Consolas", "Lucida Console", "monospace"]
    nomes = [f.lower() for f in pygame.font.get_fonts()]
    fonte_nome = next((f for f in fontes if f.lower() in nomes), "monospace")
    fonte_titulo = pygame.font.SysFont(fonte_nome, 88, bold=True)
    fonte_sub = pygame.font.SysFont(fonte_nome, 30, bold=True)
    fonte_cred = pygame.font.SysFont("arial", 20)
    fonte_press = pygame.font.SysFont(fonte_nome, 26, bold=True)
    t = 0
    while True:
        CLOCK.tick(FPS)
        t += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return
        desenhar_vulcao(TELA, t)
        painel = pygame.Surface((700, 320), pygame.SRCALPHA)
        painel.fill((0, 0, 0, 160))
        TELA.blit(painel, (100, 100))
        desenhar_texto_arcade(TELA, fonte_titulo, "DINO BARREL", AMARELO, (160, 60, 0), LARGURA // 2, 118, 8)
        desenhar_texto_arcade(TELA, fonte_sub, "- HARD MODE -", VERMELHO, (80, 10, 10), LARGURA // 2, 228, 4)
        for bx in (LARGURA // 2 - 130, LARGURA // 2 + 100):
            pygame.draw.rect(TELA, LARANJA, (bx, 280, 30, 30), border_radius=6)
            pygame.draw.rect(TELA, CINZA_PEDRA, (bx, 280, 30, 30), 2, border_radius=6)
        pygame.draw.line(TELA, LARANJA_ESC, (200, 325), (700, 325), 2)
        cor_enter = BRANCO if (t // 30) % 2 == 0 else AMARELO
        contorno = (40, 40, 40) if cor_enter == BRANCO else (100, 60, 0)
        desenhar_texto_arcade(TELA, fonte_press, "[ ENTER ] PARA JOGAR", cor_enter, contorno, LARGURA // 2, 358, 3)
        y = ALTURA - 70
        for linha in ["Criado por:", "Luiz Coutinho  •  Felipe Mastandrea  •  João Tristão"]:
            txt = fonte_cred.render(linha, True, (180, 170, 160))
            TELA.blit(txt, (LARGURA // 2 - txt.get_width() // 2, y))
            y += 28
        pygame.display.flip()

def tela_transicao(numero_fase):
    fontes = ["Courier New", "Consolas", "Lucida Console", "monospace"]
    nomes = [f.lower() for f in pygame.font.get_fonts()]
    fonte_nome = next((f for f in fontes if f.lower() in nomes), "monospace")
    fonte_grande = pygame.font.SysFont(fonte_nome, 72, bold=True)
    fonte_media = pygame.font.SysFont(fonte_nome, 32, bold=True)
    fonte_press = pygame.font.SysFont(fonte_nome, 24, bold=True)
    t = 0
    while True:
        CLOCK.tick(FPS)
        t += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return
        TELA.fill((10, 10, 20))
        painel = pygame.Surface((700, 300), pygame.SRCALPHA)
        painel.fill((0, 0, 0, 180))
        TELA.blit(painel, (100, 220))
        desenhar_texto_arcade(TELA, fonte_grande, f"FASE {numero_fase}", AMARELO, (120, 60, 0), LARGURA // 2, 250, 6)
        desenhar_texto_arcade(TELA, fonte_media, "PREPARE-SE!", BRANCO, (40, 40, 40), LARGURA // 2, 360, 4)
        cor_enter = BRANCO if (t // 30) % 2 == 0 else AMARELO
        desenhar_texto_arcade(TELA, fonte_press, "[ ENTER ] PARA CONTINUAR", cor_enter, (40, 40, 40), LARGURA // 2, 430, 3)
        pygame.display.flip()

tela_inicio()

sheet = pygame.image.load(r"C:\Users\rezen\Downloads\dinoCharactersVersion1.1\sheets\DinoSprites - doux.png").convert_alpha()
barril_img = pygame.transform.scale(pygame.image.load(r"C:\Users\rezen\Downloads\Barrel 0011.png"), (40, 40))
escada_img = pygame.transform.scale(pygame.image.load(r"C:\Users\rezen\Downloads\wood_set\ladder\28x128\1.png"), (50, 100))
macaco_img = pygame.transform.scale(pygame.image.load(r"C:\Users\rezen\Downloads\enemy certo.png"), (90, 90)).convert_alpha()

FRAME_L, FRAME_A, NUM_FRAMES = 24, 24, 6
frames = []
for i in range(NUM_FRAMES):
    frame = pygame.Surface((FRAME_L, FRAME_A), pygame.SRCALPHA)
    frame.blit(sheet, (0, 0), (i * FRAME_L, 0, FRAME_L, FRAME_A))
    frames.append(pygame.transform.scale(frame, (80, 80)))

frame_atual = 0
vel_anim = 0.2

fase_atual = 1

player = pygame.Rect(650, 1330, 50, 50)
vel_x = 0
vel_y = 0
no_chao = False
na_escada = False
GRAVIDADE = 0.6
VEL_BASE = 3
VEL_TURBINADA = 7
VEL = VEL_BASE
PULO = -7.5
vidas = 3
pontuacao = 0

poder_vel_ativo = False
poder_vel_timer = 0
PODER_VEL_DURACAO = 300
poder_bomb_ativo = False
poder_bomb_timer = 0
PODER_BOMB_DURACAO = 240

ITEM_RAIO = 18
ITEM_RESPAWN_INTERVALO = 600
itens = []
item_respawn_timer = 0

andares, plataformas, escadas = [], [], []
ALTURA_ANDAR = 115
ESPESSURA = 8

fonte = pygame.font.SysFont("arial", 28, bold=True)
fonte_pow = pygame.font.SysFont("arial", 22, bold=True)

def criar_andares():
    andares.clear()
    plataformas.clear()
    escadas.clear()
    y = 1350
    lado_buraco_esquerda = False
    for _ in range(12):
        if fase_atual == 1:
            plat = pygame.Rect(80, y, 720, ESPESSURA) if lado_buraco_esquerda else pygame.Rect(0, y, 720, ESPESSURA)
        else:
            plat = pygame.Rect(130, y, 620, ESPESSURA) if lado_buraco_esquerda else pygame.Rect(0, y, 620, ESPESSURA)
        andares.append({"rect": plat, "y": y, "buraco_esquerda": lado_buraco_esquerda})
        plataformas.append(plat)
        y -= ALTURA_ANDAR
        lado_buraco_esquerda = not lado_buraco_esquerda
    for i in range(len(andares) - 1):
        baixo, cima = andares[i], andares[i + 1]
        if fase_atual == 1:
            x = 100 if i % 2 == 0 else 550
        else:
            x = 150 if i % 2 == 0 else 600
        escadas.append(pygame.Rect(x, cima["y"], 30, baixo["y"] - cima["y"]))

criar_andares()

def spawnar_itens():
    itens.clear()
    indices = random.sample(range(1, len(andares) - 1), min(6, len(andares) - 2))
    tipos = ["velocidade", "bomba"] * 10
    random.shuffle(tipos)
    for i, idx in enumerate(indices):
        andar = andares[idx]
        x = random.randint(120, LARGURA - 120)
        y = andar["y"] - ITEM_RAIO * 2 - 4
        itens.append({
            "rect": pygame.Rect(x - ITEM_RAIO, y - ITEM_RAIO, ITEM_RAIO * 2, ITEM_RAIO * 2),
            "tipo": tipos[i % len(tipos)],
            "ativo": True,
            "pulso": random.uniform(0, 6.28),
        })

spawnar_itens()

def desenhar_item(item, cam_y):
    if not item["ativo"]:
        return
    item["pulso"] += 0.08
    escala = 1.0 + 0.12 * abs(math.sin(item["pulso"]))
    r = int(ITEM_RAIO * escala)
    cx, cy = item["rect"].centerx, item["rect"].centery - cam_y
    cor = AZUL_CLARO if item["tipo"] == "velocidade" else VERMELHO
    cor_bg = (20, 60, 120) if item["tipo"] == "velocidade" else (100, 20, 20)
    pygame.draw.circle(TELA, cor_bg, (cx, cy), r + 4)
    pygame.draw.circle(TELA, cor, (cx, cy), r)
    pygame.draw.circle(TELA, BRANCO, (cx, cy), r, 2)
    simbolo = ">>" if item["tipo"] == "velocidade" else "*"
    txt = fonte_pow.render(simbolo, True, BRANCO)
    TELA.blit(txt, (cx - txt.get_width() // 2, cy - txt.get_height() // 2))

def desenhar_barra_poder(nome, timer, duracao, cor, pos_y):
    bx, by, bw, bh = 10, pos_y, 220, 22
    prog = timer / duracao
    pygame.draw.rect(TELA, CINZA_ESC, (bx, by, bw, bh), border_radius=6)
    pygame.draw.rect(TELA, cor, (bx, by, int(bw * prog), bh), border_radius=6)
    pygame.draw.rect(TELA, BRANCO, (bx, by, bw, bh), 2, border_radius=6)
    TELA.blit(fonte_pow.render(nome, True, BRANCO), (bx + 6, by + 2))

macaco_pos = (500, andares[-1]["y"] - macaco_img.get_height())
barris = []
objetivo = pygame.Rect(500, andares[-1]["y"] - 50, 50, 50)

def spawn_barril():
    topo = andares[-1]
    chance_rapido = 0.3 if fase_atual == 1 else 0.55
    tipo = "rapido" if random.random() < chance_rapido else "normal"
    barris.append({"rect": pygame.Rect(macaco_pos[0], topo["y"] - 40, 20, 20), "dir": -1, "tipo": tipo})

camera_y = 0

def atualizar_camera():
    global camera_y
    camera_y = player.y - ALTURA // 2
    camera_y = max(0, min(camera_y, MUNDO_ALTURA - ALTURA))

def resetar():
    global vel_x, vel_y, barris
    player.x = andares[0]["rect"].x + 50
    player.y = andares[0]["y"] - player.height - 5
    vel_x = 0
    vel_y = 0
    barris.clear()

# =========================
# TELA DE GAME OVER
# =========================
def tela_game_over():
    fontes = ["Courier New", "Consolas", "Lucida Console", "monospace"]
    nomes = [f.lower() for f in pygame.font.get_fonts()]
    fonte_nome = next((f for f in fontes if f.lower() in nomes), "monospace")
    fonte_grande = pygame.font.SysFont(fonte_nome, 80, bold=True)
    fonte_media = pygame.font.SysFont(fonte_nome, 30, bold=True)
    fonte_press = pygame.font.SysFont(fonte_nome, 24, bold=True)
    t = 0
    while True:
        CLOCK.tick(FPS)
        t += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
        TELA.fill((20, 0, 0))
        painel = pygame.Surface((700, 320), pygame.SRCALPHA)
        painel.fill((0, 0, 0, 180))
        TELA.blit(painel, (100, 200))
        desenhar_texto_arcade(TELA, fonte_grande, "GAME OVER", VERMELHO, (80, 0, 0), LARGURA // 2, 230, 6)
        desenhar_texto_arcade(TELA, fonte_media, f"Pontuacao Final: {pontuacao}", BRANCO, (40, 40, 40), LARGURA // 2, 360, 4)
        cor_enter = BRANCO if (t // 30) % 2 == 0 else VERMELHO
        desenhar_texto_arcade(TELA, fonte_press, "[ ENTER ] PARA SAIR", cor_enter, (40, 40, 40), LARGURA // 2, 430, 3)
        pygame.display.flip()

# =========================
# TELA DE VITORIA
# =========================
def tela_vitoria():
    fontes = ["Courier New", "Consolas", "Lucida Console", "monospace"]
    nomes = [f.lower() for f in pygame.font.get_fonts()]
    fonte_nome = next((f for f in fontes if f.lower() in nomes), "monospace")
    fonte_grande = pygame.font.SysFont(fonte_nome, 80, bold=True)
    fonte_media = pygame.font.SysFont(fonte_nome, 30, bold=True)
    t = 0
    while True:
        CLOCK.tick(FPS)
        t += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
        TELA.fill((10, 10, 20))
        desenhar_texto_arcade(TELA, fonte_grande, "VOCE VENCEU!", AMARELO, (120, 60, 0), LARGURA // 2, 280, 6)
        desenhar_texto_arcade(TELA, fonte_media, f"Pontuacao Final: {pontuacao}", BRANCO, (40, 40, 40), LARGURA // 2, 400, 4)
        pygame.display.flip()

def avancar_fase():
    global fase_atual, barris, macaco_pos, objetivo, tempo_spawn
    global poder_vel_ativo, poder_vel_timer, poder_bomb_ativo, poder_bomb_timer
    global item_respawn_timer

    fase_atual += 1

    if fase_atual > 2:
        tela_vitoria()
        pygame.quit()
        sys.exit()

    tempo_spawn = 0
    item_respawn_timer = 0
    poder_vel_ativo = False
    poder_vel_timer = 0
    poder_bomb_ativo = False
    poder_bomb_timer = 0

    criar_andares()
    spawnar_itens()

    macaco_pos = (500, andares[-1]["y"] - macaco_img.get_height())
    objetivo = pygame.Rect(500, andares[-1]["y"] - 50, 50, 50)

    resetar()
    barris.clear()

    tela_transicao(fase_atual)

# =========================
# LOOP PRINCIPAL
# =========================
tempo_spawn = 0
while True:
    CLOCK.tick(FPS)

    fundo_atual = fundo_img if fase_atual == 1 else fundo_fase2
    parallax_y = int(camera_y * 0) % ALTURA
    TELA.blit(fundo_atual, (0, -parallax_y))
    TELA.blit(fundo_atual, (0, ALTURA - parallax_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    VEL = VEL_TURBINADA if poder_vel_ativo else VEL_BASE

    vel_x = 0
    if teclas[pygame.K_LEFT]:
        vel_x = -VEL
    if teclas[pygame.K_RIGHT]:
        vel_x = VEL

    na_escada = any(player.colliderect(e) for e in escadas)

    if na_escada:
        vel_y = 0
        if teclas[pygame.K_UP]:
            vel_y = -VEL
        if teclas[pygame.K_DOWN]:
            vel_y = VEL
    else:
        vel_y += GRAVIDADE

    if teclas[pygame.K_SPACE] and no_chao and not na_escada:
        vel_y = PULO

    player.x += vel_x
    player.y += int(vel_y)
    player.x = max(0, min(player.x, LARGURA - player.width))

    no_chao = False
    for plat in plataformas:
        if player.colliderect(plat) and vel_y > 0:
            player.bottom = plat.top
            vel_y = 0
            no_chao = True

    if not na_escada:
        for plat in plataformas:
            if player.colliderect(plat) and vel_y < 0:
                player.top = plat.bottom
                vel_y = 0

    atualizar_camera()

    if poder_vel_ativo:
        poder_vel_timer -= 1
        if poder_vel_timer <= 0:
            poder_vel_ativo = False
    if poder_bomb_ativo:
        poder_bomb_timer -= 1
        if poder_bomb_timer <= 0:
            poder_bomb_ativo = False

    for item in itens:
        if item["ativo"] and player.colliderect(item["rect"]):
            item["ativo"] = False
            if item["tipo"] == "velocidade":
                poder_vel_ativo = True
                poder_vel_timer = PODER_VEL_DURACAO
            else:
                poder_bomb_ativo = True
                poder_bomb_timer = PODER_BOMB_DURACAO

    item_respawn_timer += 1
    if item_respawn_timer >= ITEM_RESPAWN_INTERVALO:
        item_respawn_timer = 0
        for item in itens:
            if not item["ativo"]:
                item["ativo"] = True

    movendo = vel_x != 0 or vel_y != 0
    frame_atual = (frame_atual + vel_anim) % len(frames) if movendo else 0
    sprite = frames[int(frame_atual)]
    if vel_x < 0:
        sprite = pygame.transform.flip(sprite, True, False)

    intervalo_spawn = max(40, 120 - pontuacao // 10) if fase_atual == 1 else max(25, 90 - pontuacao // 10)
    tempo_spawn += 1
    if tempo_spawn > intervalo_spawn:
        spawn_barril()
        tempo_spawn = 0

    barris_remover = []
    for b in barris:
        barril = b["rect"]
        if fase_atual == 1:
            velocidade = 6 if b["tipo"] == "rapido" else 3 + pontuacao // 200
        else:
            velocidade = 7 if b["tipo"] == "rapido" else 5 + pontuacao // 150

        barril.x += velocidade * b["dir"]
        barril.y += 5

        if random.random() < 0.01:
            b["dir"] *= -1

        for escada in escadas:
            if barril.colliderect(escada) and random.random() < 0.02:
                barril.y += 15

        for andar in andares:
            plat = andar["rect"]
            if barril.colliderect(plat):
                barril.bottom = plat.top
                if andar["buraco_esquerda"] and barril.x < 80:
                    continue
                if not andar["buraco_esquerda"] and barril.x > 520:
                    continue
                b["dir"] = -1 if andar["buraco_esquerda"] else 1

        if barril.colliderect(player):
            if poder_bomb_ativo:
                barris_remover.append(b)
                pontuacao += 10
            else:
                vidas -= 1
                resetar()
                if vidas <= 0:
                    # GAME OVER: mostra tela e encerra
                    tela_game_over()
                    pygame.quit()
                    sys.exit()

    for b in barris_remover:
        if b in barris:
            barris.remove(b)
    barris = [b for b in barris if b["rect"].y < MUNDO_ALTURA]

    if player.y > MUNDO_ALTURA:
        vidas -= 1
        resetar()
        if vidas <= 0:
            # GAME OVER: mostra tela e encerra
            tela_game_over()
            pygame.quit()
            sys.exit()

    if player.colliderect(objetivo):
        pontuacao += 100
        avancar_fase()

    for plat in plataformas:
        pygame.draw.rect(TELA, BRANCO, (plat.x, plat.y - camera_y, plat.width, plat.height))

    for escada in escadas:
        TELA.blit(escada_img, (escada.x, escada.y - camera_y))

    for item in itens:
        desenhar_item(item, camera_y)

    pygame.draw.rect(TELA, AMARELO, (objetivo.x, objetivo.y - camera_y, objetivo.width, objetivo.height))
    TELA.blit(macaco_img, (macaco_pos[0], macaco_pos[1] - camera_y))

    if poder_vel_ativo or poder_bomb_ativo:
        cor_aura = AZUL_CLARO if poder_vel_ativo else VERMELHO
        aura = (player.x - 4, player.bottom - sprite.get_height() - camera_y - 4, sprite.get_width() + 8, sprite.get_height() + 8)
        pygame.draw.rect(TELA, cor_aura, aura, 3, border_radius=8)

    TELA.blit(sprite, (player.x, player.bottom - sprite.get_height() - camera_y + 10))

    for b in barris:
        draw_y = b["rect"].bottom - barril_img.get_height() - camera_y
        TELA.blit(barril_img, (b["rect"].x, draw_y))

    texto = fonte.render(f"Pontuação: {pontuacao}", True, BRANCO)
    vidas_txt = fonte.render(f"Vidas: {vidas}", True, BRANCO)
    fase_txt = fonte.render(f"Fase: {fase_atual}", True, AMARELO)
    x_pont = LARGURA - texto.get_width() - 15
    pygame.draw.rect(TELA, CINZA_ESC, (x_pont - 10, 5, texto.get_width() + 20, 45), border_radius=10)
    TELA.blit(texto, (x_pont, 10))
    TELA.blit(vidas_txt, (10, 10))
    TELA.blit(fase_txt, (LARGURA // 2 - fase_txt.get_width() // 2, 10))

    hud_y = 50
    if poder_vel_ativo:
        desenhar_barra_poder("TURBO", poder_vel_timer, PODER_VEL_DURACAO, AZUL_CLARO, hud_y)
        hud_y += 30
    if poder_bomb_ativo:
        desenhar_barra_poder("BOMBA", poder_bomb_timer, PODER_BOMB_DURACAO, VERMELHO, hud_y)

    leg = fonte_pow.render("Azul = Turbo  |  Vermelho = Bomba", True, (160, 160, 160))
    TELA.blit(leg, (10, ALTURA - 28))

    pygame.display.flip()