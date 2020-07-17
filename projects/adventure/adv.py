from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


verbose = False
# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
if verbose:
    world.print_rooms()

player = Player(world.starting_room)

traversal_path = []
reverse_path = []
visited = {}
movement = {"n": "s", "e": "w", "s": "n", "w": "e"}

# add first room
exits = player.current_room.get_exits()
current = player.current_room.id
visited[current] = {k: v for (k, v) in zip(exits, [None] * len(exits))}

# helper function to determine which direction to go next
def descend(exits):
    options = {k for k, v in exits.items() if v == None}
    return [i for i in ["n", "e", "s", "w"] if i in options]


while len(visited) < len(room_graph):
    exits = player.current_room.get_exits()
    current = player.current_room.id
    options = descend(visited[current])
    # options = [
    #     i
    #     for i in ["n", "e", "s", "w"]
    #     if i in [k for k, v in visited[current].items() if v == None]
    # ]
    if len(options) > 0:
        moved_from = current
        player.travel(options[0])
        traversal_path.append(options[0])
        reverse_path.append(movement[options[0]])
        current = player.current_room.id
        # if new room is not in visited, add it
        if current not in visited:
            loose_ends = player.current_room.get_exits()
            visited[current] = {
                k: v for (k, v) in zip(loose_ends, [None] * len(loose_ends))
            }
        # in either case, map where we just came from
        visited[moved_from][options[0]] = current
        visited[current][movement[options[0]]] = moved_from
        if verbose:
            print(f"Moved {options[0]} ({moved_from} -> {current})")
    else:
        # backtrack until we find a route with an unexplored area
        explored = True
        while explored:
            moved_from = current
            backtrack = reverse_path.pop()
            player.travel(backtrack)
            traversal_path.append(backtrack)
            current = player.current_room.id
            if verbose:
                print(f"Moved {backtrack} ({moved_from} -> {current})")
            if len(descend(visited[current])) > 0:
                explored = False


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited"
    )
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

# UNCOMMENT TO WALK AROUND
"""
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
"""
