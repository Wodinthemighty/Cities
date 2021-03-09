height=3
width=3
board = [[" | " for x in range(width)] for y in range(height)]
board[height//2][width//2] = "🏙️  "
for column in board:
  for i in column:
    print(f" {i} ", end="")
  print()
