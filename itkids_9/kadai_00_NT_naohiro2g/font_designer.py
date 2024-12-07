# Dot-Matrix Font Designer
# 5x7のドットマトリクスフォントをデザインするためのプログラム
# 各文字は5x7のドットマトリクスで表現される
# フォントデータはfont.txtに保存される
# font.txtが存在しない場合、96文字分のデータで初期化される

import os
import shutil
import pygame
import pygame.freetype

# ドットマトリクスの設定
SMALL_DOT_SIZE = 6
LARGE_DOT_SIZE = 16
SMALL_MARGIN = 2
LARGE_MARGIN = 4
WINDOW_MARGIN = 8
DISPLAY_COL_MARGIN = 6
DISPLAY_ROW_MARGIN = 6
ROWS = 7
COLS = 5
SMALL_DOT_INTV = SMALL_DOT_SIZE + SMALL_MARGIN
LARGE_DOT_INTV = LARGE_DOT_SIZE + LARGE_MARGIN
DISPLAY_COL_INTV = COLS * SMALL_DOT_INTV + DISPLAY_COL_MARGIN
DISPLAY_ROW_INTV = ROWS * SMALL_DOT_INTV + DISPLAY_ROW_MARGIN

# 表示領域の設定
DISPLAY_ROWS = 6
DISPLAY_COLS = 16

# 画面の設定
WINDOW_WIDTH = DISPLAY_COLS * DISPLAY_COL_INTV - DISPLAY_COL_MARGIN + WINDOW_MARGIN * 2
WINDOW_HEIGHT = 660

# 初期化
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Dot-Matrix Font Designer')

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LAVENDER = (230, 230, 250)
DARK_RED = (139, 0, 0)
LIGHT_RED = (255, 182, 193)
DARK_BLUE = (0, 0, 139)
LIGHT_BLUE = (173, 216, 230)
PURPLE = (128, 0, 128)
LIGHT_PURPLE = (216, 191, 216)

# フォントの設定
FONT_PATH = 'fonts/natumemozi.ttf'
font1 = pygame.freetype.Font(FONT_PATH, 24)
large_font = pygame.freetype.Font(FONT_PATH, 48)
SAVE_MESSAGE_STAY = 1500

