import pygame
import sys
import time
import math

#  CONFIG 
W, H = 1100, 700
FPS  = 60

#  PALETTE 
BG        = (10,  12,  20)
PANEL     = (18,  22,  36)
PANEL2    = (22,  28,  46)
ACCENT    = (0,  220, 180)
ACCENT2   = (255, 90, 120)
ACCENT3   = (90, 160, 255)
TEXT      = (220, 235, 255)
TEXT_DIM  = (90, 110, 150)
BORDER    = (40,  55,  80)
BTN_HOVER = (30,  40,  65)
BTN_ACT   = (0,  180, 140)
RED       = (220,  60,  80)
GREEN     = (60,  210, 130)
YELLOW    = (255, 200,  60)
WHITE     = (255, 255, 255)

#  DATA 
USERS = {"admin": "admin", "user1": "123", "familia": "123", "convidats": "123"}

DESCAREGES    = ["ghub", "steam", "arxiu.zip", "lightroom"]
MUSICA_LIST   = ["ja dormire", "La Familia", "2002", "dins del meu cap"]
VIDEO_LIST    = ["familia 90 anys", "27/11/2020"]
IMATGES_LIST  = ["img 0078.jpg", "img 6534.jpg", "img 2437.jpg"]
DOCUMENTS_LIST= ["document 0078.doc", "grammar practice.doc", "els mobils i la falta de son"]

MRUA_OPTS     = ["a  (acceleració)", "Av (Δv)", "At (Δt)", "Vf (vel. final)", "Xf (posició final)"]

MENU_ITEMS = [
    ("descàrregues", "⬇"),
    ("música",       "♪"),
    ("vídeo",        "▶"),
    ("imatges",      "🖼"),
    ("documents",    "📄"),
    ("calc. MRUA",   "⚡"),
    ("configuració", "⚙"),
    ("exit",         "✕"),
]

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

