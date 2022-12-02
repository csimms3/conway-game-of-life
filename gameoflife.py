import copy
import random

x = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0]]



class Life:

    def generate_arr(self):
        arr = []
        for i in range(self.y):
            arr.append([])
            for j in range(self.x):
                arr[i].append(0 if random.random() > self.weight else 1)
        return arr

    def __init__(self, x, y, weight=0.5):
        self.x = x
        self.y = y
        self.weight = weight
        self.arr = self.generate_arr()


        self.generation = 0

    def get_cell_value(self, cell_x, cell_y):
        if cell_x in range(0, self.x) and cell_y in range(0, self.y):
            return self.arr[cell_y][cell_x]
        else:
            return 0

    def count_neighbors(self, cell_x, cell_y):
        min_x, max_x = max(0, cell_x - 1), min(self.x - 1, cell_x + 1)
        min_y, max_y = max(0, cell_y - 1), min(self.y - 1, cell_y + 1)


        neighbors_alive = 0
        for i in range(min_y, max_y+1):
            for j in range(min_x, max_x+1):
                if (i, j) == (cell_y, cell_x):
                    pass
                elif self.get_cell_value(j, i) == 1:
                    neighbors_alive += 1
        return neighbors_alive

    def update_cell(self, cell_x, cell_y, num_neighbors):
        cell_status = self.get_cell_value(cell_x, cell_y)

        if cell_status == 1:
            if 2 <= num_neighbors <= 3:
                updated_state = 1
            else:
                updated_state = 0
        else:
            if num_neighbors == 3:
                updated_state = 1
            else:
                updated_state = 0
        return updated_state

    def modify_cell(self, cell_x, cell_y):
        self.arr[cell_y][cell_x] = 1 if self.get_cell_value(cell_x,cell_y) == 0 else 0

    def update_arr(self):
        new_frame = copy.deepcopy(self.arr)
        self.generation += 1
        for cell_y in range(self.y):
            for cell_x in range(self.x):
                new_frame[cell_y][cell_x] = self.update_cell(cell_x, cell_y, self.count_neighbors(cell_x, cell_y))
        self.arr = new_frame

    def print_cell_neighbors(self, cell_x, cell_y):
        print(f"{cell_x, cell_y}\n"
              f"val: {self.get_cell_value(cell_x, cell_y)}\n"
              f"neighbors: {self.count_neighbors(cell_x, cell_y)}")

    def print_arr(self):
        print(f"Generation: {self.generation}")
        print("--------------")
        for pos, item in enumerate(self.arr):
            for j in item:
                print(j, end=" ")
            print(end="\n")
        print("--------------")


def main():
    life = Life(20,10)

    print("commands:\n"
          "c = change cell\n"
          "n = next frame\n"
          "s = print list-format of current state\n"
          "e = end process")

    life.print_arr()

    while True:
        todo = input("> ")
        match todo:
            case "c":
                x = int(input("x-val:"))
                y = int(input("y-val:"))
                life.modify_cell(x,y)
            case "n":
                life.update_arr()
            case "s":
                print(life.arr)
            case "e":
                break

        print("-------------------")
        life.print_arr()


if __name__ == "__main__":
    main()


