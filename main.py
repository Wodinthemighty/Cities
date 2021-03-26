#Board initilisation
import os
import time
height=11
width=11
board = [[" | " for x in range(width)] for y in range(height)]
board[height//2][width//2] = "🏙️  "
game = True
h = ' '*10
Errors = 0
Options = ['1','2','3','4','factory','city','tunnel','nothing']
def clear_board():
 os.system("ls")
 time.sleep(1)
#initilizing variables for resources
plastique = 0
aqua_vida = 0
keilpe = 0
p = [0,0,0]

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
      p[type] +=1
#Game loop
while game == True:
#resetting game board
 clear_board()
 print('\n'*30)
 for column in board:
  for i in column:
   print(f" {i} ", end="")
  print()
  print(' ')
 print('\n'+h+'Avalible resources:\n\n')
 time.sleep(0.5)
 print(h+'You have '+str(plastique)+' Plasteel')
 time.sleep(0.5)
 print(h+'You have '+str(aqua_vida)+' Hydric Acid')
 time.sleep(0.5)
 print(h+'You have '+str(keilpe)+' Kelp')
 time.sleep(1.0)
 print('\n'*3+'Would you like to build a:')
 print('1. A factory\n2. A city\n3. A tunnel\n4. Nothing, next round please.')
 if Errors < 5:
  X = input()
  if X in Options:
   break
  else:
   Errors+=1
#Generating resources
 plastique += p[0]
 aqua_vida += p[1]
 keilpe += p[2]
