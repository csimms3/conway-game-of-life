import time

import graphics as g
from gameoflife import Life


def main():
    window_x, window_y = 900, 500
    win = g.GraphWin("Game of life", window_x, window_y, autoflush=False)

    def draw_tiles(num_x, num_y, array):
        # clear previous screen
        for i in (win.find_all()):
            win.delete(i)

        tile_width = (window_x - 100) / num_x
        tile_height = (window_y - 100) / num_y

        tile_size = min(tile_height, tile_width)

        for i in range(num_x):
            for j in range(num_y):

                pt1x = 50 + (i * tile_size)
                pt1y = 50 + (j * tile_size)
                pt2x = 50 + ((i + 1) * tile_size)
                pt2y = 50 + ((j + 1) * tile_size)

                tile = g.Rectangle(g.Point(pt1x, pt1y), g.Point(pt2x, pt2y))

                if array[j][i]:
                    tile.setFill("black")
                tile.draw(win)
        win.update()

    size = int(input("sim size:"))

    width, height = size * 2, size

    life = Life(width, height)

    print("commands:\n"
          "r = run sim\n"
          "c = change cell\n"
          "n = next frame\n"
          "s = print list-format of current state\n"
          "e = end process")

    while True:
        todo = input("> ")
        match todo:
            case "r":
                gens = int(input("num generations (at 20/s):"))
                for i in range(gens):
                    draw_tiles(width,height,life.arr)
                    life.update_arr()
                    time.sleep(0.1)

            case "c":
                x = int(input("x-val:"))
                y = int(input("y-val:"))
                life.modify_cell(x, y)

            case "n":
                life.update_arr()

            case "s":
                print(life.arr)

            case "e":
                break

        print("-------------------")
        life.print_arr()
        draw_tiles(width, height, life.arr)

    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
