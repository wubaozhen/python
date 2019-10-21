### 用pygame画图
```
import pygame

pygame.init()
screen = pygame.display.set_mode((900,600))  # 设定屏幕大小
drawing = False
clock = pygame.time.Clock()
screen.fill((255,255,255))  # 屏幕背景色
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            quit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        if i.type == pygame.MOUSEBUTTONUP:
            drawing = False

    if drawing:
        pygame.draw.circle(screen,(0,0,0),pygame.mouse.get_pos(),3)

    pygame.display.flip()
    clock.tick(100)
   
 ```
