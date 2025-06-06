import pygame
import sys
import Tools.tools as tools
import Tools.figures as figures

pygame.init()

# Tamaño ventana
width = 1200
height = 760

# Inicializar variables ------------------------------------------
# Variables de inicio
start_point = (0, 0)
end_point = (0, 0)
drawing = False

# Colores
black = (0, 0, 0)
blue = (10, 10, 205)
red = (205, 10, 10)
green = (10, 215, 10)
yellow = (240, 240, 0)
cyan = (0, 200, 255)
magenta = (235, 0, 200)
purple = (128, 0, 128)
brown = (165, 82, 42)
orange = (255, 100, 0)

# Cargar imágenes de los botones
eraser = pygame.image.load("Images/eraser.png")
eraser = pygame.transform.scale(eraser, (40, 40))
pencil = pygame.image.load("Images/pen.png")
pencil = pygame.transform.scale(pencil, (40, 40))
broom = pygame.image.load("Images/broom.png")
broom = pygame.transform.scale(broom, (40, 40))



# Crear botones
buttons = [
    {"tool": "pencil", "rect": pygame.Rect(10, 10, 60, 50)},
    {"tool": "line", "rect": pygame.Rect(10, 70, 60, 50)},
    {"tool": "curve", "rect": pygame.Rect(10, 130, 60, 50)},
    {"tool": "rectangle", "rect": pygame.Rect(10, 190, 60, 50)},
    {"tool": "triangle", "rect": pygame.Rect(10, 250, 60, 50)},
    {"tool": "polygon", "rect": pygame.Rect(10, 310, 60, 50)},
    {"tool": "circle", "rect": pygame.Rect(10, 370, 60, 50)},
    {"tool": "ellipse", "rect": pygame.Rect(10, 430, 60, 50)},
    {"tool": "eraser", "rect": pygame.Rect(10, 490, 60, 50)},
    {"tool": "clear", "rect": pygame.Rect(10, 550, 60, 50)},
]

# Crear botones de color
colors = [
    {"color": black, "rect": pygame.Rect(1130, 10, 60, 50)},
    {"color": red, "rect": pygame.Rect(1130, 70, 60, 50)},
    {"color": blue, "rect": pygame.Rect(1130, 130, 60, 50)},
    {"color": green, "rect": pygame.Rect(1130, 190, 60, 50)},
    {"color": yellow, "rect": pygame.Rect(1130, 250, 60, 50)},
    {"color": cyan, "rect": pygame.Rect(1130, 310, 60, 50)},
    {"color": magenta, "rect": pygame.Rect(1130, 370, 60, 50)},
    {"color": purple, "rect": pygame.Rect(1130, 430, 60, 50)},
    {"color": brown, "rect": pygame.Rect(1130, 490, 60, 50)},
    {"color": orange, "rect": pygame.Rect(1130, 550, 60, 50)},
]

