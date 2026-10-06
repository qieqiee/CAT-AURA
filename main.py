import pygame
import os
import random

# ==========================================
# INITIAL SETUP
# ==========================================

pygame.init()
pygame.mixer.init()

WIDTH = 900
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cat Aura")

clock = pygame.time.Clock()
FPS = 60


# ==========================================
# ASSET PATHS
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSET_DIR = os.path.join(BASE_DIR, "assets")

BACKGROUND_PATH = os.path.join(ASSET_DIR, "background.jpg")

SOUND_DIR = os.path.join(ASSET_DIR, "sound")
UI_DIR = os.path.join(ASSET_DIR, "ui")
FONT_DIR = os.path.join(ASSET_DIR, "font")
CAT_DIR = os.path.join(ASSET_DIR, "cat")
ITEM_DIR = os.path.join(ASSET_DIR, "items")
FISH_PATH = os.path.join(ITEM_DIR, "fish.png")
CAT_FOOD_PATH = os.path.join(ITEM_DIR, "cat_food.png")
WATER_PATH = os.path.join(ITEM_DIR, "water.png")
MOUSE_PATH = os.path.join(ITEM_DIR, "mouse.png")
STRAWBERRY_PATH = os.path.join(ITEM_DIR, "strawberry.png")
BANANA_PATH = os.path.join(ITEM_DIR, "banana.png")
BOMB_PATH = os.path.join(ITEM_DIR, "bomb.png")

HEART_PATH = os.path.join(UI_DIR, "heart.png")
MISSION_FAILED_PATH = os.path.join(UI_DIR, "mission_failed.png")
CAT_CLOSED_PATH = os.path.join(CAT_DIR, "cat_closed.png")
CAT_OPEN_PATH = os.path.join(CAT_DIR, "cat_open.png")

# Menu button images - English
PLAY_PATH = os.path.join(UI_DIR, "play.png")
EXIT_PATH = os.path.join(UI_DIR, "exit.png")

# Menu button images - Bahasa Melayu
MULA_PATH = os.path.join(UI_DIR, "mula.png")
KELUAR_PATH = os.path.join(UI_DIR, "keluar.png")

WASD_PATH = os.path.join(UI_DIR, "wasd.png")
ARROWS_PATH = os.path.join(UI_DIR, "arrows.png")

PIXEL_FONT = os.path.join(FONT_DIR, "pixel.ttf")

MISSION_PASSED_PATH = os.path.join(
    UI_DIR,
    "mission_passed.png"
)

# ==========================================
# LOAD BACKGROUND
# ==========================================

background = pygame.image.load(BACKGROUND_PATH).convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


# ==========================================
# LOAD SOUNDS
# ==========================================

click_sound = pygame.mixer.Sound(
    os.path.join(SOUND_DIR, "click.mp3")
)

pygame.mixer.music.load(
    os.path.join(SOUND_DIR, "bg_music.mp3")
)

pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

ngap_sound = pygame.mixer.Sound(
    os.path.join(SOUND_DIR, "ngap.mp3")
)

ngap_sound.set_volume(0.7)

bomb_sound = pygame.mixer.Sound(
    os.path.join(SOUND_DIR, "bomb.mp3")
)

gameover_sound = pygame.mixer.Sound(
    os.path.join(SOUND_DIR, "gameover.mp3")
)

bomb_sound.set_volume(0.7)
gameover_sound.set_volume(0.7)

levelup_sound = pygame.mixer.Sound(
    os.path.join(SOUND_DIR, "levelup.mp3")
)

success_sound = pygame.mixer.Sound(
    os.path.join(SOUND_DIR, "success.mp3")
)

levelup_sound.set_volume(0.7)
success_sound.set_volume(0.7)

# ==========================================
# PIXEL FONTS
# ==========================================

