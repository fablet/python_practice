import random

#allow user to select difficulty level to set grid size
#sizes will be 5x5 EASY, 10x10 MED, 15x15 HARD (or as gets adjusted by variable)
def set_difficulty():
  easy = 5
  med = 10
  hard = 15
  grid = []
  level = ''
  while True:
    print("How difficult would you like this to be?")
    difficulty = input("Type EASY, MED, HARD >> ").upper()
    if difficulty == "EASY":
      grid = build_grid(easy)
      edge = easy
      break
    elif difficulty == "MED":
      grid = build_grid(med)
      edge = med
      break
    elif difficulty == "HARD":
      grid = build_grid(hard)
      edge = hard
      level = 'hard'
      break
    else:
      print("That is not a valid selection. Try again")
      
  return grid, edge, level 



#create a tup list of grid points to create a range for random choice
def build_grid(size):
  x_axis = list(range(0,size))
  y_axis = list(range(0,size))
  grid_list = []
  
  for x_point in x_axis:
    for y_point in y_axis:
      grid_point = (x_point,y_point)
      grid_list.append(grid_point)
            
  return grid_list



def draw_map(edge, current_room, previous_moves, locations, level):
  row = edge - 1
  
  if current_room == locations['monster']:
    map_key = '@'
  elif current_room == locations['door']:
    map_key = '*'
  else:
    map_key = 'X'
    
  print('_.' * edge)
  while row >= 0:
    column = 0
    while column < edge:
      if (row, column) == current_room:
        if column == edge -1:
          print('|{}|'.format(map_key))
        else:
          print('|{}'.format(map_key), end='')
      elif (row, column) in previous_moves:
        if column == edge - 1:
          print('|/|')
        else:
          print('|/', end='')
      elif level == 'hard' and (row, column) == locations['monster']:
          if column == edge - 1:
            print('|@|')
          else:
            print('|@', end='')
      else:
        if column == edge -1:
          print('|_|')
        else:
          print('|_', end='')
      column += 1
    row -= 1 
    
  return  
  
      
  
  
#random selection of starting points for player, exit and monster
def get_locations(grid):
  locations_dict = {}
  while True:
    locations_dict['monster'] = random.choice(grid)
    locations_dict['door'] = random.choice(grid)
    locations_dict['start'] = random.choice(grid)
    if not (locations_dict['monster'] == locations_dict['door'] and locations_dict['monster'] == locations_dict['start'] and locations_dict['door'] == locations_dict['start']):
      break
  
  return locations_dict
      

  
#moving player through grid
def move_player(current_room, direction):
  x_axis, y_axis = current_room
  
  if direction == 'U':
    x_axis += 1
  elif direction == 'D':
    x_axis -= 1
  elif direction == 'R':
    y_axis += 1
  else:
    y_axis -= 1
    
  next_room = x_axis, y_axis
  
  return next_room
  


#test to see if current room results in no possible valid moves
def boxed_in(current_room, previous_moves, grid):
  stuck = False
  if move_player(current_room,'U') in previous_moves or not move_player(current_room,'U') in grid:
      if move_player(current_room,'D') in previous_moves or not move_player(current_room,'D') in grid:
          if move_player(current_room,'L') in previous_moves or not move_player(current_room,'L') in grid:
              if move_player(current_room,'R') in previous_moves or not move_player(current_room,'R') in grid:
                stuck = True
                
  return stuck


  
#basic instructions  
def show_help():
  print("\nTry to find the way out before the monster finds you.")
  print("You can move up(U), down(D), left(L), or right(R).")
  print("\nYou cannot move into any space you have already been in.")
  print("If you box yourself in or get eaten by the monster, you lose.")
  print("\nTo show these instructions again type HELP.  To end the game type QUIT.")

        


#main program:  

#introduction and initialization of parameters
game_grid, boundary, difficulty = set_difficulty()

starting_locations = get_locations(game_grid)
new_room = starting_locations['start']

players_moves = [] 
directions = ['U', 'D', 'L', 'R']

print("Welcome to the dungeon!")
print("\nYour dungeon will be {}x{} square".format(boundary,boundary))
print("You will be starting in room {}".format(starting_locations['start']))
draw_map(boundary, new_room, players_moves, starting_locations, difficulty)
show_help()
if difficulty == 'hard':
  print('Be warned the monster is wandering aimlessly throughout the rooms in the dungeon')
players_moves.append(starting_locations['start'])

player_choice = input(" >>").upper()

#game loop
while True:
  if player_choice == 'HELP':
    show_help()
    player_choice = input(" >>").upper()
  elif player_choice == 'QUIT':
    break
  elif player_choice not in directions:
    print('\n>>That is not a recognized selection.<<')
    show_help()
    player_choice = input("Try again. >>").upper()
  elif boxed_in(new_room, players_moves, game_grid):
    draw_map(boundary, new_room, players_moves, starting_locations, difficulty)
    print("You have boxed yourself in with no valid moves")
    print("Since you are trapped, the monster makes his way leisurely to your position")
    print("You die screaming while the monster eats you alive (>-<)")
    print("\nThanks for playing. Better luck in your next incarnation")
    break
  else:
    new_room = move_player(new_room, player_choice)
    draw_map(boundary, new_room, players_moves, starting_locations, difficulty)
    if new_room in players_moves:
      print("Sorry. You've already been to that room. Try again")
      new_room = players_moves[-1]
      player_choice = input(" >>").upper()
    elif not new_room in game_grid:
      print("Sorry. You have run into the dungeon wall. Try again")
      new_room = players_moves[-1]
      player_choice = input(" >>").upper()
    elif new_room == starting_locations['monster']:
      print("Oh bad luck. You wandered into a room and found the monster waiting")
      print("You die screaming while the monster eats you alive (>-<)")
      print("\nThanks for playing. Better luck in your next incarnation")
      break
    elif new_room == starting_locations['door']:
      print("Congratulations! You found the way out")
      print("The monster, still trapped in the dungeon, dies of starvation")
      print("\nThanks for playing. Maybe you'll give another monster a chance at a good meal")
      break
    else:
      print("You moved to room {}. The bad news is you still haven't found the way out.".format(new_room))
      print("The good news is you also haven't been eaten.")
      
      players_moves.append(new_room)
      player_choice = input("Where to next? >>").upper()
      while True:
        if difficulty == 'hard':
          starting_locations['monster'] = move_player(starting_locations['monster'],random.choice(directions))
          if starting_locations['monster'] in game_grid:
            break
        else:
          break