#  MAIN APP 
class MiniOS:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((W, H))
        pygame.display.set_caption("MiniOS v2.0")
        self.clock  = pygame.time.Clock()

        # Fonts
        pygame.font.init()
        self.f_title  = pygame.font.SysFont("Courier New", 22, bold=True)
        self.f_sub    = pygame.font.SysFont("Courier New", 15, bold=True)
        self.f_body   = pygame.font.SysFont("Courier New", 14)
        self.f_small  = pygame.font.SysFont("Courier New", 12)
        self.f_big    = pygame.font.SysFont("Courier New", 28, bold=True)
        self.f_icon   = pygame.font.SysFont("Segoe UI Emoji", 18)

        self.state    = "login"   # login | desktop | section | modal_*
        self.current_user = None
        self.section  = None      # active section key
        self.selected = None      # selected item inside section
        self.notifs   = []
        self.modal    = None
        self.modal_ctx= {}        # extra context for modal callbacks
        self.tick     = 0

        # MRUA state
        self.mrua_result = None
        self.mrua_step   = "choose"  # choose | input | result
        self.mrua_opt    = None
        self.mrua_fields = []
        self.mrua_vals   = {}
        self.mrua_inputs = []

        # Config state
        self.config_sub  = None

        self._build_login()

    #  NOTIFICATIONS 
    def notify(self, msg, kind="info"):
        self.notifs.append(Notification(msg, kind))

    #  LOGIN 
    def _build_login(self):
        cx = W//2
        self.login_user = InputBox((cx-150, 300, 300, 40), self.f_body,
                                   "nom d'usuari")
        self.login_pass = InputBox((cx-150, 360, 300, 40), self.f_body,
                                   "contrasenya", password=True)
        self.login_btn  = Button((cx-80, 420, 160, 42), "Entrar", font=self.f_sub,
                                  accent=ACCENT, color_base=PANEL2,
                                  color_hover=BTN_HOVER)

    def _try_login(self):
        u = self.login_user.text.strip()
        p = self.login_pass.text
        if USERS.get(u) == p:
            self.current_user = u
            self.state = "desktop"
            self.notify(f"Benvingut, {u}!", "ok")
            self._build_desktop()
        else:
            self.notify("Usuari o contrasenya incorrectes.", "error")
            self.login_pass.text = ""

    #  DESKTOP 
    def _build_desktop(self):
        self.menu_btns = []
        cols, rows = 4, 2
        bw, bh = 200, 80
        gx, gy = 30, 140
        gap    = 18
        for i, (lbl, icon) in enumerate(MENU_ITEMS):
            c = i % cols
            r = i // cols
            x = gx + c*(bw+gap)
            y = gy + r*(bh+gap)
            self.menu_btns.append(
                Button((x, y, bw, bh), lbl, icon=icon, font=self.f_sub,
                       tag=lbl, accent=ACCENT, color_base=PANEL2,
                       color_hover=BTN_HOVER, radius=10)
            )

    #  SECTION 
    def _build_section(self, key):
        self.section   = key
        self.state     = "section"
        self.selected  = None
        self.item_btns = []
        items = self._section_items(key)
        for i, item in enumerate(items):
            self.item_btns.append(
                Button((360, 130+i*52, 380, 42), item, font=self.f_body,
                       tag=item, accent=ACCENT3, color_base=PANEL2,
                       color_hover=BTN_HOVER, radius=8)
            )
        self.back_btn = Button((20, 20, 110, 36), "← Enrere", font=self.f_body,
                                tag="back", accent=ACCENT, color_base=PANEL2,
                                color_hover=BTN_HOVER, radius=8)
        if key in ("música","vídeo","imatges","documents","descàrregues"):
            self.action_btn = Button((360, H-70, 180, 40), "Obrir/Reproduir",
                                      font=self.f_body, tag="action",
                                      accent=ACCENT, color_base=PANEL2,
                                      color_hover=BTN_HOVER, radius=8)
        else:
            self.action_btn = None

    def _section_items(self, key):
        return {
            "descàrregues": sorted(DESCAREGES),
            "música":       sorted(MUSICA_LIST),
            "vídeo":        sorted(VIDEO_LIST),
            "imatges":      sorted(IMATGES_LIST),
            "documents":    sorted(DOCUMENTS_LIST),
        }.get(key, [])

    def _can_access(self, key):
        restricted = ("música","vídeo","imatges","documents","descàrregues")
        if key in restricted:
            return self.current_user in ("admin","familia")
        return True

    def _open_action(self):
        if self.selected is None:
            self.notify("Selecciona un element primer.", "info")
            return
        if self.current_user not in ("admin","familia"):
            self.notify("No tens permisos.", "error")
            return
        # Always ask admin confirmation
        self._open_admin_modal(f"Confirma per obrir: {self.selected}")

    def _open_admin_modal(self, ctx_msg="Autenticació admin"):
        self.modal_ctx["reason"] = ctx_msg
        self.modal = Modal(
            "Autenticació d'administrador",
            [("Usuari admin", "admin", False),
             ("Contrasenya", "", True)],
            [("Confirmar", "confirm", ACCENT),
             ("Cancel·lar", "cancel", RED)],
            self.f_sub, self.f_body
        )
        self.state = "modal_admin"

    def _confirm_admin(self, vals):
        return vals[0] == "admin" and USERS.get("admin") == vals[1]

    #  CONFIG 
    def _build_config(self):
        self.section  = "configuració"
        self.state    = "config"
        self.cfg_btns = []
        opts = [("Afegir usuari","add"), ("Treure usuari","remove"),
                ("Editar usuari","edit")]
        for i,(lbl,tag) in enumerate(opts):
            self.cfg_btns.append(
                Button((360, 150+i*62, 280, 46), lbl, font=self.f_sub,
                       tag=tag, accent=ACCENT2, color_base=PANEL2,
                       color_hover=BTN_HOVER, radius=8)
            )
        self.back_btn = Button((20, 20, 110, 36), "← Enrere", font=self.f_body,
                                tag="back", accent=ACCENT, color_base=PANEL2,
                                color_hover=BTN_HOVER, radius=8)

    def _open_add_user(self):
        self.modal = Modal(
            "Afegir usuari",
            [("Nom d'usuari", "nou usuari", False),
             ("Contrasenya",  "contrasenya", True)],
            [("Afegir","add", ACCENT), ("Cancel·lar","cancel", RED)],
            self.f_sub, self.f_body
        )
        self.state = "modal_add"

    def _open_remove_user(self):
        self.modal = Modal(
            "Treure usuari",
            [("Nom d'usuari a treure", "usuari", False)],
            [("Treure","remove", ACCENT2), ("Cancel·lar","cancel", RED)],
            self.f_sub, self.f_body
        )
        self.state = "modal_remove"

    def _open_edit_user(self):
        self.modal = Modal(
            "Editar usuari",
            [("Nom d'usuari", "usuari", False),
             ("Nova contrasenya", "contrasenya", True)],
            [("Guardar","edit", ACCENT), ("Cancel·lar","cancel", RED)],
            self.f_sub, self.f_body
        )
        self.state = "modal_edit"

    #  MRUA 
    def _build_mrua(self):
        self.section   = "calc. MRUA"
        self.state     = "mrua"
        self.mrua_step = "choose"
        self.mrua_opt  = None
        self.mrua_result = None
        self.mrua_inputs = []
        self.back_btn  = Button((20, 20, 110, 36), "← Enrere", font=self.f_body,
                                 tag="back", accent=ACCENT, color_base=PANEL2,
                                 color_hover=BTN_HOVER, radius=8)
        self.calc_btn  = Button((360, H-70, 160, 40), "Calcular",
                                 font=self.f_body, tag="calc",
                                 accent=ACCENT, color_base=PANEL2,
                                 color_hover=BTN_HOVER, radius=8)
        self._mrua_choice_btns()

    def _mrua_choice_btns(self):
        self.mrua_choice_btns = []
        opts = [
            ("a  – acceleració", "a"),
            ("Δv – canvi velocitat", "Av"),
            ("Δt – interval temps",  "At"),
            ("Vf – velocitat final",  "Vf"),
            ("Xf – posició final",    "Xf"),
        ]
        for i, (lbl, tag) in enumerate(opts):
            self.mrua_choice_btns.append(
                Button((360, 130+i*54, 360, 42), lbl, font=self.f_body,
                       tag=tag, accent=ACCENT3, color_base=PANEL2,
                       color_hover=BTN_HOVER, radius=8)
            )

    def _mrua_build_inputs(self, opt):
        fields = {
            "a":  [("Velocitat inicial (m/s)", "Vo"),
                   ("Velocitat final (m/s)",   "Vf"),
                   ("Temps inicial (s)",        "To"),
                   ("Temps final (s)",          "Tf")],
            "Av": [("Acceleració (m/s²)", "a"),
                   ("Temps inicial (s)",   "To"),
                   ("Temps final (s)",     "Tf")],
            "At": [("Acceleració (m/s²)",       "a"),
                   ("Velocitat inicial (m/s)",   "Vo"),
                   ("Velocitat final (m/s)",     "Vf")],
            "Vf": [("Velocitat inicial (m/s)", "Vo"),
                   ("Acceleració (m/s²)",       "a"),
                   ("Temps inicial (s)",         "To"),
                   ("Temps final (s)",           "Tf")],
            "Xf": [("Velocitat inicial (m/s)", "Vo"),
                   ("Posició inicial (m)",      "Xo"),
                   ("Acceleració (m/s²)",       "a"),
                   ("Temps final (s)",          "Tf"),
                   ("Temps inicial (s)",        "To")],
        }
        self.mrua_field_defs = fields[opt]
        self.mrua_inputs = [
            (lbl, var, InputBox((360, 130+i*54, 320, 38), self.f_body, f"{lbl}…"))
            for i, (lbl, var) in enumerate(self.mrua_field_defs)
        ]

    def _mrua_compute(self):
        try:
            vals = {var: float(inp.text) for (_, var, inp) in self.mrua_inputs}
        except ValueError:
            self.notify("Introdueix valors numèrics vàlids.", "error")
            return
        opt = self.mrua_opt
        try:
            if opt == "a":
                r = (vals["Vf"]-vals["Vo"]) / (vals["Tf"]-vals["To"])
            elif opt == "Av":
                r = vals["a"] * (vals["Tf"]-vals["To"])
            elif opt == "At":
                r = (vals["Vf"]-vals["Vo"]) / vals["a"]
            elif opt == "Vf":
                r = vals["Vo"] + vals["a"]*(vals["Tf"]-vals["To"])
            elif opt == "Xf":
                r = vals["Xo"] + vals["Vo"]*(vals["Tf"]-vals["To"]) + \
                    0.5*vals["a"]*(vals["Tf"]-vals["To"])**2
        except ZeroDivisionError:
            self.notify("Divisió per zero!", "error")
            return
        self.mrua_result = r
        self.mrua_step   = "result"
        self.notify(f"Resultat: {round(r,4)}", "ok")

    #  DRAW HELPERS 
    def _draw_bg(self):
        self.screen.fill(BG)
        # Subtle grid
        for x in range(0, W, 40):
            pygame.draw.line(self.screen, (20,28,45), (x, 0), (x, H))
        for y in range(0, H, 40):
            pygame.draw.line(self.screen, (20,28,45), (0, y), (W, y))
        # Decorative corner accent
        pygame.draw.line(self.screen, ACCENT, (0, H-2), (W, H-2), 2)

    def _draw_taskbar(self):
        bar = pygame.Rect(0, 0, W, 50)
        draw_rect_fill(self.screen, PANEL2, bar)
        pygame.draw.line(self.screen, ACCENT, (0, 50), (W, 50), 1)
        draw_text(self.screen, "MiniOS v2.0", self.f_title, ACCENT, 20, 14)
        if self.current_user:
            ustr = f"● {self.current_user.upper()}"
            draw_text(self.screen, ustr, self.f_sub, GREEN, W-20, 14, anchor="topright")
        t = time.strftime("%H:%M:%S")
        draw_text(self.screen, t, self.f_body, TEXT_DIM, W//2, 14, anchor="midtop")

    def _draw_notifications(self):
        alive = [n for n in self.notifs if n.alive]
        self.notifs = alive
        for i, n in enumerate(alive[-4:]):
            n.update()
            n.draw(self.screen, self.f_body, H - 60 - i*52)

    #  LOGIN DRAW 
    def _draw_login(self):
        self._draw_bg()
        # Big title
        draw_text(self.screen, "MiniOS", self.f_big, ACCENT, W//2, 180, anchor="center")
        draw_text(self.screen, "sistema d'autenticació", self.f_body, TEXT_DIM,
                  W//2, 220, anchor="center")
        # Panel
        panel = pygame.Rect(W//2-190, 260, 380, 220)
        draw_rect_fill(self.screen, PANEL, panel, 12)
        draw_rect_border(self.screen, BORDER, panel, 12, 1)
        draw_text(self.screen, "Usuari:", self.f_small, TEXT_DIM, W//2-150, 285)
        self.login_user.draw(self.screen)
        draw_text(self.screen, "Contrasenya:", self.f_small, TEXT_DIM, W//2-150, 345)
        self.login_pass.draw(self.screen)
        self.login_btn.draw(self.screen)
        # Hint
        draw_text(self.screen, "usuaris: admin/admin  familia/123  convidats/123",
                  self.f_small, TEXT_DIM, W//2, 480, anchor="center")

    #  DESKTOP DRAW 
    def _draw_desktop(self):
        self._draw_bg()
        self._draw_taskbar()
        draw_text(self.screen, "ESCRIPTORI", self.f_sub, TEXT_DIM, 30, 62)
        for btn in self.menu_btns:
            btn.draw(self.screen)

    #  SECTION DRAW 
    def _draw_section(self):
        self._draw_bg()
        self._draw_taskbar()
        # Sidebar
        sidebar = pygame.Rect(0, 50, 340, H-50)
        draw_rect_fill(self.screen, PANEL, sidebar)
        pygame.draw.line(self.screen, BORDER, (340, 50), (340, H), 1)
        draw_text(self.screen, self.section.upper(), self.f_title, ACCENT, 20, 70)
        # Permission info
        perm = "accés complet" if self.current_user in ("admin","familia") else "només lectura"
        pcol = GREEN if self.current_user in ("admin","familia") else YELLOW
        draw_text(self.screen, f"● {perm}", self.f_small, pcol, 20, 100)
        # Items
        draw_text(self.screen, "Contingut disponible:", self.f_sub, TEXT_DIM, 360, 100)
        for btn in self.item_btns:
            btn.active = (btn.tag == self.selected)
            btn.draw(self.screen)
        if self.action_btn:
            self.action_btn.draw(self.screen)
        self.back_btn.draw(self.screen)

    #  CONFIG DRAW 
    def _draw_config(self):
        self._draw_bg()
        self._draw_taskbar()
        sidebar = pygame.Rect(0, 50, 340, H-50)
        draw_rect_fill(self.screen, PANEL, sidebar)
        pygame.draw.line(self.screen, BORDER, (340, 50), (340, H), 1)
        draw_text(self.screen, "CONFIGURACIÓ", self.f_title, ACCENT, 20, 70)
        if self.current_user == "admin":
            draw_text(self.screen, "● administrador", self.f_small, GREEN, 20, 100)
            draw_text(self.screen, "Gestió d'usuaris:", self.f_sub, TEXT_DIM, 360, 100)
            for btn in self.cfg_btns:
                btn.draw(self.screen)
            # User list
            draw_text(self.screen, "Usuaris actius:", self.f_sub, TEXT_DIM, 360, 360)
            for i, (u, p) in enumerate(USERS.items()):
                col = ACCENT if u == "admin" else TEXT
                draw_text(self.screen, f"  {u}", self.f_body, col, 360, 392+i*24)
        else:
            draw_text(self.screen, "Accés denegat.", self.f_sub, RED, 360, 200)
            draw_text(self.screen, "Necessites ser administrador.", self.f_body,
                      TEXT_DIM, 360, 230)
        self.back_btn.draw(self.screen)

    #  MRUA DRAW 
    def _draw_mrua(self):
        self._draw_bg()
        self._draw_taskbar()
        sidebar = pygame.Rect(0, 50, 340, H-50)
        draw_rect_fill(self.screen, PANEL, sidebar)
        pygame.draw.line(self.screen, BORDER, (340, 50), (340, H), 1)
        draw_text(self.screen, "CALC. MRUA", self.f_title, ACCENT, 20, 70)
        draw_text(self.screen, "Moviment Rectilini", self.f_small, TEXT_DIM, 20, 100)
        draw_text(self.screen, "Uniformement Accelerat", self.f_small, TEXT_DIM, 20, 118)

        if self.mrua_step == "choose":
            draw_text(self.screen, "Tria la incògnita:", self.f_sub, TEXT_DIM, 360, 100)
            for btn in self.mrua_choice_btns:
                btn.draw(self.screen)

        elif self.mrua_step == "input":
            lbl_map = {"a":"acceleració","Av":"Δv","At":"Δt","Vf":"Vf","Xf":"Xf"}
            draw_text(self.screen, f"Calculant: {lbl_map.get(self.mrua_opt,'')}",
                      self.f_sub, ACCENT3, 360, 100)
            for (lbl, var, inp) in self.mrua_inputs:
                draw_text(self.screen, lbl+":", self.f_small, TEXT_DIM,
                          360, inp.rect.y-16)
                inp.draw(self.screen)
            self.calc_btn.draw(self.screen)

        elif self.mrua_step == "result":
            lbl_map = {"a":"a (m/s²)","Av":"Δv (m/s)","At":"Δt (s)",
                       "Vf":"Vf (m/s)","Xf":"Xf (m)"}
            draw_text(self.screen, "Resultat:", self.f_sub, TEXT_DIM, 360, 120)
            res_txt = f"{round(self.mrua_result, 6)}"
            draw_text(self.screen, res_txt, self.f_big, ACCENT, 360, 160)
            draw_text(self.screen, lbl_map.get(self.mrua_opt,""), self.f_body,
                      TEXT_DIM, 360, 210)
            # Km/h conversion
            kmh = self.mrua_result * 3.6
            draw_text(self.screen, f"≈ {round(kmh,4)} km/h (si és velocitat)",
                      self.f_small, TEXT_DIM, 360, 250)
            retry = Button((360, 310, 200, 40), "Nou càlcul", font=self.f_body,
                            tag="retry", accent=ACCENT, color_base=PANEL2,
                            color_hover=BTN_HOVER, radius=8)
            retry.update(*pygame.mouse.get_pos())
            retry.draw(self.screen)
            self._mrua_retry_btn = retry

        self.back_btn.draw(self.screen)

    #  EVENT LOOP 
    def run(self):
        while True:
            mx, my = pygame.mouse.get_pos()
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()

                #  LOGIN 
                if self.state == "login":
                    self.login_user.handle(event)
                    self.login_pass.handle(event)
                    if self.login_btn.clicked(event):
                        self._try_login()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        self._try_login()

                #  DESKTOP 
                elif self.state == "desktop":
                    for btn in self.menu_btns:
                        if btn.clicked(event):
                            tag = btn.tag
                            if tag == "exit":
                                pygame.quit(); sys.exit()
                            elif tag == "configuració":
                                if self.current_user == "admin":
                                    self._build_config()
                                else:
                                    self.notify("Necessites ser administrador.", "error")
                            elif tag == "calc. MRUA":
                                self._build_mrua()
                            elif tag == "viatjar":
                                self.notify("URL: landbot.online/v3/H-2775206…", "info")
                            elif tag in ("descàrregues","música","vídeo",
                                         "imatges","documents"):
                                if self._can_access(tag):
                                    self._build_section(tag)
                                else:
                                    self.notify("No tens permisos per accedir.", "error")

                #  SECTION 
                elif self.state == "section":
                    if self.back_btn.clicked(event):
                        self.state = "desktop"
                    for btn in self.item_btns:
                        if btn.clicked(event):
                            self.selected = btn.tag
                    if self.action_btn and self.action_btn.clicked(event):
                        self._open_action()

                #  CONFIG 
                elif self.state == "config":
                    if self.back_btn.clicked(event):
                        self.state = "desktop"
                    for btn in self.cfg_btns:
                        if btn.clicked(event):
                            if btn.tag == "add":
                                self._open_add_user()
                            elif btn.tag == "remove":
                                self._open_remove_user()
                            elif btn.tag == "edit":
                                self._open_edit_user()

                #  MRUA 
                elif self.state == "mrua":
                    if self.back_btn.clicked(event):
                        self.state = "desktop"
                    if self.mrua_step == "choose":
                        for btn in self.mrua_choice_btns:
                            if btn.clicked(event):
                                self.mrua_opt = btn.tag
                                self._mrua_build_inputs(btn.tag)
                                self.mrua_step = "input"
                    elif self.mrua_step == "input":
                        for (_, _, inp) in self.mrua_inputs:
                            inp.handle(event)
                        if self.calc_btn.clicked(event):
                            self._mrua_compute()
                    elif self.mrua_step == "result":
                        if hasattr(self, "_mrua_retry_btn") and \
                                self._mrua_retry_btn.clicked(event):
                            self.mrua_step = "choose"

                # MODAL ADMIN 
                elif self.state == "modal_admin":
                    self.modal.handle(event)
                    tag = self.modal.clicked_btn(event)
                    if tag == "confirm":
                        vals = self.modal.get_values()
                        if self._confirm_admin(vals):
                            item = self.selected or "element"
                            self.notify(f"Obert: {item}", "ok")
                        else:
                            self.notify("Autenticació admin incorrecta.", "error")
                        self.modal = None
                        self.state = "section"
                    elif tag == "cancel":
                        self.modal = None
                        self.state = "section"

                #  MODAL ADD 
                elif self.state == "modal_add":
                    self.modal.handle(event)
                    tag = self.modal.clicked_btn(event)
                    if tag == "add":
                        vals = self.modal.get_values()
                        nou, pw = vals[0].strip(), vals[1]
                        if not nou:
                            self.notify("Nom d'usuari invàlid.", "error")
                        elif nou in USERS:
                            self.notify(f"Usuari '{nou}' ja existeix.", "error")
                        else:
                            USERS[nou] = pw
                            self.notify(f"Usuari '{nou}' afegit.", "ok")
                            self.modal = None
                            self.state = "config"
                    elif tag == "cancel":
                        self.modal = None
                        self.state = "config"

                #MODAL REMOVE 
                elif self.state == "modal_remove":
                    self.modal.handle(event)
                    tag = self.modal.clicked_btn(event)
                    if tag == "remove":
                        vals = self.modal.get_values()
                        u = vals[0].strip()
                        if u == "admin":
                            self.notify("No es pot treure l'administrador.", "error")
                        elif u in USERS:
                            del USERS[u]
                            self.notify(f"Usuari '{u}' eliminat.", "ok")
                            self.modal = None
                            self.state = "config"
                        else:
                            self.notify(f"Usuari '{u}' no existeix.", "error")
                    elif tag == "cancel":
                        self.modal = None
                        self.state = "config"

                #  MODAL EDIT 
                elif self.state == "modal_edit":
                    self.modal.handle(event)
                    tag = self.modal.clicked_btn(event)
                    if tag == "edit":
                        vals = self.modal.get_values()
                        u, pw = vals[0].strip(), vals[1]
                        if u in USERS:
                            USERS[u] = pw
                            self.notify(f"Contrasenya de '{u}' actualitzada.", "ok")
                            self.modal = None
                            self.state = "config"
                        else:
                            self.notify(f"Usuari '{u}' no existeix.", "error")
                    elif tag == "cancel":
                        self.modal = None
                        self.state = "config"

            #  UPDATE 
            self.tick += 1
            if self.state == "login":
                self.login_user.update()
                self.login_pass.update()
                self.login_btn.update(mx, my)
            elif self.state == "desktop":
                for btn in self.menu_btns:
                    btn.update(mx, my)
            elif self.state == "section":
                self.back_btn.update(mx, my)
                for btn in self.item_btns:
                    btn.update(mx, my)
                if self.action_btn:
                    self.action_btn.update(mx, my)
            elif self.state == "config":
                self.back_btn.update(mx, my)
                for btn in self.cfg_btns:
                    btn.update(mx, my)
            elif self.state == "mrua":
                self.back_btn.update(mx, my)
                self.calc_btn.update(mx, my)
                if self.mrua_step == "choose":
                    for btn in self.mrua_choice_btns:
                        btn.update(mx, my)
                elif self.mrua_step == "input":
                    for (_, _, inp) in self.mrua_inputs:
                        inp.update()
            if self.modal:
                self.modal.update(mx, my)

            #  DRAW 
            if self.state == "login":
                self._draw_login()
            elif self.state == "desktop":
                self._draw_desktop()
            elif self.state == "section":
                self._draw_section()
            elif self.state == "config":
                self._draw_config()
            elif self.state == "mrua":
                self._draw_mrua()
            elif self.state in ("modal_admin","modal_add","modal_remove","modal_edit"):
                # Draw background state first
                if self.section in ("música","vídeo","imatges",
                                    "documents","descàrregues"):
                    self._draw_section()
                elif self.section == "configuració":
                    self._draw_config()
                else:
                    self._draw_desktop()
                self.modal.draw(self.screen)

            self._draw_notifications()
            pygame.display.flip()
            self.clock.tick(FPS)


if __name__ == "__main__":
    app = MiniOS()
    app.run()