import pygame
import sys
import random

# Khởi tạo Pygame
pygame.init()
res = (720, 720)
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()

# Màu sắc
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
start_light = (169, 169, 169)
start_dark = (100, 100, 100)

# Biến trò chơi
lead_x = 40
lead_y = screen.get_height() // 2
player_color = green
enemy_size = 50
score = 0
game_speed = 15
enemy_count = 2

# Fonts
smallfont = pygame.font.SysFont('Corbel', 35)
text_start = smallfont.render('Start', True, white)
text_exit = smallfont.render('Exit', True, white)
text_options = smallfont.render('Options', True, white)

# Hàm chính của trò chơi
def game():
    global lead_x, lead_y, score, game_speed, enemy_count
    red_blocks = [[screen.get_width(), random.randint(50, screen.get_height() - 50)] for _ in range(enemy_count)]
    green_block_pos = [screen.get_width(), random.randint(50, screen.get_height() - 50)]
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            lead_y -= 10
        if keys[pygame.K_DOWN]:
            lead_y += 10

        # Giới hạn người chơi không di chuyển ra ngoài màn hình
        lead_y = max(0, min(lead_y, screen.get_height() - 40))

        screen.fill((65, 25, 64))
        clock.tick(game_speed)

        # Vẽ người chơi
        pygame.draw.rect(screen, player_color, [lead_x, lead_y, 40, 40])

        # Xử lý khối đỏ
        for red_block_pos in red_blocks:
            pygame.draw.rect(screen, red, [red_block_pos[0], red_block_pos[1], enemy_size, enemy_size])
            red_block_pos[0] -= 10
            if red_block_pos[0] < 0:
                red_block_pos[0] = screen.get_width()
                red_block_pos[1] = random.randint(50, screen.get_height() - 50)
            # Kiểm tra va chạm với khối đỏ
            if (lead_x < red_block_pos[0] + enemy_size and
                lead_x + 40 > red_block_pos[0] and
                lead_y < red_block_pos[1] + enemy_size and
                lead_y + 40 > red_block_pos[1]):
                print("Game Over")
                return

        # Xử lý khối xanh lá
        pygame.draw.rect(screen, green, [green_block_pos[0], green_block_pos[1], enemy_size, enemy_size])
        green_block_pos[0] -= 8
        if green_block_pos[0] < 0:
            green_block_pos = [screen.get_width(), random.randint(50, screen.get_height() - 50)]

        # Kiểm tra va chạm với khối xanh lá
        if (lead_x < green_block_pos[0] + enemy_size and
            lead_x + 40 > green_block_pos[0] and
            lead_y < green_block_pos[1] + enemy_size and
            lead_y + 40 > green_block_pos[1]):
            # Tăng điểm ngẫu nhiên từ 100 đến 500
            random_score = random.randint(1, 10)
            score += random_score
            print(f"Chạm khối xanh lá! Tăng điểm: {random_score}, Điểm hiện tại: {score}")
            # Đặt lại vị trí khối xanh lá
            green_block_pos = [screen.get_width(), random.randint(50, screen.get_height() - 50)]

        # Hiển thị điểm số
        score_text = smallfont.render(f'Score: {score}', True, white)
        screen.blit(score_text, (screen.get_width() - 500, 10))
        
        pygame.display.update()

# Màn hình giới thiệu
def intro():
    intro_running = True
    while intro_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 300 < mouse[0] < 400 and 290 < mouse[1] < 330:  # Kiểm tra nhấn nút "Start"
                    game()
                elif 300 < mouse[0] < 400 and 360 < mouse[1] < 400:  # Kiểm tra nhấn nút "Options"
                    options()
                elif 300 < mouse[0] < 400 and 430 < mouse[1] < 470:  # Kiểm tra nhấn nút "Exit"
                    pygame.quit()
                    sys.exit()

        screen.fill((65, 25, 64))
        screen.blit(text_start, (300, 290))
        screen.blit(text_options, (300, 360))
        screen.blit(text_exit, (300, 430))
        pygame.display.update()

# Hàm tùy chọn
def options():
    global game_speed, enemy_count
    options_running = True
    while options_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 300 < mouse[0] < 450 and 200 < mouse[1] < 240:
                    game_speed += 5
                elif 300 < mouse[0] < 450 and 250 < mouse[1] < 290:
                    game_speed = max(5, game_speed - 5)
                elif 300 < mouse[0] < 450 and 300 < mouse[1] < 340:
                    enemy_count += 1
                elif 300 < mouse[0] < 450 and 350 < mouse[1] < 390:
                    enemy_count = max(1, enemy_count - 1)
                elif 300 < mouse[0] < 450 and 400 < mouse[1] < 440:
                    return

        screen.fill((65, 25, 64))
        speed_text = smallfont.render(f'Speed: {game_speed}', True, white)
        difficulty_text = smallfont.render(f'Enemies: {enemy_count}', True, white)
        increase_speed = smallfont.render('Increase Speed', True, white)
        decrease_speed = smallfont.render('Decrease Speed', True, white)
        increase_difficulty = smallfont.render('Increase Enemies', True, white)
        decrease_difficulty = smallfont.render('Decrease Enemies', True, white)
        back_text = smallfont.render('Back', True, white)

        screen.blit(increase_speed, (300, 200))
        screen.blit(decrease_speed, (300, 250))
        screen.blit(increase_difficulty, (300, 300))
        screen.blit(decrease_difficulty, (300, 350))
        screen.blit(back_text, (300, 400))
        screen.blit(speed_text, (50, 200))
        screen.blit(difficulty_text, (50, 300))
        pygame.display.update()

# Bắt đầu game
intro()
