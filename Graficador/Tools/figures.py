import pygame
import numpy as np
import math

class Figure:
    '''
    Clase base para las figuras a dibujar.
    
    Atributos:
    start_point (tuple): Punto inicial de la figura (x, y).
    end_point (tuple): Punto final de la figura (x, y).
    color (tuple): Color de la figura en formato RGB.
    width (int): Ancho de la figura.
    '''
    def __init__(self, start_point, end_point, color, width):
        '''
        Inicializa la figura con los puntos, color y ancho.
        
        Argumentos:
        start_point: Punto inicial de la figura (x, y).
        end_point: Punto final de la figura (x, y).
        color: Color de la figura en formato RGB.
        width: Ancho de la figura.
        '''
        self.start_point = start_point
        self.end_point = end_point
        self.color = color
        self.width = width

class Buttons_shape(Figure):
    '''
    Dibuja un rectángulo usando los puntos inicial y final, calculando el ancho y el largo.
    '''
    def __init__(self, start_point, end_point, color, width, border):
        '''
        Inicializa el rectángulo con los puntos, color y ancho.
        
        Argumentos:
        border: Ancho del borde del rectángulo.
        '''
        super().__init__(start_point, end_point, color, width)
        self.border = border
    
    def draw(self, screen):
        '''
        Dibuja el rectángulo en la superficie dada.
        
        Argumentos:
        screen: Superficie donde se dibuja el rectángulo.
        '''
        x1, y1 = self.start_point
        x2, y2 = self.end_point
        border = self.border

        # Normalizamos el rectángulo (esquina superior izquierda + tamaño)
        left = min(x1, x2)
        top = min(y1, y2)
        width = abs(x2 - x1)
        height = abs(y2 - y1)

        rect = pygame.Rect(left, top, width, height)
        pygame.draw.rect(screen, self.color, rect, width=self.width, border_radius=border)

