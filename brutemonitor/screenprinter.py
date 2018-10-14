
from color import colors

class ScreenPrinter:
    def __init__(self, path_to_background=None, term_dim_x=50, term_dim_y=20):
        print()
        self.term_dim_x = term_dim_x
        self.term_dim_y = term_dim_y

        self.sprites = []
        self.collision_matrix = []

        try:
            with open(path_to_background, 'r') as file:
                raw_data = file.read()
        except:
            raw_data = ''
            # raise FileNotFoundError("Invalid filepath!")

        lines = raw_data.split("\n")
        temp_buffer = {}

        for y in range(term_dim_y):
            for x in range(term_dim_x):
                # temp_buffer[x, y,] = lines[y][x]
                temp_buffer[x, y,] = f" " #if y != self.term_dim_y - 3 else "░"

        dim_x = len(lines[0])
        dim_y = len(lines) - 1

        self.__current_buffer = temp_buffer

    def blankScreen(self):
        for x in range(self.term_dim_x):
            for y in range(self.term_dim_y):
                self.changeCharacterAtPos(x, y, " ")

    def changeCharacterAtPos(self, pos_x, pos_y, char, safe=True):
        if len(char) != 1 and safe:
            raise Exception("Invalid char!")


        if not ( 0 <= pos_x < self.term_dim_x or 0 <= pos_y < self.term_dim_y):
            raise Exception("Invalid arguments!")

        self.getCurrentScreenBuffer()[pos_x, pos_y] = char

    def commit(self):
        print("\033[F" * (self.term_dim_y + 2), end="", flush=False)

        for y in range(self.term_dim_y):
            for x in range(self.term_dim_x):
                print(self.getNegative(self.__current_buffer[x, y,]), end="")



            print()

    def getCurrentScreenBuffer(self):
        return self.__current_buffer

    def drawSprite(self, pos_x, pos_y, spr):
        for y in range(spr.dim_y):
            for x in range(spr.dim_x):
                self.log(x, y)
                self.changeCharacterAtPos(pos_x + x, pos_y + y, spr.getCurrentScreenBuffer()[x, y,])

    def attachSprite(self, spr):
        self.sprites.append(spr)
        spr.setScreenPrinter(self)

    def updateSprites(self):
        # Cactus.update()
        for i in self.sprites:
            # if isinstance(i.object, Cactus):
            #     continue
            i.object.update()

    def putText(self, pos_x, pos_y, text, color=colors.white):
        for i in range(len(text)):
            # if False:
            #     pass
            if i == 0:
                self.changeCharacterAtPos(pos_x + i, pos_y, color + text[i], safe=False)
            elif i == len(text):
                self.changeCharacterAtPos(pos_x + i, pos_y, text[i] + colors.whiteblack, safe=False)
            else:
                self.changeCharacterAtPos(pos_x + i, pos_y, text[i], safe=True)

    def log(self, *args, sep=' '):
        args = list(map(str, args))
        string = sep.join(args)
        self.putText(0, self.term_dim_y - 1, self.term_dim_x * ' ')
        self.putText(0, self.term_dim_y - 1, string, color=colors.whiteblack)

    @staticmethod
    def getNegative(char):
        # k = 0
        #
        # chars = [' ', '░', '▒', '▓', '█']
        # for key, val in enumerate(chars):
        #     if val == char:
        #         k = key
        #         # print(k)
        #         break
        # else:
        #     return char
        #
        # return chars[-k]
        return char

    def detachSprite(self, spr):
        self.sprites.remove(spr)
