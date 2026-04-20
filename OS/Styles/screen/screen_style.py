import os
import sys
import subprocess
from pathlib import Path
import pygame as PG
from pygame import image
import builtins

BASE_DIR = Path(__file__).resolve().parents[2]
MINI_OS_PATH = BASE_DIR / 'mini_op.py'

# Import OS functions
sys.path.append(str(BASE_DIR))
import mini_op

class TextInput:
    def __init__(self, x, y, w, h, font, text=''):
        self.rect = PG.Rect(x, y, w, h)
        self.color = (255, 255, 255)
        self.text = text
        self.font = font
        self.txt_surface = font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == PG.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = (0, 255, 0) if self.active else (255, 255, 255)
        if event.type == PG.KEYDOWN:
            if self.active:
                if event.key == PG.K_RETURN:
                    entered_text = self.text
                    self.text = ''
                    return entered_text
                elif event.key == PG.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = self.font.render(self.text, True, self.color)
        return None

    def draw(self, screen):
        PG.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))

class TextDisplay:
    def __init__(self, x, y, w, h, font):
        self.rect = PG.Rect(x, y, w, h)
        self.lines = []
        self.font = font

    def add_text(self, text):
        self.lines.append(text)
        if len(self.lines) > 10:  # Limit lines
            self.lines.pop(0)

    def draw(self, screen):
        y_offset = self.rect.y
        for line in self.lines:
            txt_surface = self.font.render(line, True, (255, 255, 255))
            screen.blit(txt_surface, (self.rect.x, y_offset))
            y_offset += 20

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

def run_gui_os():
    screen = init_screen(size=(1000, 700), background_path=None)
    font = PG.font.SysFont("Arial", 24)

    # Buttons for menu
    buttons = {}
    menu_items = mini_op.MENU
    y_pos = 50
    for item in menu_items:
        buttons[item] = create_button(screen, (50, y_pos), (200, 50), (0, 120, 215), item, "Arial", 20, (255,255,255))
        y_pos += 60

    # Text input and display
    text_input = TextInput(300, 500, 400, 40, font)
    text_display = TextDisplay(300, 50, 600, 400, font)

    clock = PG.time.Clock()
    running = True
    current_user = None
    waiting_for_input = False
    input_prompt = ""
    input_callback = None

    # Override input and print
    original_input = builtins.input
    original_print = builtins.print

    def gui_input(prompt):
        nonlocal waiting_for_input, input_prompt
        text_display.add_text(prompt)
        waiting_for_input = True
        input_prompt = prompt
        return None  # Will be handled in loop

    def gui_print(*args, **kwargs):
        text = ' '.join(str(arg) for arg in args)
        text_display.add_text(text)

    builtins.input = gui_input
    builtins.print = gui_print

    while running:
        for event in PG.event.get():
            if event.type == PG.QUIT:
                running = False
            elif waiting_for_input:
                entered = text_input.handle_event(event)
                if entered is not None:
                    waiting_for_input = False
                    # Simulate input return
                    # This is tricky; for simplicity, store the input
                    gui_input_result = entered
                    # Call the callback if set
                    if input_callback:
                        input_callback(gui_input_result)
            else:
                for item, btn in buttons.items():
                    if is_button_clicked(event, btn):
                        if current_user is None:
                            # Login first
                            text_display.add_text("Usuari i contrasenya")
                            # Prompt for username
                            def set_username(uname):
                                nonlocal current_user, input_callback
                                current_user = uname
                                text_display.add_text("Introdueix la teva contrasenya: ")
                                def set_password(pwd):
                                    nonlocal current_user
                                    if mini_op.authenticate_user(current_user, pwd):
                                        text_display.add_text("Benvingut")
                                        current_user = uname
                                    else:
                                        text_display.add_text("Usuari o contrasenya incorrectes")
                                        current_user = None
                                input_callback = set_password
                            input_callback = set_username
                            waiting_for_input = True
                            input_prompt = "Introdueix el teu usuari: "
                        else:
                            # Handle menu item
                            if item == 'exit':
                                running = False
                            elif item == 'descareges':
                                mini_op.show_descareges(mini_op.DESCAREGES, current_user)
                            elif item == 'musica':
                                mini_op.musica(mini_op.MUSICA_CONTENT, current_user)
                            elif item == 'video':
                                mini_op.video(mini_op.VIDEO_CONTENT, current_user)
                            elif item == 'imatges':
                                mini_op.show_imatges(mini_op.IMATGES, current_user)
                            elif item == 'documents':
                                mini_op.docs(mini_op.DOCUMENTS, current_user)
                            elif item == 'calculadora MRUA':
                                text_display.add_text("Tria la incògnita: " + ', '.join(mini_op.CALCULADORA_MRUA))
                                # This needs more handling for sub-inputs
                                # For rapid, just call the function
                                gui_print(sorted(mini_op.CALCULADORA_MRUA))
                                # Etc.
                            elif item == 'configuracio':
                                mini_op.Config(mini_op.USERS, current_user)
                            elif item == 'viatjar':
                                text_display.add_text("https://landbot.online/v3/H-2775206-6P3AOFD16UGVM00S/index.html")

        screen.fill((30, 30, 30))
        for btn in buttons.values():
            PG.draw.rect(screen, (0, 120, 215), btn)
            # Redraw text
        text_display.draw(screen)
        text_input.draw(screen)
        PG.display.flip()
        clock.tick(60)

    # Restore builtins
    builtins.input = original_input
    builtins.print = original_print
    PG.quit()

if __name__ == '__main__':
    run_gui_os()