# Inicializar pantalla y reloj
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Iniciamos valores que nos controlan el color y la herramienta actual
current_color = black
current_tool = "pencil"
points = []
figures_draw = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
            
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Detectar herramientas
            for btn in buttons:
                if btn["rect"].collidepoint(event.pos):
                    points.clear()  # Limpiar puntos al cambiar de herramienta
                    current_tool = btn["tool"]
                    # Limpia completaente la pantalla
                    if current_tool == "clear":
                        figures_draw.clear()
                        current_tool = "pencil"
            
            # Detectar colores
            for color_btn in colors:
                if color_btn["rect"].collidepoint(event.pos):
                    current_color = color_btn["color"]
            
            # Iniciar dibujo
            if event.pos[0] > 80 and current_tool not in ["clear", "curve", "triangle", "polygon"] and event.pos[0] < 1117:
                drawing = True
                start_point = event.pos
                if current_tool not in ["pencil", "eraser"]: # Mientras no sea lápiz o borrador la herramienta actual, se tomarán varios puntos
                    points = [event.pos]
            if current_tool in ["curve", "triangle", "polygon"] and event.pos[0] > 80 and event.pos[0] < 1117:
                points.append(event.pos)  # Agregar el primer punto para la curva

        elif event.type == pygame.MOUSEMOTION and drawing:
            if event.pos[0] > 80 and event.pos[0] < 1117:
                end_point = event.pos
                if current_tool == "pencil":
                    figure = figures.Line(start_point, end_point, current_color, 4)
                    figures_draw.append(figure)
                    start_point = end_point
                elif current_tool == "eraser":
                    figure = figures.Line(start_point, end_point, (255, 255, 255), 30)
                    figures_draw.append(figure)
                    start_point = end_point

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False
            if current_tool not in ["pencil", "eraser", "curve", "triangle", "polygon"] and len(points) == 1 and event.pos[0] > 80:
                points.append(event.pos)
        
        elif event.type == pygame.MOUSEBUTTONDOWN and current_tool == "polygon" and event.button == 3:
            drawing = True
        
    screen.fill((255, 255, 255))

    # Dibujo de la figura seleccionada --------------------------------------------------------------------------------
    if len(points) == 2 and current_tool not in ["pencil", "eraser", "curve", "triangle", "polygon"]:
        if current_tool == "line":
            figure = figures.Line(points[0], points[1], current_color, 4)
        elif current_tool == "circle":
            figure = figures.Circle(points[0], points[1], current_color, 2)
        elif current_tool == "rectangle":
            figure = figures.Rectangle(points[0], points[1], current_color, 4)
        elif current_tool == "ellipse":
            figure = figures.Ellipse(points[0], points[1], current_color, 2)
        if figure:  # Asegurarnos que se creó una figura válida
            figures_draw.append(figure)
        points.clear()
    elif len(points) == 3 and current_tool == "triangle":
        # Si hay 3 puntos, se dibuja el triángulo y se añade a la lista de figuras
        figure = figures.Polygons(points.copy(), current_color, 4)
        figures_draw.append(figure)
        points.clear()
    elif len(points) == 4 and current_tool == "curve":
        # Si hay 4 puntos, se dibuja la curva y se añade a la lista de figuras
        figure = figures.Curve(points.copy(), current_color, 2)
        figures_draw.append(figure)
        points.clear()
    elif current_tool == "polygon":
        if drawing and len(points) > 1:
            # Si hay más de 4 puntos, se dibuja el polígono y se añade a la lista de figuras
            figure = figures.Polygons(points.copy(), current_color, 4)
            figures_draw.append(figure)
            points.clear()
            drawing = False
    
    # Dibujar dinamicamente la figura seleccionada
    if current_tool == "line" and drawing:
        points[0] = start_point
        end_point = event.pos
        figure = figures.Line(points[0], end_point, current_color, 4)
        figure.draw(screen)
    elif current_tool == "curve" and 2 <= len(points) <= 4:
        temp_points = points.copy()
        # Completamos los punto para ir visualizando poco a poco la curva
        while len(temp_points) < 4:
            temp_points.append(event.pos)
        temp_curve = figures.Curve(temp_points, current_color, 2)
        temp_curve.draw(screen)
    elif current_tool == "rectangle" and drawing:
        points[0] = start_point
        end_point = event.pos
        figure = figures.Rectangle(points[0], end_point, current_color, 4)
        figure.draw(screen)
    elif current_tool == "polygon" and len(points) > 1:
        for i in range(1, len(points)):
            start_point = points[i - 1]
            end_point = points[i]
            figure = figures.Line(start_point, end_point, current_color, 4)
            figure.draw(screen)
    elif current_tool == "triangle" and points:
        temp_points = points.copy()
        figure = figures.Polygons(temp_points, current_color, 4)
        figure.draw(screen)
    elif current_tool == "circle" and drawing:
        points[0] = start_point
        end_point = event.pos
        figure = figures.Circle(points[0], end_point, current_color, 2)
        figure.draw(screen)
    elif current_tool == "ellipse" and drawing:
        points[0] = start_point
        end_point = event.pos
        figure = figures.Ellipse(points[0], end_point, current_color, 2)
        figure.draw(screen)
    
    # Mostrar todas las figuras dibujadas
    for figure in figures_draw:
        if figure:  # Verificación adicional para evitar None
            figure.draw(screen)
    
    # Dibujo de la barra lateral y botones ------------------------------------------------------------------------------------------------
    figures.Buttons_shape((0, 0), (int(width * 0.07), height), (197, 204, 204), 0, 0).draw(screen) # Barra izquierda
    # Barra derecha
    figures.Buttons_shape((int(width * 0.93), 0), (width, height), (197, 204, 204), 0, 0).draw(screen) # Barra derecha
    
    for btn in buttons:
        tools.Button(screen, black, btn["rect"].x, btn["rect"].y, btn["rect"].width, btn["rect"].height).draw()
        
        if btn["tool"] == current_tool:
            figures.Buttons_shape((btn["rect"].x + 5, btn["rect"].y + 5), (btn["rect"].x + 55, btn["rect"].y + 45), green, 0, 4).draw(screen)
            
        # Dibujo icónico: puedes añadir una figura distinta para cada botón
        if btn["tool"] == "pencil": # Lápiz ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            screen.blit(pencil, (btn["rect"].x + 10, btn["rect"].y + 5))
        elif btn["tool"] == "line": # Línea ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            figures.Line((btn["rect"].x + 10, btn["rect"].y + 10), (btn["rect"].x + 50, btn["rect"].y + 40), black, 3).draw(screen)
        elif btn["tool"] == "curve": # Curva ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            figures.Curve(((btn["rect"].x + 10, btn["rect"].y + 10),(btn["rect"].x + 5, btn["rect"].y + 90),(btn["rect"].x + 50, btn["rect"].y - 40),(btn["rect"].x + 50, btn["rect"].y + 40)), black, 1).draw(screen)
        elif btn["tool"] == "rectangle": # Rectángulo ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
            figures.Rectangle((btn["rect"].x + 10, btn["rect"].y + 10), (btn["rect"].x + 50, btn["rect"].y + 40), black, 4).draw(screen)
        elif btn["tool"] == "triangle": # Triangle ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
            figures.Polygons(((btn["rect"].x + 10, btn["rect"].y + 40), (btn["rect"].x + 30, btn["rect"].y + 10), (btn["rect"].x + 50, btn["rect"].y + 40)), black, 4).draw(screen)
        elif btn["tool"] == "polygon": # Polygons ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
            figures.Polygons(((btn["rect"].x + 12, btn["rect"].y + 18), (btn["rect"].x + 30, btn["rect"].y + 10), (btn["rect"].x + 48, btn["rect"].y + 18), (btn["rect"].x + 42, btn["rect"].y + 40), (btn["rect"].x + 18, btn["rect"].y + 40)), black, 4).draw(screen)        
        elif btn["tool"] == "circle": # Círculo --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            figures.Circle((btn["rect"].x + 30, btn["rect"].y + 25), (btn["rect"].x + 47, btn["rect"].y + 30), black, 2).draw(screen)
        elif btn["tool"] == "ellipse": # Elípse --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            figures.Ellipse((btn["rect"].x + 30, btn["rect"].y + 25), (btn["rect"].x + 8 , btn["rect"].y + 10), black, 2).draw(screen)
        elif btn["tool"] == "eraser": # Borrador -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            screen.blit(eraser, (btn["rect"].x + 10, btn["rect"].y + 5))
        elif btn["tool"] == "clear": # Limpiar --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            screen.blit(broom, (btn["rect"].x + 10, btn["rect"].y + 5))
        
    # Dibujo de los botones de color ----------------------------------------------------------------------------------------------------------------------------------------
    for color_btn in colors:
        tools.Button(screen, black, color_btn["rect"].x, color_btn["rect"].y, color_btn["rect"].width, color_btn["rect"].height).draw()
        figures.Buttons_shape((color_btn["rect"].x + 10, color_btn["rect"].y + 10), (color_btn["rect"].x + 50, color_btn["rect"].y + 40), color_btn["color"], 0, 8).draw(screen)
    # ------------------------------------------------------------------------------------------------------------------------------------
    
    pygame.display.flip() 
    clock.tick(60)  
    
pygame.quit()