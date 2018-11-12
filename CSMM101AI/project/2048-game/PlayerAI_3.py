from random import randint, shuffle

from BaseAI_3 import BaseAI
from Displayer_3 import Displayer
import time
from Grid_3 import directionVectors
import math

# computerAi para
tileVal = [2, 4]  # tile value
grid_size = 4

prob = 0.9
displayer = Displayer()  # debug


class PlayerAI(BaseAI):

    def getMove(self, grid):
        solver = AlphaBetaSolver(heuristics_fun)
        return solver.solve(grid)


class AlphaBetaSolver():

    def __init__(self, estimateFun, max_turn=16, maxTime=0.18):
        # self.upper_utility = upper_utility  # estimate max tile value
        # self.prev_time = time()
        # self.maxTime = search_time
        self.max_dep = max_turn
        self.estimateFun = estimateFun
        self.time = time.clock()
        self.maxTime = maxTime

    def solve(self, grid):
        m = self.maximize(grid, -math.inf, math.inf)[0]

        if m is None:
            return shuffle(grid.getAvailableMoves())[0]
        return m

    def terminal_test(self, actions, dep):
        return len(actions) == 0 or time.clock() - self.time > self.maxTime or dep > self.max_dep

    def minimize(self, grid, alpha, beta, dep=0):
        # self.dep +=1
        cells = grid.getAvailableCells()

        if self.terminal_test(cells, dep):
            return self.estimateFun(grid)

        utility = 0

        for cell in cells:
            child = grid.clone()  # grid is not change

            # for val in tileVal:
            child.setCellValue(cell, tileVal[0])
            u1 = self.maximize(child, alpha, beta, dep + 1)[1]

            child.setCellValue(cell, tileVal[1])
            u2 = self.maximize(child, alpha, beta, dep + 1)[1]

            utility += prob * u1 + (1 - prob) * u2

            # print("maximize utility = ", utility)
            # if utility < min_utility:
            #   min_utility = utility

            # if min_utility <= alpha:  # pruned
            #   return min_utility

            # if min_utility < beta:
            #   beta = min_utility

        return utility / len(cells)

    def maximize(self, grid, alpha, beta, dep=0):
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

            utility = self.minimize(child, alpha, beta, dep + 1)
            # print("minimize utility = ", utility)
            if utility > max_utility:
                max_utility = utility
                mov = m

            if max_utility >= beta:
                break

            if max_utility > alpha:
                alpha = max_utility

        return (mov, max_utility)


# some helper function

# some selected para

max_power = 20

weight = [128] + [2.5 ** i for i in range(max_power)]

weight_mat = [[32, 16, 8, 4],
              [16, 8, 4, 2],
              [8, 4, 2, 0],
              [4, 2, 0, 0],
              ]


# estimate function
def heuristics_fun(grid):
    return feature2(grid) - penalty(grid) + estimate_score(grid)


def estimate_score(grid, weight=weight, max_power=max_power):
    cnt = [0 for i in range(max_power + 1)]

    for i in range(grid_size):
        for j in range(grid_size):
            idx = int(math.log2(grid.getCellValue((i, j)) + 0.0000001) + 0.5)

            if idx < 0:
                idx = 0

            cnt[idx] += 1

    ret = 0
    for i in range(len(cnt)):
        ret += cnt[i] * weight[i]

    return ret


def feature2(grid):
    ret = 0
    for i in range(grid_size):
        for j in range(grid_size):
            ret += weight_mat[i][j] * grid.getCellValue((i, j))
    return ret


def penalty(grid):
    ret = 0
    for i in range(grid_size):
        for j in range(grid_size):

            cur_pos = (i, j)
            val = grid.getCellValue(cur_pos)
            if val == 0:
                continue
            for dir in directionVectors:
                pos = (cur_pos[0] + dir[0], cur_pos[1] + dir[1])

                if grid.crossBound(pos):
                    continue
                neibor_val = grid.getCellValue(pos)

                if neibor_val == val:
                    ret -= weight[int(math.log2(val)) + 1]
                ret += abs(val - neibor_val)

    return ret
