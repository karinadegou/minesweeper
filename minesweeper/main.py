import tkinter as tk
from tkinter import messagebox
import random

class Minesweeper:
    def __init__(self, master, size=10, mines=10):
        self.master = master
        self.size = size
        self.mines = mines
        self.buttons = []
        self.mine_positions = set()
        self.flagged_positions = set()  # 用于存储标记雷的方块
        self.revealed_positions = set()  # 用于存储已揭示的方块
        self.game_over = False

        # 初始化界面
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.create_buttons()
        self.place_mines()

    # 创建按钮矩阵
    def create_buttons(self):
        for row in range(self.size):
            button_row = []
            for col in range(self.size):
                button = tk.Button(self.frame, text='', width=2, height=1,
                                   command=lambda r=row, c=col: self.on_click(r, c))
                button.bind("<Button-3>", lambda event, r=row, c=col: self.on_right_click(r, c))  # 绑定右键点击事件
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    # 随机放置地雷
    def place_mines(self):
        while len(self.mine_positions) < self.mines:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            self.mine_positions.add((row, col))

    # 左键点击事件
    def on_click(self, row, col):
        if self.game_over or (row, col) in self.flagged_positions:
            return

        if (row, col) in self.mine_positions:
            self.buttons[row][col].config(text='*', bg='red')
            self.end_game(False)
        else:
            self.reveal(row, col)

        self.check_win()

    # 右键点击事件用于标记地雷
    def on_right_click(self, row, col):
        if self.game_over or (row, col) in self.revealed_positions:
            return

        if (row, col) in self.flagged_positions:
            # 如果已经标记，取消标记
            self.buttons[row][col].config(text='', bg='SystemButtonFace')
            self.flagged_positions.remove((row, col))
        else:
            # 标记雷
            self.buttons[row][col].config(text='F', bg='yellow')
            self.flagged_positions.add((row, col))

        self.check_win()

    # 递归揭示无雷区域
    def reveal(self, row, col):
        if self.buttons[row][col]['text'] != '' or (row, col) in self.revealed_positions:
            return

        nearby_mines = self.count_nearby_mines(row, col)
        self.buttons[row][col].config(text=str(nearby_mines), bg='lightgray')
        self.revealed_positions.add((row, col))

        if nearby_mines == 0:
            for r in range(max(0, row-1), min(self.size, row+2)):
                for c in range(max(0, col-1), min(self.size, col+2)):
                    self.reveal(r, c)

    # 计算相邻雷数
    def count_nearby_mines(self, row, col):
        count = 0
        for r in range(max(0, row-1), min(self.size, row+2)):
            for c in range(max(0, col-1), min(self.size, col+2)):
                if (r, c) in self.mine_positions:
                    count += 1
        return count

    # 结束游戏
    def end_game(self, won):
        self.game_over = True
        if won:
            messagebox.showinfo("Game Over", "You Win!")
        else:
            messagebox.showinfo("Game Over", "You Hit a Mine!")

        # 显示所有地雷
        for row, col in self.mine_positions:
            self.buttons[row][col].config(text='*', bg='red')

    # 检查是否获胜
    def check_win(self):
        if len(self.revealed_positions) + len(self.mine_positions) == self.size ** 2 and \
           self.flagged_positions == self.mine_positions:
            self.end_game(True)

# 主程序
def main():
    root = tk.Tk()
    root.title("Minesweeper")
    game = Minesweeper(root, size=10, mines=10)
    root.mainloop()

if __name__ == "__main__":
    main()
