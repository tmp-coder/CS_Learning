from random import shuffle

from BaseAI_3 import BaseAI
from Displayer_3 import Displayer

import time
from Grid_3 import directionVectors
import math
# computerAi para
tileVal = [2, 4]  # tile value
grid_size = 4

prob = 0.9

# computerAi para
tileVal = [2, 4]  # tile value
grid_size = 4

prob = 0.9

class PlayerAI(BaseAI):

    def getMove(self, grid):
        solver = Solver(heuristics_fun)
        return solver.solve(grid)


class Solver():

    def __init__(self, estimateFun, max_turn=16, maxTime=0.18):
        self.max_dep = max_turn
        self.estimateFun = estimateFun
        self.time = time.clock()
        self.maxTime = maxTime

    def solve(self, grid):
        m = self.maximize(grid, self.max_dep)[0]

        if m is None:
            moves = grid.getAvailableMoves()
            shuffle(moves)
            return moves[0]
        return m

    def terminal_test(self, actions, dep):
        return dep == 0 or len(actions) == 0 or time.clock() - self.time > self.maxTime

    def minimize(self, grid, dep):
        # self.dep +=1
        cells = grid.getAvailableCells()

        if self.terminal_test(cells, dep):
            return self.estimateFun(grid)

        utility = 0

        for cell in cells:
            child = grid.clone()  # grid is not change

            # for val in tileVal:
            child.setCellValue(cell, tileVal[0])
            u1 = self.maximize(child, dep - 1)[1]

            child.setCellValue(cell, tileVal[1])
            u2 = self.maximize(child, dep - 1)[1]

            utility += prob * u1 + (1 - prob) * u2

        return utility / len(cells)

    def maximize(self, grid, dep):
        # self.dep +=1
        moves = grid.getAvailableMoves()

        if self.terminal_test(moves, dep):
            return (None, self.estimateFun(grid))

        max_utility = -1
        mov = None
        shuffle(moves)
        for m in moves:

            child = grid.clone()
            if not child.move(m):
                continue

            utility = self.minimize(child, dep - 1)
            # print("minimize utility = ", utility)
            if utility > max_utility:
                max_utility = utility
                mov = m

        return (mov, max_utility)


# some helper function

# some selected para

max_power = 20

weight = [2.5 ** 5] + [2.5 ** i for i in range(max_power)]
# weight matrix of position
weight_mat = [[13, 9, 6, 4],
              [9, 6, 4, 2],
              [6, 4, 2, 1],
              [4, 2, 1, 0],
              ]

# estimate function
def heuristics_fun(grid):
    return feature2(grid) - penalty(grid) + estimate_score(grid)


def estimate_score(grid, weight=weight):
    weight[1] = weight[2] = 0
    ret = 0
    max_v = 0
    for i in range(grid_size):
        for j in range(grid_size):
            idx = int(math.log2(grid.getCellValue((i, j)) + 0.0000001) + 0.5)
            if idx < 0:
                idx = 0
            if idx > max_v:
                max_v = idx
            ret += weight[idx]

    if idx >= 10:
        ret += (1 << idx)*idx/6
        ret =ret * idx /5
    return ret


def feature2(grid):
    ret = 0
    for i in range(grid_size):
        for j in range(grid_size):
            val = grid.getCellValue((i, j))
            if val > 4:
                ret += weight_mat[i][j] * val
    return ret


def penalty(grid):
    ret = 0
    for i in range(grid_size):
        for j in range(grid_size):

            cur_pos = (i, j)
            val = grid.getCellValue(cur_pos)
            for dir in directionVectors:
                pos = (cur_pos[0] + dir[0], cur_pos[1] + dir[1])

                if grid.crossBound(pos):
                    continue
                neibor_val = grid.getCellValue(pos)

                if neibor_val == val:
                    ret -= val
                ret += abs(val - neibor_val)

    return ret
