#Board initilisation
import os
import time
import random
import math
#Custom board sizing
def get_size():
  try:
    global height
    global width
    width = int(input("how big a map do you want?"))
    if width > 0:
      a = ' '*width
    else:
     raise
    height = width
  except:
    print('Please enter a positive integer')
    get_size()
get_size()
#For mapping
def one(num):
 return num+1
#Creation of board
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
start_resources = 2+math.ceil(math.log(height,3))
plastique = start_resources
aqua_vida = start_resources
keilpe = start_resources
p = [1,-1,-1]
points = 1
turn_count = 0
max_turns = 7
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
        locationX,locationY = input('Where would you like to put it?\n'+'\u2014'*70+'\nPlease enter co-ordiantes seperated by a comma (e.g 3,2)\n').split(',',2)
        self.locationX = int(locationX)
        self.locationY = int(locationY)
        #Check if spot is taken
        try:
         if [self.locationX,self.locationY] in Buildings:
          print("There is already a building there!")
          raise ValueError()
         elif self.type == '🚇  ':
          board[self.locationY][self.locationX] = self.type
          Buildings.append([self.locationX,self.locationY])
          built = True
          print('It has been added to the list.\n')
         elif tunnel_check(self.locationY,self.locationX):
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
        print('Please re-enter coordiantes\nPress anything to re-enter, or Z to cancel')
        if input() != 'z':
         self.place_building()
        else:
         built = False
    def upgrade_building(self,type,lvl):
      self.lvl += 1
      p[type] +=1
#Check if location is next to a tunnel
#Additional excepts to deal with limited grid range
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
    if board[X+1][Y] == '🚇  ':
      return True
    if board[X][Y+1] == '🚇  ':
      return True
    if board[X-1][Y] == '🚇  ':
      return True
    if board[X][Y-1] == '🚇  ':
      return True
    return False
#Actions taken by the player
def player_action():
 Errors = 0
 Yes = True
 global points
 while Errors < 5 and Yes == True:
  print_board()
  print('It is now year '+str(turn_count)+' out of your 7 years')
  list_resources()
  print('\n'*3+'Would you like to build a:')
  print("1. A factory (1 H20 1 PLA)\n2. A city (2 H20 3 PLA 4 KLP)\n3. A tunnel (1 PLA)\n4. Nothing, next round please. (It's free!)")
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
    #Create a generic building, then give it specific qualities
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
      time.sleep(1)
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
      time.sleep(1)
      player_action()
   elif X in ['3','tunnel']:
    if plastique >=1 and aqua_vida >=0 and keilpe >=0:
     bob = Building('🚇  ',1,0,0)
     bob.place_building()
     if built:
      plastique+=-1
    else:
      print('You cannot afford that.')
      time.sleep(1)
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
#Delayed updated display of resources avalible to the player
def list_resources():
 print('\n'+h+'Avalible resources:\n\n')
 time.sleep(0.5)
 print(h+'You have '+str(plastique)+' Plasteel')
 time.sleep(0.5)
 print(h+'You have '+str(aqua_vida)+' Hydric Acid')
 time.sleep(0.5)
 print(h+'You have '+str(keilpe)+' Kelp')
 time.sleep(1.0)
#printing the board, removing the previous map
def print_board():
 print('\n'*37)
 for column in board:
  for i in column:
   print(f" {i} ", end="")
  print()
  print(' ')
#Game loop
while game == True:
#resetting game board
 clear_board()
 #Player actions (What would you like to build?)
 
 player_action()
 
#Generating resources
 plastique += p[0]
 aqua_vida += p[1]
 keilpe += p[2]
 #Resetting error count
 Errors = 0
#lose the game from starvation
 if keilpe < 0 or aqua_vida < 0:
   print('Your people witness the end of days as you embrace the void...')
   game = False
 turn_count +=1
 if turn_count == max_turns:
  print('The game is over, you sucessfully saved '+str(points)+' million people, ka pai!')
  break
