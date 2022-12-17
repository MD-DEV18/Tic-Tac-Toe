import os

field = "1|2|3\n4|5|6\n7|8|9"

player_one_playing = True
player_two_playing = False
valid = False

win = False

def check_position(n):
  global valid

  if str(n) in field:
    valid = True
    
def check_win():
  global field, win
  field_list = [i.split("|") for i in field.split("\n")]

  for y in field_list:
    if y[0] == y[1] and y[1] == y[2]: 
      win = True
      return

  for x in range(len(field_list)):
    if field_list[0][x] == field_list[1][x] and field_list[1][x] == field_list[2][x]:
      win = True
      return

  if field_list[0][0] == field_list[1][1] and field_list[1][1] == field_list[2][2]:
    win = True
    return

  if field_list[0][2] == field_list[1][1] and field_list[1][1] == field_list[2][0]:
    win = True
    return

def reset():
  global field, player_one_playing, player_two_playing, valid, win
  field = "1|2|3\n4|5|6\n7|8|9"
  player_one_playing = True
  player_two_playing = False
  valid = False
  win = False

os.system("cls")
while True:
  if win == True:
    print(field)
    if player_two_playing:
      print("player 1 ha vinto!")
    else:
      print("player 2 ha vinto!")
    
    input("\npremi un tasto per continuare...")

    os.system("cls")
    reset()

  if player_one_playing:
    while valid != True:
      print(field)
      n = input("player 1 > ")
      check_position(n)

      os.system("cls")

    field = field.replace(str(n), "X")

    valid = False
    player_one_playing = False
    player_two_playing = True

  elif player_two_playing: 
    while valid != True:
      print(field)
      n = input("player 2 > ")
      check_position(n)

      os.system("cls")

    field = field.replace(str(n), "O")

    valid = False
    player_one_playing = True
    player_two_playing = False
  
  check_win()