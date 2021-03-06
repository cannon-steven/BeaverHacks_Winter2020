import pygame as pg
import math
from settings import *
from sprites import *
from rooms import *
from stew_work import *
from tilemap import *
from tile_map_generator import *
from title_screen import *

class Game:
    def __init__(self):
        # initialize game window, etc
        self.running = True
        create_dungeon(19, 14)
        self.load_map()
        # self.dungeon = Dungeon(14)
        pg.init()
        pg.mixer.init()  # in case we want to add sound later
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.icon = pg.image.load("Images/icon-sword.png")
        pg.display.set_icon(self.icon)
        self.clock = pg.time.Clock()  # used to set FPS later

        pygame.mixer.music.load('Sounds/backgroundmusic.wav')
        pygame.mixer.music.play(-1)

    def load_map(self):
        self.map = Map('dungeon.txt')

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.room1 = Room(self, 'Images/BasicRoom.png', 1, 1, 1, 1)
        self.room1.room_creation()
        self.player = Player(self, 8, 14, 'Images/actor.png')
        # self.minimap = Minimap(self, 19, 0, self.dungeon)
        self.camera = Camera(self.map.width, self.map.height)
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            # dt = how much time the previous frame took, given in milliseconds
            self.dt = self.clock.tick(FPS) / 1000  # dividing by 1000 to convert to seconds
            # the three main components of the cycle
            self.events()
            self.update()
            self.draw()

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window. Exits both the game event and the window.
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self):
        # Game Loop - update
        self.all_sprites.update()  # passing dt to make movement speed not tied to frame rate, but time
        self.camera.update(self.player)

    def draw(self):
        # Game Loop - draw
        # self.screen.blit(self.background, (0, 0))
        if self.player.rect.x:
            pass
        self.room1.get_background()
        self.draw_grid()
        # self.all_sprites.draw(self.screen)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        # always do last after drawing everything
        pg.display.flip()  # very important to make less intensive / slow

    def draw_grid(self):
        pass
        """Temporary method used for drawing gridlines."""
        # for x in range(0, WIDTH, TILESIZE):
        #     pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        # for y in range(0, HEIGHT, TILESIZE):
        #     pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass

# create the game object
g = Game()
g.show_start_screen()

#Game Loop

while g.running:
    title_screen()
    g.new()
    g.show_go_screen()