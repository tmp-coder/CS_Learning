# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 20:59:29 2018

@author: zouzhitao
"""

from collections import deque

from queue import PriorityQueue

import time

import resource

import sys

import math


#### SKELETON CODE ####

## The Class that Represents the Puzzle

class PuzzleState(object):
    """docstring for PuzzleState"""

    def __init__(self, config, n, parent=None, action="Initial", cost=0):

        if n * n != len(config) or n < 2:
            raise Exception("the length of config is not correct!")

        self.n = n

        self.cost = cost

        self.parent = parent

        self.action = action

        self.dimension = n

        self.config = config

        self.children = []

        h = 0
        for i in self.config:
            h = h * 10 + i
        self.hash = h

        for i, item in enumerate(self.config):

            if item == 0:
                self.blank_row = i // self.n

                self.blank_col = i % self.n

                break

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return isinstance(other, PuzzleState) and self.hash == other.hash

    def __lt__(self, other):

        return  calculate_total_cost(self) < calculate_total_cost(other)

    def display(self):

        for i in range(self.n):

            line = []

            offset = i * self.n

            for j in range(self.n):
                line.append(self.config[offset + j])

            print(line)

    def move_left(self):

        if self.blank_col == 0:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index - 1

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[
                blank_index]  # swap the number at target idx  and blank idx

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Left", cost=self.cost + 1)

    def move_right(self):

        if self.blank_col == self.n - 1:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index + 1

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Right", cost=self.cost + 1)

    def move_up(self):

        if self.blank_row == 0:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index - self.n

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Up", cost=self.cost + 1)

    def move_down(self):

        if self.blank_row == self.n - 1:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index + self.n

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Down", cost=self.cost + 1)

    def expand(self):

        """expand the node"""

        # add child nodes in order of UDLR

        if len(self.children) == 0:

            up_child = self.move_up()

            if up_child is not None:
                self.children.append(up_child)

            down_child = self.move_down()

            if down_child is not None:
                self.children.append(down_child)

            left_child = self.move_left()

            if left_child is not None:
                self.children.append(left_child)

            right_child = self.move_right()

            if right_child is not None:
                self.children.append(right_child)

        return self.children


# Function that Writes to output.txt

### Students need to change the method to have the corresponding parameters

## my helper function

def construct_result(goal_state, max_cost, explored, runtime):
    """construct result dict"""
    return {"path_to_goal": find_path_to_goal(goal_state),
            "cost_of_path": goal_state.cost,
            "nodes_expanded": len(explored),
            "search_depth": goal_state.cost,
            "max_search_depth": max_cost,
            "running_time": runtime,
            "max_ram_usage": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 / 1024}


def find_path_to_goal(goal_state):
    if goal_state == None:
        print("ERR,None Goal state")
        exit()
    goal_to_init = []
    root = goal_state
    while root.parent != None:
        goal_to_init.append(root.action)
        root = root.parent

    goal_to_init.reverse()
    return goal_to_init


def writeOutput(result, output_file="output.txt"):
    ### Student Code Goes here

    # write path to goal

    res_str = ["path_to_goal",
               "cost_of_path",
               "nodes_expanded",
               "search_depth",
               "max_search_depth",
               "running_time",
               "max_ram_usage"]
    f = open(output_file, "w")
    for e in res_str:
        f.write(e + ": " + str(result[e]) + "\n")

    f.close()


def bfs_search(initial_state):
    """BFS search"""
    ### STUDENT CODE GOES HERE ###
    nodes_exp = set()
    frontier = deque()
    frontier.append(initial_state)
    goal_state = None
    in_que = set()
    in_que.add(initial_state)
    max_dep = 0
    start_time = time.time()
    while len(frontier) != 0:
        now = frontier.popleft()
        
        if test_goal(now):
            goal_state = now
            break

        nodes_exp.add(now)
        
        now.expand()
        for e in now.children:
            if e not in in_que:
                if max_dep < e.cost:
                    max_dep = e.cost
                frontier.append(e)
                in_que.add(e)

    runtime = time.time() - start_time
    
    #goal_state.display()
    return construct_result(goal_state, max_dep, nodes_exp, runtime)


def dfs_search(initial_state):
    """DFS search"""
    nodes_exp = set()
    in_que = set()
    in_que.add(initial_state)
    frontier = []
    frontier.append(initial_state)
    goal_state = None
    start_time = time.time()
    max_dep = 0
    while len(frontier) > 0:
        now = frontier.pop();
        if test_goal(now):
            goal_state = now
            break

        nodes_exp.add(now)
        now.expand()
        now.children.reverse()  # dfs must reverse, danger bug
        for e in now.children:
            if e not in in_que:
                if max_dep < e.cost:
                    max_dep = e.cost
                
                in_que.add(e)
                frontier.append(e)
            # if e not in vis:
            #     frontier.append(e)

    runtime = time.time() - start_time

    return construct_result(goal_state, max_dep, nodes_exp, runtime)

    ### STUDENT CODE GOES HERE ###


def A_star_search(initial_state):
    """A * search"""
    nodes_expand = set()
    frontier = PriorityQueue()
    in_que = set()
    goal_state = None
    start_time = time.time()
    max_dep = 0

    in_que.add(initial_state)

    frontier.put(initial_state)

    while not frontier.empty():
        now = frontier.get()
        if test_goal(now):
            goal_state = now
            break

        nodes_expand.add(now)
        now.expand()

        for node in now.children:
            if node not in in_que:
                if max_dep < node.cost:
                    max_dep = node.cost
                in_que.add(node)
                frontier.put(node)

    runtime = time.time() - start_time

    return construct_result(goal_state,max_dep,nodes_expand,runtime)
    ### STUDENT CODE GOES HERE ###


def calculate_total_cost(state):
    """calculate the total estimated cost of a state"""
    return state.cost + calculate_estimate_cost(state)
    ### STUDENT CODE GOES HERE ###


def calculate_estimate_cost(state):
    """calculate the manhattan distance of a tile"""
    ret = 0
    n = state.n
    for i, val in enumerate(state.config):
        ret += calculate_mahatten_dist(i , val, n)
    return ret
    ### STUDENT CODE GOES HERE ###

def calculate_mahatten_dist(idx,val,n):

    if val ==0:
        return 0

    org_x = val // n
    org_y = val % n

    x = idx // n
    y = idx % n

    return  abs(x - org_x) + abs(org_y - y)


def test_goal(puzzle_state):
    """test the state is the goal state or not"""
    for i, item in enumerate(puzzle_state.config):
        if i != item:
            return False
    return True

    ### STUDENT CODE GOES HERE ###


# Main Function that reads in Input and Runs corresponding Algorithm

def main():
    sm = sys.argv[1].lower()

    begin_state = sys.argv[2].split(",")

    begin_state = tuple(map(int, begin_state))

    size = int(math.sqrt(len(begin_state)))

    hard_state = PuzzleState(begin_state, size)

    res = None

    if sm == "bfs":

        res = bfs_search(hard_state)

    elif sm == "dfs":

        res = dfs_search(hard_state)

    elif sm == "ast":

        res = A_star_search(hard_state)

    else:

        print("Enter valid command arguments !")

    writeOutput(res)


if __name__ == '__main__':
    main()
