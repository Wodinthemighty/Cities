#Board initilisation
import os
import time
height=11
width=11
board = [[" | " for x in range(width)] for y in range(height)]
board[height//2][width//2] = "🏙️  "
game = True

def clear_board():
 os.system("ls")
 time.sleep(1)

#Building data, creating buildings
class Building:
    def __init__(self,type,lvl,locationX,locationY):
      self.type = type
      self.lvl = 1
      self.locationX = locationX
      self.locationY = locationY
    def place_building(self):
      board[self.locationX][self.locationY] = self.type
    def upgrade_building(self,type,lvl):
      self.lvl += 1
#Game loop
while game == True:
#resetting game board
  clear_board()
  for column in board:
    for i in column:
      print(f" {i} ", end="")
    print()
    print(' '*110)

