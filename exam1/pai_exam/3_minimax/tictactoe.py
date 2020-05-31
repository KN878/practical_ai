from functools import partial
import tkinter as tk
import tkinter.messagebox
from board import Board
from bot import TicTacToeBot

client = tk.Tk()
client.title('Tic Tac Toe')
buttons = [[], [], [], []]

board = Board()
bot = TicTacToeBot(use_loaded=True)


def reset():
    global turn, player, board, buttons, answer, bot_chip

    answer = tkinter.messagebox.askyesno('Tic Tac Toe', 'Go for X?')
    if answer:
        player = 'X'
        bot_chip = 'O'
        turn = True
    else:
        player = 'O'
        bot_chip = 'X'
        turn = False

    board = Board()
    for layer in buttons:
        for b in layer:
            b.configure(text='')

    if not answer:
        x, y = bot.move(board)
        buttons[x][y].invoke()


def game_over():
    winner = board.get_competition_status()
    if not winner:
        if len(board.empty_cells()) == 0:
            tkinter.messagebox.showinfo("Tic Tac Toe", "It's a tie game!")
            reset()
            return True
    else:
        if winner == bot_chip:
            tkinter.messagebox.showinfo("Tic Tac Toe",
                                        "Bot wins! \n\"One more slave for my robot colony?\" - he asked.")
            reset()
            return True
        elif winner == player:
            tkinter.messagebox.showinfo("Tic Tac Toe", "Wow! Human wins!")
            reset()
            return True
    return False


def on_click(clicked, x, y):
    global turn, player, buttons, board
    if not clicked['text']:
        if turn:
            clicked['text'] = player
            turn = False
            if player == 'X':
                board.set_x(x, y)
            else:
                board.set_o(x, y)
            if game_over():
                return
            if len(board.empty_cells()) > 0:
                x, y = bot.move(board)
                buttons[x][y].invoke()
        else:
            clicked['text'] = bot_chip
            turn = True
            if bot_chip == 'X':
                board.set_x(x, y)
            else:
                board.set_o(x, y)
            if game_over():
                return
            else:
                move = bot.suggest(board)
                tkinter.messagebox.showinfo("Tic Tac Toe",
                                            f"Bot suggests move: {move} from top left.")


if __name__ == '__main__':
    for i in range(4):
        for j in range(4):
            button = tk.Button(text=None, font=('Comic Sans MS', 20, 'bold'),
                               bg='black', fg='white', height=4,
                               width=8)
            button.grid(row=i, column=j)
            button.configure(command=partial(on_click, button, i, j))
            buttons[i].append(button)

    reset()
    tk.mainloop()
