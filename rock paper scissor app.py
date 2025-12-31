from tkinter import *
import random
window = Tk()
window.geometry('400x400')
window.title('Rock Paper Scissor App')
window.configure(bg='lightgreen')
choices = ['Rock', 'Paper', 'Scissor']
def play_game(user_choice):
    computer_choice = random.choice(choices)
    if user_choice == computer_choice:
        result = 'Tie! Both chose ' + user_choice
    elif (user_choice == 'Rock' and computer_choice == 'Scissor') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissor' and computer_choice == 'Paper'):
        result = 'You Win! ' + user_choice + ' beats ' + computer_choice
    else:
        result = 'You Lose! ' + computer_choice + ' beats ' + user_choice
    result_label.config(text=result)
rock_button = Button(window, text='Rock', command=lambda: play_game('Rock'))
rock_button.pack(pady=10)
paper_button = Button(window, text='Paper', command=lambda: play_game('Paper'))
paper_button.pack(pady=10)
scissor_button = Button(window, text='Scissor', command=lambda: play_game('Scissor'))
scissor_button.pack(pady=10)
result_label = Label(window, text='', bg='lightgreen')
result_label.pack(pady=20)
window.mainloop()
