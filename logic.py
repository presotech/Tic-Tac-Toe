TOP_LEFT   = (80, 50)
TOP_MID    = (350, 50)
TOP_RIGHT  = (630, 50)

MID_LEFT  = (80, 250)
MID_MID   = (350, 250)
MID_RIGHT = (630, 250)

BOTTOM_LEFT  = (80, 450)
BOTTOM_MID   = (350, 450)
BOTTOM_RIGHT = (630, 450)

def get_box(pos):
    """ get hardcoded centered box for mouse click """
    boxes = [
        [TOP_LEFT, TOP_MID, TOP_RIGHT],
        [MID_LEFT, MID_MID, MID_RIGHT],
        [BOTTOM_LEFT, BOTTOM_MID, BOTTOM_RIGHT]
    ]

    x, y = pos

    return boxes[x][y]

def check_board(board, players):
    """ check the board to see who won

        if someone won, return them, otherwise return if board is full.
    """

    check = lambda player, line: player * 3 == "".join(line)

    cols = [
        [board[i][0] for i in range(3)],        
        [board[i][1] for i in range(3)],        
        [board[i][2] for i in range(3)]
    ]

    ldag = [
        board[0][0], board[1][1], board[2][2]
    ]

    rdag = [
        board[0][2], board[1][1], board[2][0]
    ]

    has_empty_box = False

    for player in players:
        if check(player, ldag) or check(player, rdag):
            return player
        
        for row in board:
            if " " in row:
                has_empty_box = True

            if check(player, row):
                return player
        
        for col in cols:
            if check(player, col):
                return player

    # check if its a draw, assuming we found no lines above indicating a player won    
    return has_empty_box

def move(pos, player, board):
    """ move player with converted position """
    x, y = pos

    if board[x][y] != " ":
        return False

    board[x][y] = player
    return True

# this could be better, will eventually refactor
def convert(pos):
    """ takes mouse coords and convert to 2d array coords """
    x, y = pos

    is_in = lambda n, min, max: n >= min and n <= max

    rows = ["0,200", "201,400", "401,600"]
    cols = ["0,267", "268,535", "536,800"]

    for row in rows:
        min, max = [int(i) for i in row.split(",")]

        if is_in(y, min, max):
            y = rows.index(row)

    for col in cols:
        min, max = [int(i) for i in col.split(",")]

        if is_in(x, min, max):
            x = cols.index(col)
    
    # need a better way than reversing this for it to work
    # duct tape fix
    return (y, x)

def gen_board():
    """ generate the game board """
    return [[" " for _ in range(3)] for _ in range(3)]
