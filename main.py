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
      loactionX,locationY = input('Where would you like to put it?\n\nPlease enter co-ordiantes seperated by a comma (e.g 3,2)\n').split(',',2)
      board[self.locationX][self.locationY] = self.type
    def upgrade_building(self,type,lvl):
      self.lvl += 1
      p[type] +=1
#Request building location
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
 #Player actions (What would you like to build?)
 #Also punishes player for not taking the game seriosly
 while Errors < 5:
  print('\n'*3+'Would you like to build a:')
  print('1. A factory\n2. A city\n3. A tunnel\n4. Nothing, next round please.')
  X = input()
  if X in Options:
   if X in ['4','nothing']:
     pass
   elif X in ['1','factory']:
     #This will check if resources are Avalible
    if True:
     Factory.building = 
     building.place_building()
   elif X in ['2','city']:
     pass
   elif X in ['3','tunnel']:
     pass
  else:
   Errors+=1
#Possible to lose game through mistyping
 if Errors == 5:
   print('The people have lost faith in you, exile is the only option now...')
   print('Would you like to go into exile?')
   a = input()
   print('Goodbye')
   game =  False
#Generating resources
 plastique += p[0]
 aqua_vida += p[1]
 keilpe += p[2]
 Errors = 0
