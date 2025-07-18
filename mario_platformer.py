import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
MAP_WIDTH = WIDTH * 5
STAGE_COUNT = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# 캐릭터 도트 이미지
PLAYER_W, PLAYER_H = 40, 60
MONSTER_W, MONSTER_H = 40, 60

def draw_player(surface, x, y, jumping):
    color = (255, 220, 180)
    pygame.draw.rect(surface, color, (x, y, PLAYER_W, PLAYER_H))
    pygame.draw.circle(surface, (200, 150, 100), (x+PLAYER_W//2, y+15), 15)
    if jumping:
        pygame.draw.line(surface, (0,0,0), (x+10, y+40), (x, y+20), 5)
        pygame.draw.line(surface, (0,0,0), (x+30, y+40), (x+40, y+20), 5)
        pygame.draw.line(surface, (0,0,0), (x+10, y+60), (x, y+50), 5)
        pygame.draw.line(surface, (0,0,0), (x+30, y+60), (x+40, y+50), 5)
    else:
        pygame.draw.line(surface, (0,0,0), (x+10, y+40), (x+10, y+60), 5)
        pygame.draw.line(surface, (0,0,0), (x+30, y+40), (x+30, y+60), 5)
        pygame.draw.line(surface, (0,0,0), (x+10, y+60), (x+5, y+80), 5)
        pygame.draw.line(surface, (0,0,0), (x+30, y+60), (x+35, y+80), 5)

def draw_monster(surface, x, y, mtype, squashed):
    if squashed:
        pygame.draw.ellipse(surface, (120, 120, 120), (x, y+MONSTER_H//2, MONSTER_W, MONSTER_H//3))
        return
    if mtype == 'mushroom':
        pygame.draw.rect(surface, (200,0,0), (x, y+20, MONSTER_W, MONSTER_H-20))
        pygame.draw.ellipse(surface, (255, 0, 0), (x, y, MONSTER_W, 30))
        pygame.draw.rect(surface, (255,255,255), (x+10, y+40, 20, 10))
    elif mtype == 'bomb':
        pygame.draw.ellipse(surface, (50,50,50), (x, y, MONSTER_W, MONSTER_H))
        pygame.draw.line(surface, (255,255,0), (x+MONSTER_W//2, y), (x+MONSTER_W//2, y-10), 3)
    elif mtype == 'bird':
        pygame.draw.ellipse(surface, (100,200,255), (x, y, MONSTER_W, MONSTER_H))
        pygame.draw.polygon(surface, (255,255,0), [(x+MONSTER_W, y+MONSTER_H//2), (x+MONSTER_W+15, y+MONSTER_H//2-10), (x+MONSTER_W+15, y+MONSTER_H//2+10)])

def draw_background(surface, camera_x):
    surface.fill((135, 206, 235))
    for i in range(0, MAP_WIDTH, 300):
        pygame.draw.ellipse(surface, (255,255,255), (i-camera_x, 80, 120, 50))
    for i in range(0, MAP_WIDTH, 200):
        pygame.draw.ellipse(surface, (255,255,255), (i-camera_x+100, 150, 80, 30))

def get_stage_map(stage):
    platforms = []
    pits = []
    monsters = []
    # 계단형 바닥 생성
    step_height = 550
    for i in range(0, MAP_WIDTH, 400):
        h = step_height - (i//400)*random.randint(0, 80)
        platforms.append(pygame.Rect(i, h, 400, 50))
        step_height = h
    # 낭떠러지는 바닥에 붙어 있도록 생성
    pits = []
    for i in range(stage, stage+2):
        pit_x = 600*i
        pit_w = 120 + 40*stage
        # 바닥 높이 찾기
        pit_y = 0
        for plat in platforms:
            if plat.x <= pit_x < plat.x + plat.width:
                pit_y = plat.y
                break
        pits.append(pygame.Rect(pit_x, pit_y, pit_w, 50))
    # 다양한 크기의 플랫폼 추가
    for i in range(5+stage):
        plat_w = random.randint(100, 250)
        plat_x = random.randint(200, MAP_WIDTH-plat_w-200)
        plat_y = random.randint(250, 500)
        platforms.append(pygame.Rect(plat_x, plat_y, plat_w, 20))
    # 낭떠러지 생성
    for i in range(stage, stage+2):
        pit_x = 600*i
        pit_w = 120 + 40*stage
        pits.append(pygame.Rect(pit_x, 0, pit_w, HEIGHT))
    # 몬스터 생성
    for i in range(stage+2):
        mx = 400 + 400*i
        mtype = random.choice(['mushroom','bomb','bird'])
        # 몬스터가 플랫폼 위에 생성
        plat = random.choice(platforms)
        my = plat.y - MONSTER_H
        monsters.append({'rect': pygame.Rect(mx, my, MONSTER_W, MONSTER_H), 'type': mtype, 'squashed': False, 'dir': random.choice([-1,1])})
    return platforms, pits, monsters

def main():
    stage = 1
    player = pygame.Rect(100, 500, PLAYER_W, PLAYER_H)
    player_vel_y = 0
    on_ground = False
    while stage <= STAGE_COUNT:
        platforms, pits, monsters = get_stage_map(stage)
        goal = pygame.Rect(MAP_WIDTH-100, 500, 60, 60)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and on_ground:
                    player_vel_y = -18
            keys = pygame.key.get_pressed()
            dx = 0
            if keys[pygame.K_LEFT]:
                dx -= 5
            if keys[pygame.K_RIGHT]:
                dx += 5
            player.x += dx
            player_vel_y += 1
            player.y += player_vel_y
            on_ground = False
            for plat in platforms:
                if player.colliderect(plat) and player_vel_y >= 0:
                    player.bottom = plat.top
                    player_vel_y = 0
                    on_ground = True
            # 낭떠러지 체크 (플레이어)
            in_pit = False
            for pit in pits:
                if player.colliderect(pit):
                    in_pit = True
                    break
            if player.y > HEIGHT or in_pit:
                # 게임 오버 화면 및 다시 시작 버튼
                while True:
                    screen.fill((0,0,0))
                    font = pygame.font.SysFont(None, 72)
                    text = font.render("GAME OVER", True, (255,0,0))
                    screen.blit(text, (WIDTH//2-180, HEIGHT//2-36))
                    btn_font = pygame.font.SysFont(None, 48)
                    btn_text = btn_font.render("다시 시작", True, (255,255,255))
                    btn_rect = pygame.Rect(WIDTH//2-100, HEIGHT//2+40, 200, 60)
                    pygame.draw.rect(screen, (50,150,255), btn_rect)
                    screen.blit(btn_text, (btn_rect.x+30, btn_rect.y+10))
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if btn_rect.collidepoint(event.pos):
                                # 다시 시작
                                main()
                                return
                    clock.tick(30)
            # 몬스터 이동 및 충돌, 낭떠러지 체크
            for m in monsters:
                if not m['squashed']:
                    m['rect'].x += m['dir'] * 2
                    if m['rect'].left < 0 or m['rect'].right > MAP_WIDTH:
                        m['dir'] *= -1
                    # 몬스터가 낭떠러지에 떨어지면 사라짐
                    m_in_pit = False
                    for pit in pits:
                        if m['rect'].colliderect(pit):
                            m_in_pit = True
                            break
                    if m['rect'].y > HEIGHT or m_in_pit:
                        m['squashed'] = True
                        continue
                    # 플레이어가 몬스터 위에서 밟으면 squashed
                    if player.colliderect(m['rect']) and player_vel_y > 0 and player.bottom <= m['rect'].top + 20:
                        m['squashed'] = True
                        player_vel_y = -10
                    # 몬스터와 옆에서 부딪히면 게임 오버
                    elif player.colliderect(m['rect']) and not m['squashed']:
                        while True:
                            screen.fill((0,0,0))
                            font = pygame.font.SysFont(None, 72)
                            text = font.render("GAME OVER", True, (255,0,0))
                            screen.blit(text, (WIDTH//2-180, HEIGHT//2-36))
                            btn_font = pygame.font.SysFont(None, 48)
                            btn_text = btn_font.render("다시 시작", True, (255,255,255))
                            btn_rect = pygame.Rect(WIDTH//2-100, HEIGHT//2+40, 200, 60)
                            pygame.draw.rect(screen, (50,150,255), btn_rect)
                            screen.blit(btn_text, (btn_rect.x+30, btn_rect.y+10))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if btn_rect.collidepoint(event.pos):
                                        main()
                                        return
                            clock.tick(30)
            camera_x = max(0, min(player.x - WIDTH//2, MAP_WIDTH - WIDTH))
            draw_background(screen, camera_x)
            for plat in platforms:
                plat_screen = plat.move(-camera_x, 0)
                pygame.draw.rect(screen, (34,139,34), plat_screen)
                pygame.draw.rect(screen, (0,180,0), (plat_screen.x, plat_screen.y+40, plat_screen.width, 10))
            for pit in pits:
                pit_screen = pit.move(-camera_x, 0)
                pygame.draw.rect(screen, (80,80,80), pit_screen)
            goal_screen = goal.move(-camera_x, 0)
            pygame.draw.rect(screen, (255, 215, 0), goal_screen)
            draw_player(screen, player.x - camera_x, player.y, not on_ground)
            for m in monsters:
                draw_monster(screen, m['rect'].x-camera_x, m['rect'].y, m['type'], m['squashed'])
            font = pygame.font.SysFont(None, 48)
            text = font.render(f"Stage {stage}-1", True, (0,0,0))
            screen.blit(text, (20, 20))
            pygame.display.flip()
            clock.tick(60)
            if player.colliderect(goal):
                stage += 1
                player.x, player.y = 100, 500
                break
    screen.fill((0,0,0))
    font = pygame.font.SysFont(None, 72)
    text = font.render("모든 스테이지 클리어!", True, (255,255,255))
    screen.blit(text, (WIDTH//2-200, HEIGHT//2-36))
    pygame.display.flip()
    pygame.time.wait(3000)

if __name__ == '__main__':
    main()
