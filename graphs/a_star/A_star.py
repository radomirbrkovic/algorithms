# Source found at https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
from Node import Node
from warnings import warn
import heapq

def getPath(currentNode):
    path = []
    current = currentNode

    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]    

def aStar(maze, start, end, allowDiagonalMovement = False):
    """
    Return a list of tuples as a path from the given start to the given end in the given maze 
    :param maze:
    :param star:
    :param end:
    :return:
    """    

    startNode = Node(None, start)
    startNode.G = startNode.H = startNode.F = 0

    endNode = Node(None, end)
    endNode.G = endNode.H = endNode.F = 0

    openList = []
    closedList = []

    heapq.heapify(openList)
    heapq.heappush(openList, startNode)

    outerInerations = 0
    maxInterations =  (len(maze[0]) * len(maze) // 2)

    adjacentSquares = ((0, -1), (0, 1), (-1, 0), (1, 0),)
    if allowDiagonalMovement:
        adjacentSquares = ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1),)


    while len(openList) > 0:
        outerInerations += 1

        if outerInerations > maxInterations:
            # if we hit this point return the path such as it is
            # it will not contain the destination
            warn("giving up on pathfinding too many iterations")
            return getPath(currentNode)   


        currentNode = heapq.heappop(openList)
        closedList.append(currentNode)


        # Found the goal
        if currentNode == endNode:
            return getPath(currentNode)

        # Generate children
        children = []


        for newPosition in adjacentSquares: # Adjacent squares

            # Get node position
            nodePosition = (currentNode.position[0] + newPosition[0], currentNode.position[1] + newPosition[1])

            # Make sure within range
            if nodePosition[0] > (len(maze) - 1) or nodePosition[0] < 0 or nodePosition[1] > (len(maze[len(maze)-1]) -1) or nodePosition[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[nodePosition[0]][nodePosition[1]] != 0:
                continue

            # Create new node
            newNode = Node(currentNode, nodePosition)

            # Append
            children.append(newNode)

        # Loop through children
        for child in children:
            # Child is on the closed list
            if len([closedChild for closedChild in closedList if closedChild == child]) > 0:
                continue

            # Create the f, g, and h values
            child.G = currentNode.G + 1
            child.H = ((child.position[0] - endNode.position[0]) ** 2) + ((child.position[1] - endNode.position[1]) ** 2)
            child.F = child.G + child.H

            # Child is already in the open list
            if len([openNode for openNode in openList if child.position == openNode.position and child.G > openNode.G]) > 0:
                continue

            # Add the child to the open list
            heapq.heappush(openList, child)
    
    warn("Couldn't get a path to destination")
    return None


def example(print_maze = True):

    maze = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,] * 2,
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,] * 2,
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,] * 2,
            [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,] * 2,
            [0,0,0,1,1,0,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,] * 2,
            [0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,] * 2,
            [0,0,0,1,0,1,1,1,1,0,1,1,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,] * 2,
            [0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0,0,0,1,1,1,0,] * 2,
            [0,0,0,1,0,1,1,0,1,1,0,1,1,1,0,0,0,0,0,1,0,0,1,1,1,1,1,0,0,0,] * 2,
            [0,0,0,1,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,0,1,0,1,1,] * 2,
            [0,0,0,1,0,1,0,1,1,0,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1,0,1,0,0,0,] * 2,
            [0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,1,0,] * 2,
            [0,0,0,1,0,1,1,1,1,0,1,0,0,1,1,1,0,1,1,1,1,0,1,1,1,0,1,0,0,0,] * 2,
            [0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1,] * 2,
            [0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,] * 2,
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,] * 2,]
    
    start = (0, 0)
    end = (len(maze)-1, len(maze[0])-1)

    path = aStar(maze, start, end)

    if print_maze and path != None:
      for step in path:
        maze[step[0]][step[1]] = 2
      
      for row in maze:
        line = []
        for col in row:
          if col == 1:
            line.append("\u2588")
          elif col == 0:
            line.append(" ")
          elif col == 2:
            line.append(".")
        print("".join(line))

    print(path)



example()
