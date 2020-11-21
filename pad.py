import pygame
import random


class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)


def main():
    pygame.init()
    pygame.joystick.init()

    pad = pygame.joystick.Joystick(0)
    width, height = 1280, 720
    screen = pygame.display
    surface = screen.set_mode((width, height))

    pad_name = pad.get_name()
    pygame.display.set_caption(f"{pad_name} - rysowanie")

    # pozycja kursora w oknie (domyslnie srodek okna)
    position_x = width / 2
    position_y = height / 2
    # szybkosc poruszania sie kursora
    speed = 0.5
    running = True
    drawing = False
    # kolor rysowania (domyslnie czarny)
    color = (0, 0, 0)
    # wielkosc kursora
    radius = 25
    # wszystkie  narysowane  okregi
    circles = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.JOYBUTTONDOWN:
                # obsługa przycisków kontrolera (przycisk A - lewy  przycisk  myszki)
                # A=0 - rysowanie
                # B=1 - wolniej
                # X=2 - szybciej
                # Y=3 - zmiana na losowy kolor
                # LB=4 - mniejszy kursor
                # RB=5 - większy kursor
                if pad.get_button(0):
                    drawing = True
                if pad.get_button(1):
                    speed *= 0.5
                if pad.get_button(2):
                    speed *= 2
                if pad.get_button(3):
                    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                if pad.get_button(4):
                    if radius != 0:
                        radius -= 1
                if pad.get_button(5):
                    radius += 1
            if event.type == pygame.JOYBUTTONUP:
                if not pad.get_button(0):
                    drawing = False

        surface.fill((255, 255, 255))

        # rysowanie wszystkich okręgów, które zostały narysowane
        for circle in circles:
            circle.draw(surface)

        # przemieszczanie kursora za pomoca lewej gałki kontrolera
        position_x += pad.get_axis(0) * speed
        position_y += pad.get_axis(1) * speed

        # rysowanie kursora
        pygame.draw.circle(surface, (0, 0, 0), (position_x, position_y), radius)

        if drawing:
            circles.append(Circle(position_x, position_y, radius, color))

        screen.update()


if __name__ == '__main__':
    main()
