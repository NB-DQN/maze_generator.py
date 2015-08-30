import generator

class Maze:
    def __init__(self, size):
        self.field = generator.Generator(size).generate()
        self.size = size

    def check_coordinate(self, coordinate):
        if not (0 <= coordinate[0] < self.size[0] and 0 <= coordinate[1] < self.size[1]):
            raise Exception("wrong coordinate")

    def wall(self, coordinate):
        self.check_coordinate(coordinate)
        return self.field[coordinate][0:4]

    def is_exit(self, coordinate):
        self.check_coordinate(coordinate)
        return self.field[coordinate][4]

    def display_cui(self):
        str = ""
        for y in range(self.size[1] - 1, -1, -1):
            for x in range(0, self.size[0]):
                str += "8"
                if self.field[(x, y, 2)] == 1:
                    str += "888"
                else:
                    str += "   "
            str += "8\n"

            for x in range(0, self.size[0]):
                if self.field[(x, y, 1)] == 1:
                    str += "8"
                else:
                    str += " "
                str += "   "
            if self.field[(self.size[0] - 1, y, 0)] == 1:
                str += "8\n"
            else:
                str += " \n"

        for x in range(0, self.size[0]):
            str += "8"
            if self.field[(x, 0, 3)] == 1:
                str += "888"
            else:
                str += "   "
        str += "8\n"

        print(str)

if __name__ == "__main__":
    Maze((9, 9)).display_cui()
