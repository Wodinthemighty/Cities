#Board initilisation
import os
import time
height=11
width=11
board = [[" | " for x in range(width)] for y in range(height)]
board[height//2][width//2] = "🏙️  "
game = True
h = ' '*10
Buildings = [[width//2,height//2]]
Options = ['1','2','3','4','factory','city','tunnel','nothing']
def clear_board():
 os.system("ls")
 time.sleep(1)
#initilizing variables for resources
plastique = 5
aqua_vida = 5
keilpe = 5
p = [0,0,0]

#Building data, creating buildings
class Building:
    def __init__(self,type,lvl,locationX,locationY):
      self.type = type
      self.lvl = 1
      self.locationX = locationX
      self.locationY = locationY
    def place_building(self):
      try:
        locationX,locationY = input('Where would you like to put it?\n\nPlease enter co-ordiantes seperated by a comma (e.g 3,2)\n').split(',',2)
        self.locationX = int(locationX)-1
        self.locationY = int(locationY)-1
        #Check if spot is taken
        if [self.locationX,self.locationY] in Buildings:
         raise ValueError("There is already a building there!")
        else:
         board[self.locationX][self.locationY] = self.type
         Buildings.append([self.locationX,self.locationY])
      except ValueError:
        print('Please re-enter coordiantes')
        self.place_building()
    def upgrade_building(self,type,lvl):
      self.lvl += 1
      p[type] +=1
#Player actions
def player_action():
 Errors = 0
 Yes = True
 while Errors < 5 and Yes == True:
  Errors += 1
  list_resources()
  print('\n'*3+'Would you like to build a:')
  print('1. A factory\n2. A city\n3. A tunnel\n4. Nothing, next round please.')
  X = input()
  if X in Options:
   if X in ['4','nothing']:
    print('You wait for the days to drift by...')
    Yes = False
   elif X in ['1','factory']:
     #This will check if resources are Avalible
    if plastique >=1 and aqua_vida >=1:
     #Create a generic building
     bob = Building('🏭  ',1,0,0)
     bob.place_building()
     p[0]+=1
     p[1]+=1
     p[2]+=1
    else:
      print('You cannot afford that.')
      player_action()
   elif X in ['2','city']:
    if plastique >=3 and aqua_vida >=3 and keilpe >=3:
     plastique+=-3
     aqua_vida+=-3
     keilpe+=-3
     bob = Building('🏙️  ',1,0,0)
     bob.place_building()
     p[2]+=-1
     p[1]+=-1
    else:
      print('You cannot afford that.')
      player_action()
   elif X in ['3','tunnel']:
    if plastique >=1 and aqua_vida >=0 and keilpe >=0:
     bob = Building('🚇  ',1,0,0)
     bob.place_building()
    else:
      print('You cannot afford that.')
      player_action()
#Possible to lose game through mistyping
 if Errors == 5:
   print('The people have lost faith in you, exile is the only option now...')
   print('Would you like to go into exile?')
   a = input()
   print('Goodbye')
   game =  False
def list_resources():
 print('\n'+h+'Avalible resources:\n\n')
 time.sleep(0.5)
 print(h+'You have '+str(plastique)+' Plasteel')
 time.sleep(0.5)
 print(h+'You have '+str(aqua_vida)+' Hydric Acid')
 time.sleep(0.5)
 print(h+'You have '+str(keilpe)+' Kelp')
 time.sleep(1.0)
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
 #Player actions (What would you like to build?)
 player_action()

#Generating resources
 plastique += p[0]
 aqua_vida += p[1]
 keilpe += p[2]
 Errors = 0
#lose the game from starvation
 if keilpe < 0 or aqua_vida < 0:
   print('Your people witness the end of days as you embrace the void...')
   game = False
