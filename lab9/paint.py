import pygame

pygame.init()

w, h = 800, 600
screen = pygame.display.set_mode([w, h])
pygame.display.set_caption("PAINT")
painting = []
timer = pygame.time.Clock()
fps = 60
activeColor, activeShape = (0, 0, 0), 0


def drawDisplay():
    pygame.draw.rect(screen, 'gray', [0, 0, w, 100])  # Background for the UI
    pygame.draw.line(screen, 'black', [0, 100], [w, 100])  # Separator line
    
    # (rect, circle, triangle, rhombus)
    shapes = [
        [pygame.draw.rect(screen, 'black', [10, 10, 80, 80]), 0, pygame.draw.rect(screen, 'white', [20, 20, 60, 60])],
        [pygame.draw.rect(screen, 'black', [100, 10, 80, 80]), 1, pygame.draw.circle(screen, 'white', [140, 50], 30)],
        [pygame.draw.rect(screen, 'black', [200, 10, 80, 80]), 2, pygame.draw.polygon(screen, "white", ((240, 30),(240 - 30, 80),(240 + 30, 80)))],
        [pygame.draw.rect(screen, 'black', [300, 10, 80, 80]), 3, pygame.draw.polygon(screen, "white", ((340, 50-30), (340+30, 50), (340, 50+30), (340-30, 50)))],
    ]
    
    # Define color buttons
    colors = [
        [pygame.draw.rect(screen, (0, 0, 255), [w - 35, 10, 25, 25]), (0, 0, 255)],
        [pygame.draw.rect(screen, (255, 0, 0), [w - 35, 35, 25, 25]), (255, 0, 0)],
        [pygame.draw.rect(screen, (0, 255, 0), [w - 60, 10, 25, 25]), (0, 255, 0)],
        [pygame.draw.rect(screen, (255, 255, 0), [w - 60, 35, 25, 25]), (255, 255, 0)],
        [pygame.draw.rect(screen, (0, 0, 0), [w - 85, 10, 25, 25]), (0, 0, 0)],
        [pygame.draw.rect(screen, (255, 0, 255), [w - 85, 35, 25, 25]), (255, 0, 255)],
        [pygame.draw.rect(screen, (255, 255, 255), [w - 150, 20, 25, 25]), (255, 255, 255)]
    ]
    return colors, shapes


def drawPaint(paints):
    for paint in paints:
        if paint[2] == 1:
            pygame.draw.circle(screen, paint[0], paint[1], 15)  # Draw circle
        elif paint[2] == 0:
            pygame.draw.rect(screen, paint[0], [paint[1][0]-15, paint[1][1]-15, 30, 30])  # Draw square
        elif paint[2] == 2:
            pygame.draw.polygon(screen, paint[0], ((paint[1][0]-15, paint[1][1]+15), (paint[1][0], paint[1][1]-15), (paint[1][0]+15, paint[1][1]+15)))  # Draw triangle
        elif paint[2] == 3:
            pygame.draw.polygon(screen, paint[0], ((paint[1][0], paint[1][1]-15), (paint[1][0]+15, paint[1][1]), (paint[1][0], paint[1][1]+15), (paint[1][0]-15, paint[1][1])))  # Draw rhombus

# Function to handle the painting process
def draw():
    global activeColor, activeShape, mouse
    if mouse[1] > 100:
        if activeShape == 0:
            pygame.draw.rect(screen, activeColor, [mouse[0]-15, mouse[1]-15, 30, 30])  # Square shape
        elif activeShape == 1:
            pygame.draw.circle(screen, activeColor, mouse, 15)  # Circle shape
        elif activeShape == 2:
            pygame.draw.polygon(screen, activeColor, ((mouse[0]-15, mouse[1]+15), (mouse[0], mouse[1]-15), (mouse[0]+15, mouse[1]+15)))  # Triangle shape
        elif activeShape == 3:
            pygame.draw.polygon(screen, activeColor, ((mouse[0], mouse[1]-15), (mouse[0]+15, mouse[1]), (mouse[0], mouse[1]+15), (mouse[0]-15, mouse[1])))  # Rhombus shape


run = True
while run:
    timer.tick(fps)  # Set frame rate
    screen.fill('white')  # Clear screen
    
    # Draw UI elements (colors, shapes)
    colors, shapes = drawDisplay()

    mouse = pygame.mouse.get_pos()  # Get mouse position
    draw()  # Draw the selected shape

    # Check if the user clicked to draw a shape
    click = pygame.mouse.get_pressed()[0]
    if click and mouse[1] > 100:
        painting.append((activeColor, mouse, activeShape))  # Add shape to the painting list
    drawPaint(painting)  # Draw the painted shapes

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            elif event.key == pygame.K_SPACE:
                painting = []
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in colors:
                if i[0].collidepoint(event.pos):
                    activeColor = i[1]
            for i in shapes:
                if i[0].collidepoint(event.pos):
                    activeShape = i[1]

    pygame.display.flip()

pygame.quit()