class Line(Figure):
    '''
    Clase para dibujar líneas, usando el algoritmo de Bresenham.
    '''
    def draw(self, screen):
        '''
        Dibuja la línea en la superficie dada.
        
        Argumentos:
        screen: Superficie donde se dibuja la línea.
        '''
        x0, y0 = self.start_point
        x1, y1 = self.end_point
        
        # Calcular diferencias para el algoritmo de Bresenham
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        
        # Determinar la dirección del paso
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        
        err = dx - dy 
        
        while True:
            # Dibujar el píxel actual
            pygame.draw.circle(screen, self.color, (x0, y0), self.width // 2)
            
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            # Si el error es mayor que la diferencia en X, se ajusta la coordenada Y
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy
        

class Circle(Figure):
    '''
    Dibuja un círculo usando el algoritmo de Bresenham.
    '''
    def draw(self, screen):
        '''
        Dibuja el círculo en la superficie dada.
        
        Argumentos:
        screen: Superficie donde se dibuja el círculo.
        '''
        x0, y0 = self.start_point  # Centro del círculo
        x1, y1 = self.end_point    # Punto para calcular el radio
        
        # Calcular radio usando distancia euclidiana (opcional, puedes usar solo la diferencia en X o Y si prefieres)
        radius = int(((x1 - x0)**2 + (y1 - y0)**2)**0.5)
        
        x = radius
        y = 0
        err = 0

        while x >= y:
            # Dibujar los 8 puntos simétricos del círculo
            self.draw_circle_points(screen, x0, y0, x, y)
            
            y += 1
            err += 1 + 2*y
            if 2*(err - x) + 1 > 0:
                x -= 1
                err += 1 - 2*x

    def draw_circle_points(self, screen, cx, cy, x, y):
        '''
        Dibuja los 8 puntos simétricos del círculo.
        
        Argumentos:
        screen: Superficie donde se dibuja el círculo.
        cx: Coordenada X del centro del círculo.
        cy: Coordenada Y del centro del círculo.
        x: Coordenada X del punto en el círculo.
        y: Coordenada Y del punto en el círculo.
        '''
        points = [
            (cx + x, cy + y), (cx - x, cy + y),
            (cx + x, cy - y), (cx - x, cy - y),
            (cx + y, cy + x), (cx - y, cy + x),
            (cx + y, cy - x), (cx - y, cy - x)
        ]
        for px, py in points:
            pygame.draw.circle(screen, self.color, (px, py), self.width)

class Curve(Figure):
    '''
    Dibuja una curva usando el algoritmo de Bezier para 4 puntos.
    
    Atributos:
    points (list): Lista de puntos de control para la curva.
    '''
    def __init__(self, points, color, width):
        '''
        Inicializa la curva con los puntos, color y ancho.
        
        Argumentos:
        points: Lista de puntos de control para la curva.
        color: Color de la curva en formato RGB.
        width: Ancho de la curva.
        '''
        super().__init__(points[0], points[-1], color, width)
        self.points = points
    
    def draw(self, screen):
        '''
        Dibuja la curva en la superficie dada.
        
        Argumentos:
        screen: Superficie donde se dibuja la curva.
        '''
        if len(self.points) < 4:
            return
        
        steps = np.linspace(0, 1, 500)
        
        for t in steps:
            x = int((1 - t)**3 * self.points[0][0] + 3 * (1 - t)**2 * t * self.points[1][0] + 3 * (1 - t) * t**2 * self.points[2][0] + t**3 * self.points[3][0])
            y = int((1 - t)**3 * self.points[0][1] + 3 * (1 - t)**2 * t * self.points[1][1] + 3 * (1 - t) * t**2 * self.points[2][1] + t**3 * self.points[3][1])
            pygame.draw.circle(screen, self.color, (x, y), self.width)

class Polygons(Figure):
    '''
    Dibuja un polígono usando los puntos dados.
    
    Atributos:
    points (list): Lista de puntos del polígono.
    '''
    def __init__(self, points, color, width):
        '''
        Inicializa el polígono con los puntos, color y ancho.
        
        Argumentos:
        points: Lista de puntos del polígono.
        color: Color del polígono en formato RGB.
        width: Ancho del polígono.
        '''
        super().__init__(points[0], points[-1], color, width)
        self.points = points
    
    def draw(self, screen):
        '''
        Dibuja el polígono en la superficie dada.
        
        Argumentos:
        screen: Superficie donde se dibuja el polígono.
        '''
        for i in range(len(self.points)):
            start_point = self.points[i]
            end_point = self.points[(i + 1) % len(self.points)]
            Line(start_point, end_point, self.color, self.width).draw(screen)

class Rectangle(Figure):
    '''
    Dibuja un rectángulo usando los puntos inicial y final, calculando el ancho y el largo.
    '''
    def draw(self, screen):
        '''
        Dibuja el rectángulo en la superficie dada.
        
        Argumentos:
        screen: Superficie donde se dibuja el rectángulo.
        '''
        x1, y1 = self.start_point
        x2, y2 = self.end_point
        
        points = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
        Polygons(points, self.color, self.width).draw(screen)

class Ellipse(Figure):
    '''
    Dibuja una elipse usando los puntos inicial y final, calculando el ancho y el largo.
    '''
    
    def draw(self, screen):
        '''
        Dibuja la elipse en la superficie dada.
        
        Argumentos:
        screen: Superficie donde se dibuja la elipse.
        '''
        cx, cy = self.start_point
        x1, y1 = self.end_point
        
        # Calcular los radios en x y en y usando la distancia euclidiana
        rx = abs(x1 - cx)
        ry = abs(y1 - cy)
        
        for t in np.linspace(0, 2 * math.pi, 500):
            x = cx - rx * math.cos(t)
            y = cy - ry * math.sin(t)
            pygame.draw.circle(screen, self.color, (int(x), int(y)), self.width)
