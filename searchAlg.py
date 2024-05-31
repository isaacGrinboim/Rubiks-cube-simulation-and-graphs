import cube as RubiksCube
import math
import numpy as np
from typing import List, Tuple
import heapdict
import sys


class Node:
    def __init__(self, cube :RubiksCube.Cube, father=None, action=None, cost = 0, heuristics = 0, g=0):
        self.cube = cube
        self.father = father
        self.action_to_here = action
        self.cost = cost
        self.h = heuristics
        self.g = g


class BFS:

    def __init__(self) -> None:
        self.num_expanded = 0

    def calculate_res(self, node):
        actions = []
        actions = [node.action_to_here] + actions
        node = node.father

        while node.father is not None:
            actions = [node.action_to_here] + actions
            node = node.father

        return actions, self.num_expanded

    def search(self, my_cube: RubiksCube.Cube) -> Tuple[List[int], int]:

        if my_cube.solved():
            return [], 0

        open_list = []
        s_node = Node(my_cube.clone(), None, None)
        open_list = open_list + [s_node]
        close = set()

        while open_list is not []:
            # pop
            curr_node = open_list[0]
            del open_list[0]
            
            close.add(curr_node.cube)

            self.num_expanded += 1

            for move in my_cube.get_legal_moves():
                cloned_cube = curr_node.cube.clone()
                cloned_cube.make_move[move]()
                child_node = Node(cloned_cube, curr_node ,move)

                if child_node.cube not in close and child_node.cube not in [node.cube for node in open_list]:
                    if child_node.cube.solved():
                        return self.calculate_res(child_node)

                    open_list = open_list + [child_node]





class Greedy:
    def __init__(self) -> None:
        self.open = heapdict.heapdict()
        self.close = set()
        self.num_expanded = 0

        
    def calculate_res(self, node):
        actions = []
        total_cost = node.cost
        actions = [node.action_to_here] + actions
        node = node.father

        while node.father is not None:
            total_cost = total_cost + node.cost
            actions = [node.action_to_here] + actions
            node = node.father

        return actions, total_cost, self.num_expanded

    def search(self,  my_cube: RubiksCube.Cube) -> Tuple[List[int], int, float]:
    
        self.open = heapdict.heapdict()
        self.close = set()
        self.num_expanded = 0

        if  my_cube.solved():
            return [], 0, 0
        cloned_cube = my_cube.clone()
        s_node = Node(cloned_cube, None, None, 0, cloned_cube.h_val() , 0)
        
        # initial h value is h_sap
        self.open[s_node] = s_node.h

        while self.open:  # while its not empty
            # pops the one with lowest h
            curr_node, curr_h = self.open.popitem()
            self.close.add(curr_node.cube)

            if curr_node.cube.solved():
                return self.calculate_res(curr_node)
            
            if curr_node.g > my_cube.MAX_LEN:
                continue

            self.num_expanded += 1

            for move in my_cube.get_legal_moves():

                cloned_cube = curr_node.cube.clone()
                cloned_cube.make_move[move]()
                child_node = Node(cloned_cube, curr_node ,move, 1, cloned_cube.h_val(), curr_node.g + 1)
###########################
                if child_node.cube not in self.close and child_node.cube not in [node.cube for node in self.open]:
                    self.open[child_node] = child_node.h

        return [], -1, -1




cube = RubiksCube.Cube()
scrumble = ["R","L"]
cube.scrumble(scrumble)
cube.print_side(RubiksCube.GREEN_SIDE)
print("scrumble was: ", scrumble)

print("BFS search:")
search_agent = BFS()
solution , num_expanded = search_agent.search(cube)
print("solution and num of nodes expanded: ", solution, num_expanded)
print("-solved cube-")
cube.scrumble(solution)
cube.print_side(RubiksCube.GREEN_SIDE)


print("Greedy search:")
cube_2 = RubiksCube.Cube()
scrumble = ["R","L", "U", "D","R"]
cube_2.scrumble(scrumble)
cube_2.print_side(RubiksCube.GREEN_SIDE)
print("scrumble was: ", scrumble)

search_agent = Greedy()
solution , total_cost, num_expanded = search_agent.search(cube_2)
print("solution, len and num of nodes expanded: ", solution, total_cost, num_expanded)
print("-solved cube-")
cube_2.scrumble(solution)
cube_2.print_side(RubiksCube.GREEN_SIDE)


