import os
import sys
import subprocess
from pathlib import Path

import pygame as PG
from pygame import image

BASE_DIR = Path(__file__).resolve().parents[2]
MINI_OS_PATH = BASE_DIR / 'mini_op.py'


def init_screen(size=(800, 600), background_path=None):
    PG.init()
    PG.font.init()
    display = PG.display.set_mode(size)
    if background_path:
        background = image.load(background_path)
        display.blit(background, (0, 0))
    else:
        display.fill((30, 30, 30))
    PG.display.flip()
    return display


def create_button(surface, position, size, color, text='', font_name="Arial", font_size=24, text_color=(0, 0, 0)):
    rect = PG.Rect(position, size)
    PG.draw.rect(surface, color, rect)
    if text:
        font = PG.font.SysFont(font_name, font_size)
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=rect.center)
        surface.blit(text_surface, text_rect)
    PG.display.flip()
    return rect


def is_button_clicked(event, button_rect):
    return event.type == PG.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos)


def launch_os():
    if not MINI_OS_PATH.exists():
        print(f"No s'ha trobat {MINI_OS_PATH}")
        return

    command = [sys.executable, str(MINI_OS_PATH)]
    kwargs = {'cwd': str(BASE_DIR)}
    if sys.platform.startswith('win'):
        kwargs['creationflags'] = subprocess.CREATE_NEW_CONSOLE

    subprocess.Popen(command, **kwargs)


def run_button_app():
    screen = init_screen(size=(800, 600), background_path=None)
    start_button = create_button(
        surface=screen,
        position=(300, 220),
        size=(200, 70),
        color=(0, 120, 215),
        text='Obrir Mini OS',
        font_name='Arial',
        font_size=28,
        text_color=(255, 255, 255),
    )
    quit_button = create_button(
        surface=screen,
        position=(300, 320),
        size=(200, 70),
        color=(200, 50, 50),
        text='Sortir',
        font_name='Arial',
        font_size=28,
        text_color=(255, 255, 255),
    )

    clock = PG.time.Clock()
    running = True

    while running:
        for event in PG.event.get():
            if event.type == PG.QUIT:
                running = False
            elif is_button_clicked(event, start_button):
                launch_os()
            elif is_button_clicked(event, quit_button):
                running = False

        PG.display.update([start_button, quit_button])
        clock.tick(60)

    PG.quit()


if __name__ == '__main__':
    run_button_app()
