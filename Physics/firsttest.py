import pygame , sys, pymunk

def create_apple(space,pos):
    body = pymunk.Body(1,100,body_type = pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body,70)
    space.add(body,shape)
    return shape

def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        apple_rect = apple_surface.get_rect(center = (pos_x,pos_y))
        screen.blit(apple_surface,apple_rect)

def static_ball(space,pos):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body,50)
    space.add(body,shape)
    return shape

def draw_ball(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen,(183,110,121),(pos_x,pos_y),50)

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0,500)
apple_surface = pygame.image.load('apple.png')
apples = []
balls = []
LEFT = 1
RIGHT = 3


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            apples.append(create_apple(space,event.pos))
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            balls.append(static_ball(space,event.pos))

    
    screen.fill((217,217,217))
    draw_apples(apples)
    draw_ball(balls)
    space.step(1/50)
    pygame.display.update()
    clock.tick(60)
