#Board initilisation
import os
import time
import random
height=11
width=11
def one(num):
 return num+1
board = [[" | " for x in map(one,range(width))] for y in map(one,range(height))]
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
p = [1,-1,-1]
points = 1
turn_count = 0
max_turns = random.randint(5,15)
#construction queue
c_list = []
#Building data, creating buildings
class Building:
    def __init__(self,type,lvl,locationX,locationY):
      self.type = type
      self.lvl = 1
      self.locationX = locationX
      self.locationY = locationY
    def place_building(self):
      try:
        global built
        locationX,locationY = input('Where would you like to put it?\n\nPlease enter co-ordiantes seperated by a comma (e.g 3,2)\n').split(',',2)
        self.locationX = int(locationX)
        self.locationY = int(locationY)
        #Check if spot is taken
        try:
         if [self.locationX,self.locationY] in Buildings:
          print("There is already a building there!")
          raise ValueError()
         elif tunnel_check(self.locationY,self.locationX) or self.type == '🚇  ':
          board[self.locationY][self.locationX] = self.type
          Buildings.append([self.locationX,self.locationY])
          built = True
          print('It has been added to the list.\n')
         else:
          print('You need to build next to a tunnel!')
          raise ValueError()
        except:
         raise ValueError()
      except ValueError:
        print('Please re-enter coordiantes\npress anything to re-enter, or Z to cancel')
        if input() != 'z':
         self.place_building()
        else:
         built = False
    def upgrade_building(self,type,lvl):
      self.lvl += 1
      p[type] +=1
#Check if location is next to a tunnel
def tunnel_check(X,Y):
  try:
    if board[X][Y-1] == '🚇  ':
      return True
    if board[X][Y+1] == '🚇  ':
      return True
    if board[X-1][Y] == '🚇  ':
      return True
    if board[X+1][Y] == '🚇  ':
      return True
    else:
      return False
  except:
   if board[X-1][Y] == '🚇  ':
    return True
   if board[X][Y-1] == '🚇  ':
    return True
   else:
    return False
  

#Player actions
def player_action():
 Errors = 0
 Yes = True
 while Errors < 5 and Yes == True:
  list_resources()
  print('\n'*3+'Would you like to build a:')
  print('1. A factory\n2. A city\n3. A tunnel\n4. Nothing, next round please.')
  X = input()
  if X in Options:
   global plastique
   global aqua_vida
   global keilpe
   if X in ['4','nothing']:
    print('You wait for the days to drift by...')
    Yes = False
   elif X in ['1','factory']:
     #This will check if resources are Avalible
    if plastique >=1 and aqua_vida >=1:
     #Create a generic building
     bob = Building('🏭  ',1,0,0)
     bob.place_building()
     if built:
      plastique+=-1
      aqua_vida+=-1
      p[0]+=1
      p[1]+=1
      p[2]+=1
    else:
      print('You cannot afford that.')
      player_action()
   elif X in ['2','city']:
    if plastique >=3 and aqua_vida >=3 and keilpe >=3:
     bob = Building('🏙️  ',1,0,0)
     bob.place_building()
     if built:
      plastique+=-3
      aqua_vida+=-3
      keilpe+=-3
      p[2]+=-1
      p[1]+=-1
      points += 1
    else:
      print('You cannot afford that.')
      player_action()
   elif X in ['3','tunnel']:
    if plastique >=1 and aqua_vida >=0 and keilpe >=0:
     bob = Building('🚇  ',1,0,0)
     bob.place_building()
     if built:
      plastique+=-1
    else:
      print('You cannot afford that.')
      player_action()
  else:
   Errors += 1
#Possible to lose game through mistyping
 if Errors == 5:
   print('The people have lost faith in you, exile is the only option now...')
   print('Would you like to go into exile?')
   if input() != False:
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
#building 
#lose the game from starvation
 if keilpe < 0 or aqua_vida < 0:
   print('Your people witness the end of days as you embrace the void...')
   game = False
 turn_count +=1
 if turn_count == max_turns:
  print('The game is over, you sucessfully saved '+str(points)+' million people, the people thank you')
  break
