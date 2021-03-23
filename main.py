#Board initilastion
height=11
width=11
board = [[" | " for x in range(width)] for y in range(height)]
board[height//2][width//2] = "🏙️  "
game = True

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
      self.lvl +=1
#Game loop
while game == True:
  for column in board:
    for i in column:
      print(f" {i} ", end="")
    print()
  Factory_1 = Building('🏭',1,3,3)
  Factory_1.place_building()

