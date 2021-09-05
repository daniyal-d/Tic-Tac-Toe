inp = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

grid = f"|{inp[0]}|{inp[1]}|{inp[2]}|\n|{inp[3]}|{inp[4]}|{inp[5]}|\n|{inp[6]}|{inp[7]}|{inp[8]}|"
print(grid)

coordinates_and_squares = {"1 1": 6, "1 2": 3, "1 3": 0, "2 1": 7, "2 2": 4, "2 3": 1, "3 1": 8, "3 2": 5, "3 3":2}

def x_turn():
  grid_add = input("Input the coordiantes where you would like to place an X: ")
  x_input(grid_add)

def x_input(x):
  if x not in ["1 1", "1 2", "1 3", "2 1", "2 2", "2 3", "3 1", "3 2", "3 3"]:
    print("Please input a proper coordinate")
    x_turn()

  else:
    answer = coordinates_and_squares[x]

    if inp[answer] not in ["X", "O"]:
      inp[answer] = "X"
      grid = f"|{inp[0]}|{inp[1]}|{inp[2]}|\n|{inp[3]}|{inp[4]}|{inp[5]}|\n|{inp[6]}|{inp[7]}|{inp[8]}|"
      print(grid)

      if x_win():
        print("X Wins")
      elif draw():
        print("Draw")
      else:
        o_turn()
    
    else:
      print("Square is occupied, please try again")
      x_turn()


def o_turn():
  grid_add = input("Input the coordiantes where you would like to place an O: ")
  o_input(grid_add)

def o_input(x):
  if x not in ["1 1", "1 2", "1 3", "2 1", "2 2", "2 3", "3 1", "3 2", "3 3"]:
    print("Please input a proper coordinate")
    o_turn()

  else:
    answer = coordinates_and_squares[x]

    if inp[answer] not in ["X", "O"]:
      inp[answer] = "O"
      grid = f"|{inp[0]}|{inp[1]}|{inp[2]}|\n|{inp[3]}|{inp[4]}|{inp[5]}|\n|{inp[6]}|{inp[7]}|{inp[8]}|"
      print(grid)

      if o_win():
        print("O Wins")
      elif draw():
        print("Draw")
      else:
        x_turn()
    
    else:
      print("Square is occupied, please try again")
      o_turn()

def x_win():
  if (inp[0] == "X" and inp[1] == "X" and inp[2] == "X") or (inp[3] == "X" and inp[4] == "X" and inp[5] == "X") or (inp[6] == "X" and inp[7] == "X" and inp[8] == "X") or (inp[0] == "X" and inp[3] == "X" and inp[6] == "X") or (inp[1] == "X" and inp[4] == "X" and inp[7] == "X") or (inp[2] == "X" and inp[5] == "X" and inp[8] == "X") or (inp[0] == "X" and inp[4] == "X" and inp[8] == "X") or (inp[2] == "X" and inp[4] == "X" and inp[6] == "X"):
    return True

def o_win():
  if (inp[0] == "O" and inp[1] == "O" and inp[2] == "O") or (inp[3] == "O" and inp[4] == "O" and inp[5] == "O") or (inp[6] == "O" and inp[7] == "O" and inp[8] == "O") or (inp[0] == "O" and inp[3] == "O" and inp[6] == "O") or (inp[1] == "O" and inp[4] == "O" and inp[7] == "O") or (inp[2] == "O" and inp[5] == "O" and inp[8] == "O") or (inp[0] == "O" and inp[4] == "O" and inp[8] == "O") or (inp[2] == "O" and inp[4] == "O" and inp[6] == "O"):
    return True

def draw():
  if inp[0] != " " and inp[1] != " " and inp[2] != " " and inp[3] != " " and inp[4] != " " and inp[5] != " " and inp[6] != " " and inp[7] != " " and inp[8] != " ":
    return True

x_turn()
