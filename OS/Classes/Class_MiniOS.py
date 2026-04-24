import pygame
import sys
import time
import os
from Classes.Class_UIElements import *
from constants import *

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

        # File viewing
        self.view_image = None
        self.view_text  = None
        self.view_title = None

        # MRUA state
        self.mrua_result = None
        self.mrua_step   = "choose"  # choose | input | result
        self.mrua_opt    = None
        self.mrua_fields = []
        self.mrua_vals   = {}
        self.mrua_inputs = []

        # Config state
        self.config_sub  = None

        # Permissions
        self.permissions = {
            "familia": ["música","vídeo","imatges","documents","descàrregues"],
            "convidats": ["descàrregues","música"]
        }

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

    def _logout(self):
        self.current_user = None
        self.state = "login"
        self._build_login()
        self.notify("Sessió tancada.", "info")

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
        folders = {
            "descàrregues": "Download",
            "música": "Music",
            "vídeo": "Video",
            "imatges": "Images",
            "documents": "Documents",
        }
        folder = folders.get(key)
        if folder:
            assets_path = os.path.join(os.path.dirname(__file__), "..", "Assets")
            path = os.path.join(assets_path, folder)
            if os.path.exists(path):
                return sorted([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
        return []

    def _can_access(self, key):
        if self.current_user == "admin":
            return True
        if key == "configuració":
            return False
        return key in self.permissions.get(self.current_user, [])

    def _open_action(self):
        if self.selected is None:
            self.notify("Selecciona un element primer.", "info")
            return
        if not self._can_access(self.section):
            self.notify("No tens permisos.", "error")
            return
        # Obrir o reproduir segons el tipus
        item = self.selected
        if self.section == "música":
            file_path = os.path.join(os.path.dirname(__file__), "..", "Assets", "Music", self.selected)
            if os.path.exists(file_path):
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play()
                self.notify(f"Reproduint: {item}", "ok")
            else:
                self.notify(f"Fitxer no trobat: {item}", "error")
        elif self.section == "imatges":
            file_path = os.path.join(os.path.dirname(__file__), "..", "Assets", "Images", self.selected)
            if os.path.exists(file_path):
                try:
                    self.view_image = pygame.image.load(file_path)
                    self.view_title = f"Imatge: {item}"
                    self.state = "view_image"
                except:
                    self.notify("No es pot carregar la imatge.", "error")
            else:
                self.notify(f"Fitxer no trobat: {item}", "error")
        elif self.section == "documents":
            file_path = os.path.join(os.path.dirname(__file__), "..", "Assets", "Documents", self.selected)
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        self.view_text = f.read()
                    self.view_title = f"Document: {item}"
                    self.state = "view_text"
                except:
                    self.notify("No es pot obrir el document.", "error")
            else:
                self.notify(f"Fitxer no trobat: {item}", "error")
        else:
            self.notify(f"Obert: {item}", "ok")

    #  CONFIG
    def _build_config(self):
        self.section  = "configuració"
        self.state    = "config"
        self.cfg_btns = []
        opts = [("Afegir usuari","add"), ("Treure usuari","remove"),
                ("Editar usuari","edit"), ("Editar permisos","perms")]
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

    def _open_perms_modal(self):
        buttons = []
        sections = ["música","vídeo","imatges","documents","descàrregues"]
        for user in ["familia","convidats"]:
            for sec in sections:
                status = "Sí" if sec in self.permissions[user] else "No"
                label = f"{user} {sec}: {status}"
                tag = f"toggle_{user}_{sec}"
                buttons.append((label, tag, ACCENT2))
        buttons.append(("Tancar", "close", RED))
        self.modal = Modal(
            "Editar permisos",
            [],
            buttons,
            self.f_sub, self.f_body,
            width=500  # wider modal
        )
        self.state = "modal_perms"

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

    def _draw_view_image(self):
        self.screen.fill(BG)
        if self.view_image:
            # Scale to fit
            iw, ih = self.view_image.get_size()
            scale = min(W / iw, (H - 100) / ih)
            if scale < 1:
                nw, nh = int(iw * scale), int(ih * scale)
                img = pygame.transform.scale(self.view_image, (nw, nh))
            else:
                img = self.view_image
            rect = img.get_rect(center=(W//2, H//2))
            self.screen.blit(img, rect)
        draw_text(self.screen, self.view_title, self.f_title, ACCENT, W//2, 20, anchor="midtop")
        back_btn = Button((20, H-60, 100, 40), "Tornar", font=self.f_body, tag="back")
        back_btn.draw(self.screen)
        self.view_back_btn = back_btn

    def _draw_view_text(self):
        self.screen.fill(BG)
        draw_text(self.screen, self.view_title, self.f_title, ACCENT, 20, 20)
        # Draw text lines
        lines = self.view_text.split('\n')
        y = 60
        for line in lines[:30]:  # Limit lines
            draw_text(self.screen, line, self.f_body, TEXT, 20, y)
            y += 20
        back_btn = Button((20, H-60, 100, 40), "Tornar", font=self.f_body, tag="back")
        back_btn.draw(self.screen)
        self.view_back_btn = back_btn

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
                            if tag == "logout":
                                self._logout()
                            elif tag == "exit":
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

                #  VIEW IMAGE/TEXT
                elif self.state in ("view_image", "view_text"):
                    if hasattr(self, 'view_back_btn') and self.view_back_btn.clicked(event):
                        self.state = "section"
                        self.view_image = None
                        self.view_text = None
                        self.view_title = None

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
                            elif btn.tag == "perms":
                                self._open_perms_modal()

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

                #  MODAL PERMS
                elif self.state == "modal_perms":
                    self.modal.handle(event)
                    tag = self.modal.clicked_btn(event)
                    if tag == "close":
                        self.modal = None
                        self.state = "config"
                    elif tag.startswith("toggle_"):
                        _, user, sec = tag.split("_", 2)
                        if sec in self.permissions[user]:
                            self.permissions[user].remove(sec)
                        else:
                            self.permissions[user].append(sec)
                        # Reopen modal to update labels
                        self._open_perms_modal()

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
            elif self.state == "view_image" or self.state == "view_text":
                self.view_back_btn.update(mx, my)
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
            elif self.state == "view_image":
                self._draw_view_image()
            elif self.state == "view_text":
                self._draw_view_text()
            elif self.state == "config":
                self._draw_config()
            elif self.state == "mrua":
                self._draw_mrua()
            elif self.state in ("modal_add","modal_remove","modal_edit","modal_perms"):
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