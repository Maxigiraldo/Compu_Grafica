import pygame   
import Tools.figures as figures

class Button:
    '''
    Clase para crear cada botón en la pantalla.
    
    Atributos:
    screen (pygame.Surface): Superficie donde se dibuja el botón.
    color (tuple): Color del botón en formato RGB.
    x (int): Coordenada X de la esquina superior izquierda del botón.
    y (int): Coordenada Y de la esquina superior izquierda del botón.
    width (int): Ancho del botón.
    height (int): Alto del botón.
    
    '''
    def __init__(self, screen, color, x, y, width, height):
        '''
        Inicializa el botón con la superficie, color y dimensiones.
        
        Argumentos:
        
        screen: Superficie donde se dibuja el botón.
        color: Color del botón en formato RGB.
        x: Coordenada X de la esquina superior izquierda del botón.
        y: Coordenada Y de la esquina superior izquierda del botón.
        width: Ancho del botón.
        height: Alto del botón.
        
        '''
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        '''
        Dibuja el botón en la superficie con los valores dados.
        '''
        figures.Buttons_shape((self.x, self.y), (self.x + self.width, self.y + self.height), self.color, 4, 8).draw(self.screen)
        
