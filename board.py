import tkinter as tk

LIGHT_WOOD = "#F0D9B5"
DARK_WOOD = "#855E42"


class ChessBoard:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Board")
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.board = {f"{chr(col)}{row}": None
                      for col in range(ord("A"), ord("H")+1) for row in range(1, 9)}
        self.draw_board()

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                x1 = col * 50
                y1 = row * 50
                x2 = x1 + 50
                y2 = y1 + 50
                if (row+col) % 2 == 0:
                    color = LIGHT_WOOD
                else:
                    color = DARK_WOOD
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)


root = tk.Tk()
board = ChessBoard(root)

root.mainloop()