title_font = pygame.font.Font(PIXEL_FONT, 55)
button_font = pygame.font.Font(PIXEL_FONT, 17)
normal_font = pygame.font.Font(PIXEL_FONT, 13)
small_font = pygame.font.Font(PIXEL_FONT, 11)

# ==========================================
# LANGUAGE / TRANSLATION
# ==========================================

TEXT = {
    "EN": {
        "instructions": "INSTRUCTIONS",
        "language": "LANGUAGE: EN",

        "how_to_play": "HOW TO PLAY",
        "move_left": "LEFT / A - MOVE LEFT",
        "move_right": "RIGHT / D - MOVE RIGHT",
        "pause_game": "P - PAUSE GAME",
        "restart_game": "R - RESTART GAME",
        "catch_food": "CATCH FOOD TO EARN POINTS!",
        "avoid_bombs": "AVOID THE BOMBS!",
        "survive": "SURVIVE ALL 3 LEVELS TO WIN!",
        "return": "PRESS ESC TO RETURN",

        "level": "LEVEL",
        "score": "AURA SCORE",
        "time": "TIME",

        "paused": "PAUSED",
        "continue": "PRESS P TO CONTINUE",

        "complete": "COMPLETE",
        "next_level": "NEXT LEVEL",
        "restart": "RESTART",
        "exit": "EXIT",
        "final_score": "FINAL AURA SCORE"
    },

    "BM": {
        "instructions": "CARA BERMAIN",
        "language": "BAHASA: BM",

        "how_to_play": "CARA BERMAIN",
        "move_left": "KIRI / A - GERAK KE KIRI",
        "move_right": "KANAN / D - GERAK KE KANAN",
        "pause_game": "P - JEDA PERMAINAN",
        "restart_game": "R - MULA SEMULA",
        "catch_food": "TANGKAP MAKANAN UNTUK MATA!",
        "avoid_bombs": "ELAKKAN BOM!",
        "survive": "LEPASI 3 TAHAP UNTUK MENANG!",
        "return": "TEKAN ESC UNTUK KEMBALI",

        "level": "TAHAP",
        "score": "SKOR AURA",
        "time": "MASA",

        "paused": "DIJEDA",
        "continue": "TEKAN P UNTUK SAMBUNG",

        "complete": "SELESAI",
        "next_level": "TAHAP SETERUSNYA",
        "restart": "MULA SEMULA",
        "exit": "KELUAR",
        "final_score": "SKOR AURA AKHIR"
    }
}

# ==========================================
# IMAGE BUTTON CLASS
# ==========================================

