"""
COMP30024 Artificial Intelligence, Semester 1 2019
Solution to Project Part A: Searching

Authors: 
Luca Kennedy
Billy Price
"""


"""
And now, a message from our intelligent agent:
"""

"""
Hello {markerName}, my name is Kanye's fingers, and I'm here to use my fingers to take the pieces to where they want to be
"""
import sys
import json
from math import ceil
from hexboard import Tile, Colour, PieceState, HexBoard
from heapq import heappush, heappop
from node import Node
import parseBoard

class PriorityQueue():
    
    def __init__(self):
        self.queue = []
        self.find = dict()
    
    def push(self, node):
        heappush(self.queue, node)

    
    def pop(self):
        return heappop(self.queue)

    def __bool__(self):
        return bool(self.queue)


def main():
    board = HexBoard(start_config_file=parseBoard.testname)
    queue = PriorityQueue()
    bestnode = None
    board.seen_states.add(board.start_state.pieces)
    queue.push(Node(state=board.start_state, parent=None, prevmove="", cost=0, heu=board.start_state.get_heu(board)))
    while queue:
        nextnode = queue.pop()
        if bestnode and nextnode >= bestnode:     # pretty sure this is the break condition (even though the first one we find should be best)
            break 
        if nextnode.isgoal():
            bestnode = nextnode
            continue
        for node in nextnode.expand(board):
            if node.state.pieces not in board.seen_states:
                queue.push(node)
                board.seen_states.add(node.state.pieces)

    # bestnode.print_path()
    bestnode.print_path_boards(board)
               


# when this module is executed, run the `main` function:
if __name__ == '__main__':
    main()