# 参照用文字とデザイン用文字の表示位置
REF_CHAR_X = (WINDOW_WIDTH // 4) - (COLS * LARGE_DOT_INTV // 2)
REF_CHAR_Y = WINDOW_HEIGHT - 200
DESIGN_CHAR_X = (3 * WINDOW_WIDTH // 4) - (COLS * LARGE_DOT_INTV // 2)
DESIGN_CHAR_Y = WINDOW_HEIGHT - 200

# 矢印アイコンの読み込み
arrow_image = pygame.image.load('images/right_arrow.png')
arrow_rect = arrow_image.get_rect()
arrow_rect.center = (WINDOW_WIDTH // 2,
                     REF_CHAR_Y + (ROWS * LARGE_DOT_INTV) // 2)

# 鉛筆アイコンの読み込み
pencil_image = pygame.image.load('images/pencil.png')
pencil_rect = pencil_image.get_rect()
pencil_rect.topleft = (DESIGN_CHAR_X + COLS * LARGE_DOT_INTV + 10,
                       DESIGN_CHAR_Y)

# チェックマークアイコンの読み込み
check_image = pygame.image.load('images/check.png')
check_rect = check_image.get_rect()
check_rect.center = (arrow_rect.centerx, arrow_rect.centery - arrow_rect.height)

# 初期データの読み込みまたは初期化
FONT_FILE = 'font.txt'
BACKUP_FILE = 'font.txt.bak'
if os.path.exists(FONT_FILE):
    shutil.copy(FONT_FILE, BACKUP_FILE)  # バックアップを作成
    with open(FONT_FILE, 'r', encoding='utf-8') as f:
        font_data = f.read().splitlines()
else:
    font_data = ['00000' for _ in range(ROWS * (0x7F - 0x20 + 1))]

# データが不足している場合の初期化
if len(font_data) < ROWS * (0x7F - 0x20 + 1):
    font_data.extend(['00000' for _ in range(ROWS * (0x7F - 0x20 + 1) - len(font_data))])

# 選択状態の初期化
blue_selection = [0, 0]
red_selection = [0, 0]

# デザイン用文字の一時データ
design_char_data = ['00000' for _ in range(ROWS)]

# メインループ
RUNNING = True
SAVE_MESSAGE_TIME = 0
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                blue_selection[1] = max(0, blue_selection[1] - 1)
            elif event.key == pygame.K_s:
                blue_selection[1] = min(DISPLAY_ROWS - 1, blue_selection[1] + 1)
            elif event.key == pygame.K_a:
                blue_selection[0] = max(0, blue_selection[0] - 1)
            elif event.key == pygame.K_d:
                blue_selection[0] = min(DISPLAY_COLS - 1, blue_selection[0] + 1)
            elif event.key == pygame.K_UP:
                red_selection[1] = max(0, red_selection[1] - 1)
                DESIGN_CHAR_INDEX = red_selection[1] * DISPLAY_COLS + red_selection[0]
                if DESIGN_CHAR_INDEX < (0x7F - 0x20 + 1):
                    design_char_data = font_data[DESIGN_CHAR_INDEX * ROWS:(DESIGN_CHAR_INDEX + 1) * ROWS]
            elif event.key == pygame.K_DOWN:
                red_selection[1] = min(DISPLAY_ROWS - 1, red_selection[1] + 1)
                DESIGN_CHAR_INDEX = red_selection[1] * DISPLAY_COLS + red_selection[0]
                if DESIGN_CHAR_INDEX < (0x7F - 0x20 + 1):
                    design_char_data = font_data[DESIGN_CHAR_INDEX * ROWS:(DESIGN_CHAR_INDEX + 1) * ROWS]
            elif event.key == pygame.K_LEFT:
                red_selection[0] = max(0, red_selection[0] - 1)
                DESIGN_CHAR_INDEX = red_selection[1] * DISPLAY_COLS + red_selection[0]
                if DESIGN_CHAR_INDEX < (0x7F - 0x20 + 1):
                    design_char_data = font_data[DESIGN_CHAR_INDEX * ROWS:(DESIGN_CHAR_INDEX + 1) * ROWS]
            elif event.key == pygame.K_RIGHT:
                red_selection[0] = min(DISPLAY_COLS - 1, red_selection[0] + 1)
                DESIGN_CHAR_INDEX = red_selection[1] * DISPLAY_COLS + red_selection[0]
                if DESIGN_CHAR_INDEX < (0x7F - 0x20 + 1):
                    design_char_data = font_data[DESIGN_CHAR_INDEX * ROWS:(DESIGN_CHAR_INDEX + 1) * ROWS]
            elif event.key == pygame.K_RETURN:
                # エンターキーでデザイン用文字の変更を表示領域に反映
                DESIGN_CHAR_INDEX = red_selection[1] * DISPLAY_COLS + red_selection[0]
                if DESIGN_CHAR_INDEX < (0x7F - 0x20 + 1):
                    font_data[DESIGN_CHAR_INDEX * ROWS:(DESIGN_CHAR_INDEX + 1) * ROWS] = design_char_data[:]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            cond1 = DESIGN_CHAR_X <= mouse_x < DESIGN_CHAR_X + COLS * LARGE_DOT_INTV
            cond2 = DESIGN_CHAR_Y <= mouse_y < DESIGN_CHAR_Y + ROWS * LARGE_DOT_INTV
            if cond1 and cond2:
                c = (mouse_x - DESIGN_CHAR_X) // LARGE_DOT_INTV
                r = (mouse_y - DESIGN_CHAR_Y) // LARGE_DOT_INTV
                DESIGN_CHAR_INDEX = red_selection[1] * DISPLAY_COLS + red_selection[0]
                if DESIGN_CHAR_INDEX < (0x7F - 0x20 + 1):
                    if design_char_data == ['00000' for _ in range(ROWS)]:
                        design_char_data = font_data[DESIGN_CHAR_INDEX * ROWS:(DESIGN_CHAR_INDEX + 1) * ROWS]
                    new_row = list(design_char_data[r])
                    new_row[c] = '0' if new_row[c] == '1' else '1'
                    design_char_data[r] = ''.join(new_row)
            elif arrow_rect.collidepoint(mouse_x, mouse_y):
                # 矢印アイコンがクリックされた場合、参照用文字をデザイン用文字にコピー
                REF_CHAR_INDEX = blue_selection[1] * DISPLAY_COLS + blue_selection[0]
                if REF_CHAR_INDEX < (0x7F - 0x20 + 1):
                    design_char_data = font_data[REF_CHAR_INDEX * ROWS:(REF_CHAR_INDEX + 1) * ROWS]
            elif pencil_rect.collidepoint(mouse_x, mouse_y):
                # 鉛筆アイコンがクリックされた場合、デザイン用文字の変更を表示領域に反映
                DESIGN_CHAR_INDEX = red_selection[1] * DISPLAY_COLS + red_selection[0]
                if DESIGN_CHAR_INDEX < (0x7F - 0x20 + 1):
                    font_data[DESIGN_CHAR_INDEX * ROWS:(DESIGN_CHAR_INDEX + 1) * ROWS] = design_char_data[:]
            elif check_rect.collidepoint(mouse_x, mouse_y):
                # チェックマークアイコンがクリックされた場合、表示領域の全てのデータをfont.txtに書き出し
                with open(FONT_FILE, 'w', encoding='utf-8') as f:
                    for line in font_data:
                        f.write(line + '\n')
                SAVE_MESSAGE_TIME = pygame.time.get_ticks()

    # 画面のクリア
    screen.fill(LAVENDER)

    # 表示領域の描画（上部）
    for row in range(DISPLAY_ROWS):
        for col in range(DISPLAY_COLS):
            char_index = row * DISPLAY_COLS + col
            if char_index < (0x7F - 0x20 + 1):
                char_data = font_data[char_index * ROWS:(char_index + 1) * ROWS]
                for r in range(ROWS):
                    for c in range(COLS):
                        x = col * DISPLAY_COL_INTV + c * SMALL_DOT_INTV + WINDOW_MARGIN
                        y = row * DISPLAY_ROW_INTV + r * SMALL_DOT_INTV + WINDOW_MARGIN
                        if char_data[r][c] == '1':
                            if [col, row] == blue_selection and [col, row] == red_selection:
                                color = PURPLE
                            elif [col, row] == blue_selection:
                                color = DARK_BLUE
                            elif [col, row] == red_selection:
                                color = DARK_RED
                            else:
                                color = BLACK
                        else:
                            if [col, row] == blue_selection and [col, row] == red_selection:
                                color = LIGHT_PURPLE
                            elif [col, row] == blue_selection:
                                color = LIGHT_BLUE
                            elif [col, row] == red_selection:
                                color = LIGHT_RED
                            else:
                                color = WHITE
                        pygame.draw.rect(screen, color, (x, y, SMALL_DOT_SIZE, SMALL_DOT_SIZE))

    # 参照用文字の描画（左下）
    REF_CHAR_INDEX = blue_selection[1] * DISPLAY_COLS + blue_selection[0]
    if REF_CHAR_INDEX < (0x7F - 0x20 + 1):
        ref_char_data = font_data[REF_CHAR_INDEX * ROWS:(REF_CHAR_INDEX + 1) * ROWS]
        for r in range(ROWS):
            for c in range(COLS):
                color = DARK_BLUE if ref_char_data[r][c] == '1' else LIGHT_BLUE
                pygame.draw.rect(screen, color,
                                 (REF_CHAR_X + c * LARGE_DOT_INTV,
                                  REF_CHAR_Y + r * LARGE_DOT_INTV,
                                  LARGE_DOT_SIZE, LARGE_DOT_SIZE))

    # デザイン用文字の描画（右下）
    for r in range(ROWS):
        for c in range(COLS):
            color = DARK_RED if design_char_data[r][c] == '1' else LIGHT_RED
            pygame.draw.rect(screen, color, (DESIGN_CHAR_X + c * LARGE_DOT_INTV,
                                             DESIGN_CHAR_Y + r * LARGE_DOT_INTV,
                                             LARGE_DOT_SIZE, LARGE_DOT_SIZE))

    # 矢印アイコンの描画
    screen.blit(arrow_image, arrow_rect)

    # 鉛筆アイコンの描画
    screen.blit(pencil_image, pencil_rect)

    # チェックマークアイコンの描画
    screen.blit(check_image, check_rect)

    # 現在選択されているコードの表示
    ref_code = f"0x{0x20 + blue_selection[1] * DISPLAY_COLS + blue_selection[0]:02X}"
    design_code = f"0x{0x20 + red_selection[1] * DISPLAY_COLS + red_selection[0]:02X}"
    ref_code_surface, _ = font1.render(ref_code, BLACK, None,
                                       pygame.freetype.STYLE_DEFAULT, True)
    design_code_surface, _ = font1.render(design_code, BLACK, None,
                                          pygame.freetype.STYLE_DEFAULT, True)
    screen.blit(ref_code_surface, (REF_CHAR_X + 24, REF_CHAR_Y + ROWS * LARGE_DOT_INTV + 10))
    screen.blit(design_code_surface, (DESIGN_CHAR_X + 24, DESIGN_CHAR_Y + ROWS * LARGE_DOT_INTV + 10))

    # キーガイドの表示
    w_surface, _ = font1.render("W", BLACK, None)
    a_surface, _ = font1.render("A", BLACK, None)
    s_surface, _ = font1.render("S", BLACK, None)
    d_surface, _ = font1.render("D", BLACK, None)
    up_surface, _ = font1.render("↑", BLACK, None)
    left_surface, _ = font1.render("←", BLACK, None)
    down_surface, _ = font1.render("↓", BLACK, None)
    right_surface, _ = font1.render("→", BLACK, None)

    screen.blit(w_surface, (REF_CHAR_X - 40, REF_CHAR_Y + 70))
    screen.blit(a_surface, (REF_CHAR_X - 60, REF_CHAR_Y + 100))
    screen.blit(s_surface, (REF_CHAR_X - 40, REF_CHAR_Y + 100))
    screen.blit(d_surface, (REF_CHAR_X - 20, REF_CHAR_Y + 100))

    screen.blit(up_surface, (DESIGN_CHAR_X + COLS * LARGE_DOT_INTV + 20, DESIGN_CHAR_Y + 70))
    screen.blit(left_surface, (DESIGN_CHAR_X + COLS * LARGE_DOT_INTV, DESIGN_CHAR_Y + 100))
    screen.blit(down_surface, (DESIGN_CHAR_X + COLS * LARGE_DOT_INTV + 20, DESIGN_CHAR_Y + 100))
    screen.blit(right_surface, (DESIGN_CHAR_X + COLS * LARGE_DOT_INTV + 40, DESIGN_CHAR_Y + 100))

    # 保存メッセージの表示
    if SAVE_MESSAGE_TIME and pygame.time.get_ticks() - SAVE_MESSAGE_TIME < SAVE_MESSAGE_STAY:
        save_message_surface, _ = font1.render("デザインをfont.txtに保存しました。",
                                               BLACK, None,
                                               pygame.freetype.STYLE_DEFAULT, True)
        screen.blit(save_message_surface,
                    (WINDOW_WIDTH // 2 - save_message_surface.get_width() // 2, check_rect.top - 50))
    else:
        SAVE_MESSAGE_TIME = 0

    # 画面の更新
    pygame.display.flip()

pygame.quit()
