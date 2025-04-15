import pygame, sys, random, psycopg2



conn = psycopg2.connect(
    host = "localhost",
    database = "snake_db",
    user = "postgres",
    password = "Almas200"
)
cur = conn.cursor()

# Player Name
username = input("Enter Your Name: ")

cur.execute("SELECT id, score, level FROM user_score WHERE name = %s;", (username,))
player = cur.fetchone()


if player is None:
    cur.execute("INSERT INTO user_score (name, score, level) VALUES (%s, 0, 1) RETURNING id;", (username,))
    user_id = cur.fetchone()[0]
    score = 0
    level = 1
    conn.commit()
    print("New player added.")
else:
    user_id, score, level = player
    print(f"Welcome back, {username}! Level: {level}, Score: {score}")


# Game setup
speed = 10 + (level - 1) * 2
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

snake = [(100, 100)]
direction = (20, 0)

def make_food():
    x = random.randint(0, 39) * 20
    y = random.randint(0, 29) * 20
    return x, y

food = make_food()

def game_over():
    cur.execute("UPDATE user_score SET score = %s, level = %s WHERE id = %s;", (score, level, user_id))
    conn.commit()
    cur.close()
    conn.close()
    pygame.quit()
    print("Game Over. Score:", score)
    sys.exit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 20):
                direction = (0, -20)
            elif event.key == pygame.K_DOWN and direction != (0, -20):
                direction = (0, 20)
            elif event.key == pygame.K_LEFT and direction != (20, 0):
                direction = (-20, 0)
            elif event.key == pygame.K_RIGHT and direction != (-20, 0):
                direction = (20, 0)
            elif event.key == pygame.K_p:
                cur.execute("UPDATE user_score SET score = %s, level = %s WHERE id = %s;", (score, level, user_id))
                conn.commit()
                print("Game paused. Press P again to continue.")
                paused = True
                while paused:
                    for e in pygame.event.get():
                        if e.type == pygame.KEYDOWN and e.key == pygame.K_p:
                            paused = False


    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    if head[0] < 0 or head[0] >= 800 or head[1] < 0 or head[1] >= 600 or head in snake:
        game_over()

    snake = [head] + snake
    if head == food:
        score += 1
        if score % 5 == 0:
            level += 1
            speed += 1
        food = make_food()
    else:
        snake.pop()

    screen.fill((0, 0, 0))
    for s in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*s, 20, 20))
    pygame.draw.rect(screen, (255, 0, 0), (*food, 20, 20))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    level_text = font.render(f"Level: {level}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 30))

    pygame.display.flip()
    clock.tick(speed)