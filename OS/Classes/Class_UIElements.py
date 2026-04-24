import pygame
from constants import *

#  HELPERS
def draw_rect_border(surf, color, rect, radius=8, width=1):
    pygame.draw.rect(surf, color, rect, width, border_radius=radius)

def draw_rect_fill(surf, color, rect, radius=8):
    pygame.draw.rect(surf, color, rect, border_radius=radius)

def draw_text(surf, text, font, color, x, y, anchor="topleft"):
    s = font.render(text, True, color)
    r = s.get_rect()
    setattr(r, anchor, (x, y))
    surf.blit(s, r)

def lerp_color(a, b, t):
    return tuple(int(a[i] + (b[i]-a[i])*t) for i in range(3))

#  BUTTON
class Button:
    def __init__(self, rect, label, icon="", font=None, tag=None,
                 color_base=PANEL2, color_hover=BTN_HOVER, color_text=TEXT,
                 radius=8, border_color=BORDER, accent=ACCENT):
        self.rect         = pygame.Rect(rect)
        self.label        = label
        self.icon         = icon
        self.font         = font
        self.tag          = tag or label
        self.color_base   = color_base
        self.color_hover  = color_hover
        self.color_text   = color_text
        self.radius       = radius
        self.border_color = border_color
        self.accent       = accent
        self.hovered      = False
        self.active       = False
        self._t           = 0.0   # animation lerp

    def update(self, mx, my):
        self.hovered = self.rect.collidepoint(mx, my)
        target = 1.0 if (self.hovered or self.active) else 0.0
        self._t += (target - self._t) * 0.18

    def draw(self, surf):
        c = lerp_color(self.color_base, self.color_hover, self._t)
        draw_rect_fill(surf, c, self.rect, self.radius)
        bc = lerp_color(self.border_color, self.accent, self._t)
        draw_rect_border(surf, bc, self.rect, self.radius, 1)
        if self.font:
            lbl = f"{self.icon}  {self.label}" if self.icon else self.label
            draw_text(surf, lbl, self.font, self.color_text,
                      self.rect.centerx, self.rect.centery, anchor="center")

    def clicked(self, event):
        return (event.type == pygame.MOUSEBUTTONDOWN and
                event.button == 1 and self.rect.collidepoint(event.pos))

#  INPUT BOX
class InputBox:
    def __init__(self, rect, font, placeholder="", password=False):
        self.rect        = pygame.Rect(rect)
        self.font        = font
        self.placeholder = placeholder
        self.password    = password
        self.text        = ""
        self.active      = False
        self.cursor_vis  = True
        self._blink      = 0

    def handle(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key not in (pygame.K_RETURN, pygame.K_TAB):
                self.text += event.unicode

    def update(self):
        self._blink += 1
        if self._blink > 30:
            self._blink = 0
            self.cursor_vis = not self.cursor_vis

    def draw(self, surf):
        bc = ACCENT if self.active else BORDER
        draw_rect_fill(surf, PANEL2, self.rect, 6)
        draw_rect_border(surf, bc, self.rect, 6, 1)
        disp = ("•" * len(self.text)) if self.password else self.text
        if disp:
            draw_text(surf, disp, self.font, TEXT,
                      self.rect.x+12, self.rect.centery, anchor="midleft")
        elif not self.active:
            draw_text(surf, self.placeholder, self.font, TEXT_DIM,
                      self.rect.x+12, self.rect.centery, anchor="midleft")
        if self.active and self.cursor_vis:
            tw = self.font.size(disp)[0]
            cx = self.rect.x + 12 + tw + 2
            cy = self.rect.centery
            pygame.draw.line(surf, ACCENT, (cx, cy-10), (cx, cy+10), 2)

#  NOTIFICATION
class Notification:
    def __init__(self, msg, kind="info"):
        self.msg   = msg
        self.kind  = kind   # info | ok | error
        self.timer = 180
        self.alpha = 255

    @property
    def color(self):
        return {
            "ok":    GREEN,
            "error": RED,
            "info":  ACCENT3,
        }.get(self.kind, ACCENT3)

    def update(self):
        self.timer -= 1
        if self.timer < 60:
            self.alpha = max(0, int(self.alpha - 4))

    @property
    def alive(self):
        return self.timer > 0

    def draw(self, surf, font, y):
        s = pygame.Surface((420, 44), pygame.SRCALPHA)
        r = pygame.Rect(0, 0, 420, 44)
        col = self.color
        pygame.draw.rect(s, (*PANEL2, self.alpha), r, border_radius=8)
        pygame.draw.rect(s, (*col, self.alpha), r, 1, border_radius=8)
        pygame.draw.rect(s, (*col, min(self.alpha, 180)), (0, 0, 4, 44), border_radius=8)
        txt = font.render(self.msg, True, (*TEXT, self.alpha))
        s.blit(txt, (14, 12))
        surf.blit(s, (W - 440, y))

#  MODAL
class Modal:
    """Generic modal with a title, body text, input boxes, and action buttons."""
    def __init__(self, title, fields, buttons, font_title, font_body, width=440):
        self.title      = title
        self.inputs     = []
        for (label, ph, pw) in fields:
            self.inputs.append((label, InputBox((0,0,width-60,36), font_body, ph, pw)))
        self.btn_objs   = []
        for (lbl, tag, accent) in buttons:
            self.btn_objs.append(Button((0,0,120,36), lbl, font=font_body,
                                        tag=tag, accent=accent, color_base=PANEL2,
                                        color_hover=BTN_HOVER))
        self.font_title = font_title
        self.font_body  = font_body
        self.width      = width
        self._layout()

    def _layout(self):
        mw = self.width
        field_h = 60
        mh = 70 + len(self.inputs)*field_h + 60
        self.rect = pygame.Rect((W-mw)//2, (H-mh)//2, mw, mh)
        y = self.rect.y + 60
        for (lbl, inp) in self.inputs:
            inp.rect.topleft = (self.rect.x+30, y+20)
            y += field_h
        # buttons row
        bx = self.rect.x + 30
        by = self.rect.bottom - 54
        for btn in self.btn_objs:
            btn.rect.topleft = (bx, by)
            bx += 130

    def handle(self, event):
        for (_, inp) in self.inputs:
            inp.handle(event)

    def update(self, mx, my):
        for inp in [i for _,i in self.inputs]:
            inp.update()
        for btn in self.btn_objs:
            btn.update(mx, my)

    def draw(self, surf):
        # Overlay
        ov = pygame.Surface((W, H), pygame.SRCALPHA)
        ov.fill((0, 0, 0, 160))
        surf.blit(ov, (0,0))
        # Panel
        draw_rect_fill(surf, PANEL, self.rect, 12)
        draw_rect_border(surf, ACCENT, self.rect, 12, 1)
        # Title bar
        tbar = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, 46)
        draw_rect_fill(surf, PANEL2, tbar, 12)
        draw_text(surf, self.title, self.font_title, ACCENT,
                  self.rect.x+20, self.rect.y+12)
        # Fields
        y = self.rect.y + 60
        for (lbl, inp) in self.inputs:
            draw_text(surf, lbl, self.font_body, TEXT_DIM,
                      self.rect.x+30, y+2)
            inp.draw(surf)
            y += 60
        # Buttons
        for btn in self.btn_objs:
            btn.draw(surf)

    def get_values(self):
        return [inp.text for _, inp in self.inputs]

    def clicked_btn(self, event):
        for btn in self.btn_objs:
            if btn.clicked(event):
                return btn.tag
        return None