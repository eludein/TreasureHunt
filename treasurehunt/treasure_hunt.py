import random

# Game settings
DUNGEON_SIZE = 5
TREASURE_ROOMS = 3
TRAP_ROOMS = 2
MAX_MOVES = 10

# Initialize dungeon
def create_dungeon(size, treasures, traps):
    dungeon = [["Empty" for _ in range(size)] for _ in range(size)]
    place_items(dungeon, "Treasure", treasures)
    place_items(dungeon, "Trap", traps)
    return dungeon

# Place items in the dungeon
def place_items(dungeon, item, count):
    for _ in range(count):
        x, y = random.randint(0, len(dungeon) - 1), random.randint(0, len(dungeon) - 1)
        while dungeon[x][y] != "Empty":
            x, y = random.randint(0, len(dungeon) - 1), random.randint(0, len(dungeon) - 1)
        dungeon[x][y] = item

# Player movement
def move_player():
    move = input("Move (N, S, E, W): ").upper()
    if move in ["N", "S", "E", "W"]:
        return move
    else:
        print("Invalid move. Try again.")
        return move_player()

# Check room content
def check_room(dungeon, x, y):
    if dungeon[x][y] == "Treasure":
        print("You found a treasure!")
    elif dungeon[x][y] == "Trap":
        print("Oh no, it's a trap!")
        return False
    else:
        print("This room is empty.")
    return True

# Main game function
def play_game():
    dungeon = create_dungeon(DUNGEON_SIZE, TREASURE_ROOMS, TRAP_ROOMS)
    player_x, player_y = 0, 0
    moves_left = MAX_MOVES

    while moves_left > 0:
        print(f"\nYou have {moves_left} moves left.")
        move = move_player()

        if move == "N" and player_x > 0:
            player_x -= 1
        elif move == "S" and player_x < DUNGEON_SIZE - 1:
            player_x += 1
        elif move == "E" and player_y < DUNGEON_SIZE - 1:
            player_y += 1
        elif move == "W" and player_y > 0:
            player_y -= 1

        if not check_room(dungeon, player_x, player_y):
            break

        moves_left -= 1

    if moves_left == 0:
        print("You've run out of moves!")
    print("Game over.")

if __name__ == "__main__":
    play_game()