class ImageButton:

    def __init__(self, image_path, x, y, width, height):

        self.original_image = pygame.image.load(
            image_path
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.original_image,
            (width, height)
        )

        self.rect = self.image.get_rect(
            center=(x, y)
        )

    def draw(self, surface):

        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):

            hover_image = pygame.transform.scale(
                self.original_image,
                (
                    int(self.rect.width * 1.08),
                    int(self.rect.height * 1.08)
                )
            )

            hover_rect = hover_image.get_rect(
                center=self.rect.center
            )

            surface.blit(hover_image, hover_rect)

        else:

            surface.blit(
                self.image,
                self.rect
            )

    def is_clicked(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            if (
                event.button == 1
                and self.rect.collidepoint(event.pos)
            ):

                click_sound.play()
                return True

        return False


# ==========================================
# PIXEL BUTTON CLASS
# ==========================================

class PixelButton:

    def __init__(self, text, x, y, width, height):

        self.text = text

        self.rect = pygame.Rect(
            0,
            0,
            width,
            height
        )

        self.rect.center = (x, y)

    def draw(self, surface):

        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            colour = (255, 205, 225)

        else:
            colour = (255, 145, 195)

        # Pixel shadow
        shadow = self.rect.copy()
        shadow.x += 6
        shadow.y += 6

        pygame.draw.rect(
            surface,
            (70, 35, 65),
            shadow
        )

        pygame.draw.rect(
            surface,
            colour,
            self.rect
        )

        # Pixel border
        pygame.draw.rect(
            surface,
            (45, 25, 45),
            self.rect,
            4
        )

        text_surface = button_font.render(
            self.text,
            True,
            (35, 20, 35)
        )

        text_rect = text_surface.get_rect(
            center=self.rect.center
        )

        surface.blit(
            text_surface,
            text_rect
        )

    def is_clicked(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            if (
                event.button == 1
                and self.rect.collidepoint(event.pos)
            ):

                click_sound.play()
                return True

        return False

# ==========================================
# PLAYER CLASS
# ==========================================

class Player:

    def __init__(self):

        # Load cat image
        self.image_closed = pygame.image.load(
            CAT_CLOSED_PATH
        ).convert_alpha()

        # Resize cat
        self.image_closed = pygame.transform.scale(
            self.image_closed,
            (120, 120)
        )

        self.image_open = pygame.image.load(
            CAT_OPEN_PATH
        ).convert_alpha()

        self.image_open = pygame.transform.scale(
            self.image_open,
            (120, 120)
        )

        self.image = self.image_closed

        self.mouth_open_until = 0


        self.rect = self.image.get_rect(
            midbottom=(WIDTH // 2, HEIGHT)
        )

        # Movement speed
        self.speed = 7

    def move(self):

        keys = pygame.key.get_pressed()

        # Move left
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed

        # Move right
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

        # Stop cat from leaving screen
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def open_mouth(self):

        self.image = self.image_open

        # Keep mouth open for 250 milliseconds
        self.mouth_open_until = pygame.time.get_ticks() + 250

    def update_animation(self):

        if pygame.time.get_ticks() >= self.mouth_open_until:
            self.image = self.image_closed

    def draw(self, surface):

        surface.blit(
            self.image,
            self.rect
        )

# ==========================================
# ITEM CLASS
# ==========================================

class Item:

    def __init__(self, name, image_path, points, is_bomb=False):

        self.name = name
        self.points = points
        self.is_bomb = is_bomb

        self.image = pygame.image.load(
            image_path
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (55, 55)
        )

        self.rect = self.image.get_rect()

        # Different starting positions
        self.rect.x = random.randint(
            20,
            WIDTH - self.rect.width - 20
        )

        self.rect.y = random.randint(-700, -50)



    def fall(self, speed):
        self.rect.y += speed

    def draw(self, surface):

        surface.blit(
            self.image,
            self.rect
        )

    def reset(self):

        self.rect.x = random.randint(
            20,
            WIDTH - self.rect.width - 20
        )

        self.rect.y = random.randint(-500, -80)


class GameManager:
    """Own the application states, game rules, level timer and main loop."""

    LEVEL_DURATION = 20
    LEVEL_SPEEDS = {1: 5, 2: 7, 3: 10}
    RESULT_STATES = ("LEVEL_COMPLETE", "GAME_COMPLETE", "GAME_OVER")

    def __init__(self):
        self.screen = screen
        self.clock = clock
        self.running = True
        self.game_state = "MENU"
        self.player = Player()
        self.items = self.create_items()
        self.heart_image = self.load_ui(HEART_PATH, (35, 35))
        self.mission_failed_image = self.load_ui(MISSION_FAILED_PATH, (400, 220))
        self.mission_passed_image = self.load_ui(MISSION_PASSED_PATH, (400, 220))
        self.wasd_image = self.load_ui(WASD_PATH, (120, 85))
        self.arrows_image = self.load_ui(ARROWS_PATH, (120, 85))
        # Default language
        self.language = "EN"

        # Main menu buttons
        self.play_button = ImageButton(
            PLAY_PATH,
            WIDTH // 2,
            315,
            170,
            55
        )

        self.instructions_button = PixelButton(
            TEXT[self.language]["instructions"],
            WIDTH // 2,
            385,
            245,
            55
        )

        self.language_button = PixelButton(
            TEXT[self.language]["language"],
            WIDTH // 2,
            455,
            245,
            55
        )

        self.menu_exit_button = ImageButton(
            EXIT_PATH,
            WIDTH // 2,
            525,
            170,
            55
        )
        self.next_button = PixelButton("NEXT LEVEL", WIDTH // 2 - 150, 480, 280, 60)
        self.restart_button = PixelButton("RESTART", WIDTH // 2 - 130, 480, 220, 60)
        self.result_exit_button = PixelButton("EXIT",WIDTH // 2 + 160,480,180,60)
        self.overlays = {}
        for opacity in (45, 135, 150, 155, 160):
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, opacity))
            self.overlays[opacity] = overlay

    @staticmethod
    def load_ui(path, size):
        return pygame.transform.scale(pygame.image.load(path).convert_alpha(), size)

    def toggle_language(self):
        """Switch the interface between English and Bahasa Melayu."""

        if self.language == "EN":
            self.language = "BM"

            # Change image buttons
            self.play_button = ImageButton(
                MULA_PATH,
                WIDTH // 2,
                315,
                170,
                55
            )

            self.menu_exit_button = ImageButton(
                KELUAR_PATH,
                WIDTH // 2,
                525,
                170,
                55
            )

        else:
            self.language = "EN"

            # Change image buttons
            self.play_button = ImageButton(
                PLAY_PATH,
                WIDTH // 2,
                315,
                170,
                55
            )

            self.menu_exit_button = ImageButton(
                EXIT_PATH,
                WIDTH // 2,
                525,
                170,
                55
            )

        # Update text buttons
        self.instructions_button.text = (
            TEXT[self.language]["instructions"]
        )

        self.language_button.text = (
            TEXT[self.language]["language"]
        )

        self.next_button.text = (
            TEXT[self.language]["next_level"]
        )

        self.restart_button.text = (
            TEXT[self.language]["restart"]
        )

        self.result_exit_button.text = (
            TEXT[self.language]["exit"]
        )

    @staticmethod
    def create_items():
        """Create the seven reusable item types with their original points."""
        return [
            Item("Fish", FISH_PATH, 10),
            Item("Cat Food", CAT_FOOD_PATH, 15),
            Item("Water", WATER_PATH, 5),
            Item("Mouse", MOUSE_PATH, 20),
            Item("Strawberry", STRAWBERRY_PATH, 10),
            Item("Banana", BANANA_PATH, 10),
            Item("Bomb", BOMB_PATH, 0, True),
        ]

    def reset_game(self):
        pygame.mixer.music.fadeout(500)
        self.level = 1
        self.aura_score = 0
        self.lives = 3
        self.player.rect.midbottom = (WIDTH // 2, HEIGHT)
        self.player.image = self.player.image_closed
        self.player.mouth_open_until = 0
        self.start_level()

    def start_level(self):
        """Start a new countdown while keeping score and hearts."""
        self.game_state = "PLAYING"
        self.paused = False
        self.level_start_time = pygame.time.get_ticks()
        self.pause_start = 0
        self.total_paused_time = 0
        self.time_left = self.LEVEL_DURATION
        self.spawn_item()

    def spawn_item(self):
        self.active_item = random.choice(self.items)
        self.active_item.reset()

    def return_to_menu(self):
        self.game_state = "MENU"
        pygame.mixer.music.play(-1)

    def next_level(self):
        if self.game_state == "LEVEL_COMPLETE" and self.level < 3:
            self.level += 1
            self.start_level()

    def toggle_pause(self):
        now = pygame.time.get_ticks()
        if self.paused:
            self.total_paused_time += now - self.pause_start
            self.paused = False
        else:
            self.update_timer(now)
            self.pause_start = now
            self.paused = True

    def update_timer(self, now=None):
        """Exclude paused milliseconds, including the current pause interval."""
        if now is None:
            now = pygame.time.get_ticks()
        end_time = self.pause_start if self.paused else now
        elapsed = (end_time - self.level_start_time - self.total_paused_time) // 1000
        self.time_left = max(0, self.LEVEL_DURATION - elapsed)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return
            if event.type == pygame.KEYDOWN:
                self.handle_key(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.handle_click(event)

    def handle_key(self, key):
        if key == pygame.K_ESCAPE:
            if self.game_state == "INSTRUCTIONS":
                click_sound.play()
                self.game_state = "MENU"
            elif self.game_state != "MENU":
                self.return_to_menu()
        elif self.game_state in ("PLAYING",) + self.RESULT_STATES:
            if key == pygame.K_r:
                self.reset_game()
            elif key == pygame.K_p and self.game_state == "PLAYING":
                self.toggle_pause()

    def handle_click(self, event):
        if self.game_state == "MENU":

            if self.play_button.is_clicked(event):
                self.reset_game()

            elif self.instructions_button.is_clicked(event):
                self.game_state = "INSTRUCTIONS"

            elif self.language_button.is_clicked(event):
                self.toggle_language()

            elif self.menu_exit_button.is_clicked(event):
                self.running = False

        elif self.game_state in self.RESULT_STATES:
            primary = self.next_button if self.game_state == "LEVEL_COMPLETE" else self.restart_button
            if primary.is_clicked(event):
                if self.game_state == "LEVEL_COMPLETE":
                    self.next_level()
                else:
                    self.reset_game()
            elif self.result_exit_button.is_clicked(event):
                self.return_to_menu()

    def resolve_item(self):
        """Caught bombs and missed food cost one heart, missed bombs are safe."""
        item = self.active_item
        if self.player.rect.colliderect(item.rect):
            if item.is_bomb:
                self.lives = max(0, self.lives - 1)
                bomb_sound.play()
            else:
                self.aura_score += item.points
                ngap_sound.play()
                self.player.open_mouth()
            self.spawn_item()
        elif item.rect.top > HEIGHT:
            if not item.is_bomb:
                self.lives = max(0, self.lives - 1)
            self.spawn_item()

    def check_progress(self):
        if self.lives == 0:
            self.game_state = "GAME_OVER"
            gameover_sound.play()
        elif self.time_left == 0:
            if self.level < 3:
                self.game_state = "LEVEL_COMPLETE"
                levelup_sound.play()
            else:
                self.game_state = "GAME_COMPLETE"
                success_sound.play()

    def update(self):
        if self.game_state != "PLAYING" or self.paused:
            return
        self.update_timer()
        self.player.move()
        self.player.update_animation()
        self.active_item.fall(self.LEVEL_SPEEDS[self.level])
        self.resolve_item()
        self.check_progress()

    def draw_text(self, text, font, colour, center):
        image = font.render(text, True, colour)
        self.screen.blit(image, image.get_rect(center=center))

    def draw_overlay(self, opacity):
        self.screen.blit(self.overlays[opacity], (0, 0))

    def draw_menu(self):
        self.draw_overlay(45)
        self.draw_text("CAT AURA", title_font, (40, 20, 40), (WIDTH // 2 + 5, 160))
        self.draw_text("CAT AURA", title_font, (255, 220, 80), (WIDTH // 2, 155))
        self.play_button.draw(self.screen)
        self.instructions_button.draw(self.screen)
        self.language_button.draw(self.screen)
        self.menu_exit_button.draw(self.screen)

    def draw_instructions(self):
        """Draw the instructions page using the selected language."""

        self.draw_overlay(155)

        text = TEXT[self.language]

        # Heading
        self.draw_text(
            text["how_to_play"],
            button_font,
            (255, 220, 80),
            (WIDTH // 2, 65)
        )

        # Control images
        wasd_rect = self.wasd_image.get_rect(
            center=(WIDTH // 2 - 90, 145)
        )

        arrows_rect = self.arrows_image.get_rect(
            center=(WIDTH // 2 + 90, 145)
        )

        self.screen.blit(self.wasd_image, wasd_rect)
        self.screen.blit(self.arrows_image, arrows_rect)

        # Instructions
        lines = [
            text["move_left"],
            text["move_right"],
            "",
            text["pause_game"],
            text["restart_game"],
            "",
            text["catch_food"],
            text["avoid_bombs"],
            text["survive"]
        ]

        y = 225

        for line in lines:
            if line:
                self.draw_text(
                    line,
                    normal_font,
                    (255, 255, 255),
                    (WIDTH // 2, y)
                )

            y += 32

        # Return instruction
        self.draw_text(
            text["return"],
            small_font,
            (255, 190, 220),
            (WIDTH // 2, 555)
        )

    def draw_hud(self):
        """Draw score, level, time and remaining lives."""

        text = TEXT[self.language]

        hud_items = (
            (f'{text["level"]} {self.level}', 20),
            (f'{text["score"]}: {self.aura_score}', 55),
            (f'{text["time"]}: {self.time_left}', 90)
        )

        for label, y in hud_items:
            self.screen.blit(
                small_font.render(
                    label,
                    True,
                    (255, 255, 255)
                ),
                (20, y)
            )

        # Draw remaining hearts
        for index in range(self.lives):
            self.screen.blit(
                self.heart_image,
                (WIDTH - 50 - index * 42, 20)
            )

    def draw_pause(self):
        """Draw the pause overlay in the selected language."""

        text = TEXT[self.language]

        self.draw_overlay(150)

        self.draw_text(
            text["paused"],
            button_font,
            (255, 220, 80),
            (WIDTH // 2, 270)
        )

        self.draw_text(
            text["continue"],
            small_font,
            (255, 255, 255),
            (WIDTH // 2, 330)
        )

    def draw_result(self):
        """Draw level complete, game complete and game over screens."""

        text = TEXT[self.language]

        failed = self.game_state == "GAME_OVER"
        intermediate = self.game_state == "LEVEL_COMPLETE"

        # Dark overlay
        self.draw_overlay(160 if failed else 135)

        # Level completion heading
        if not failed:
            self.draw_text(
                f'{text["level"]} {self.level} {text["complete"]}',
                button_font,
                (255, 255, 255),
                (WIDTH // 2, 80)
            )

        # Mission image
        if failed:
            image = self.mission_failed_image
        else:
            image = self.mission_passed_image

        self.screen.blit(
            image,
            image.get_rect(
                center=(WIDTH // 2, 245)
            )
        )

        # Score label
        if intermediate:
            score_label = text["score"]
        else:
            score_label = text["final_score"]

        self.draw_text(
            f"{score_label}: {self.aura_score}",
            small_font,
            (255, 255, 255),
            (WIDTH // 2, 390)
        )

        # Result buttons
        if intermediate:
            primary_button = self.next_button
        else:
            primary_button = self.restart_button

        primary_button.draw(self.screen)
        self.result_exit_button.draw(self.screen)

    def draw(self):
        self.screen.blit(background, (0, 0))
        if self.game_state == "MENU":
            self.draw_menu()
        elif self.game_state == "INSTRUCTIONS":
            self.draw_instructions()
        elif self.game_state == "PLAYING":
            self.active_item.draw(self.screen)
            self.player.draw(self.screen)
            self.draw_hud()
            if self.paused:
                self.draw_pause()
        elif self.game_state in self.RESULT_STATES:
            self.draw_result()

    def run(self):
        """Use one loop for every screen and every restart."""
        try:
            while self.running:
                self.handle_events()
                if not self.running:
                    break
                self.update()
                self.draw()
                pygame.display.update()
                self.clock.tick(FPS)
        finally:
            pygame.quit()


if __name__ == "__main__":
    GameManager().run()

