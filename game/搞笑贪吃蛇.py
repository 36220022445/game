import pygame
import random

# 初始化 pygame
pygame.init()

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 游戏窗口设置
WIDTH, HEIGHT = 640, 480
BLOCK_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("搞笑贪吃蛇")

# 时钟对象
clock = pygame.time.Clock()


# 蛇类
class Snake:
    def __init__(self, color, start_x, start_y):
        self.body = [(start_x, start_y)]
        self.direction = 'RIGHT'
        self.color = color

    def move(self):
        head = self.body[0]
        if self.direction == 'UP':
            new_head = (head[0], head[1] - BLOCK_SIZE)
        elif self.direction == 'DOWN':
            new_head = (head[0], head[1] + BLOCK_SIZE)
        elif self.direction == 'LEFT':
            new_head = (head[0] - BLOCK_SIZE, head[1])
        elif self.direction == 'RIGHT':
            new_head = (head[0] + BLOCK_SIZE, head[1])

            # 穿墙功能
        if new_head[0] < 0:
            new_head = (WIDTH - BLOCK_SIZE, new_head[1])
        elif new_head[0] >= WIDTH:
            new_head = (0, new_head[1])
        elif new_head[1] < 0:
            new_head = (new_head[0], HEIGHT - BLOCK_SIZE)
        elif new_head[1] >= HEIGHT:
            new_head = (new_head[0], 0)

        self.body.insert(0, new_head)
        self.body.pop()

    def eat_food(self):
        self.body.insert(0, self.body[0])

    def draw(self):
        for block in self.body:
            pygame.draw.rect(screen, self.color, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

        # 食物类


class Food:
    def __init__(self):
        self.position = (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                         random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

    # 创建两条蛇和一个食物


snake1 = Snake(GREEN, 100, 100)
snake2 = Snake(BLUE, 200, 200)
food = Food()

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if snake1.direction != 'DOWN':
                    snake1.direction = 'UP'
                if snake2.direction != 'DOWN':
                    snake2.direction = 'UP'
            elif event.key == pygame.K_DOWN:
                if snake1.direction != 'UP':
                    snake1.direction = 'DOWN'
                if snake2.direction != 'UP':
                    snake2.direction = 'DOWN'
            elif event.key == pygame.K_LEFT:
                if snake1.direction != 'RIGHT':
                    snake1.direction = 'LEFT'
                if snake2.direction != 'RIGHT':
                    snake2.direction = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                if snake1.direction != 'LEFT':
                    snake1.direction = 'RIGHT'
                if snake2.direction != 'LEFT':
                    snake2.direction = 'RIGHT'

                    # 移动蛇
    snake1.move()
    snake2.move()

    # 检查蛇是否吃到食物
    if snake1.body[0] == food.position:
        snake1.eat_food()
        food = Food()
    if snake2.body[0] == food.position:
        snake2.eat_food()
        food = Food()

        # 绘制背景
    screen.fill(BLACK)

    # 绘制蛇和食物
    snake1.draw()
    snake2.draw()
    food.draw()

    # 更新显示
    pygame.display.flip()

    # 控制帧率
    clock.tick(10)

# 退出游戏
pygame.quit()