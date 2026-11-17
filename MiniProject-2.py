import random
import tkinter as tk
from tkinter import messagebox

ranks=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
suits=['♠️','♥️','♦️','♣️']
Hide_card='🂠'

class Card:
    def __init__(self, rank, suit):
        self.rank=rank
        self.suit=suit

    def __str__(self):
        return f'{self.rank}{self.suit}'

class Player:
    def __init__(self,name):
        self.name=name
        self.hand=[]
        self.pairs=0

    def add_cards(self, cards):
        self.hand.extend(cards)

    def remove_by_rank(self, rank):
        remove_card=[card for card in self.hand if card.rank==rank]
        self.hand=[card for card in self.hand if card.rank!=rank]
        return remove_card

    def has_rank(self, rank):
        return any(card.rank==rank for card in self.hand)

    def find_pairs(self):
        rank_count={}
        for card in self.hand:
            rank_count[card.rank] = rank_count.get(card.rank, 0)+1

        for rank in list(rank_count):
            while rank_count[rank]>=2:
                self.remove_by_rank(rank)
                self.hand.append(Card(rank, random.choice(suits)))
                self.pairs+=1
                rank_count[rank]-=2

class Go_Fish:
    def __init__(self,root):
        self.root=root
        self.root.title('Go Fish')
        self.deck=self.create_deck()
        self.players=[Player('Player 1'), Player('Player 2')]
        self.turn=0
        self.drop_var=tk.StringVar()
        self.buttons=[]
        self.deal_cards()
        self.build_gui()
        self.updating()

        for player in  self.players:
            player.find_pairs()


    def create_deck(self):
        deck=[Card(rank,suit) for rank in ranks for suit in suits]
        random.shuffle(deck)
        return deck

    def deal_cards(self):
        for _ in range(7):
            for player in self.players:
                if self.deck:
                    player.hand.append(self.deck.pop())

    def build_gui(self):
        self.top_frame=tk.Frame(self.root)
        self.middle_frame=tk.Frame(self.root)
        self.bottom_frame=tk.Frame(self.root)
        self.top_frame.pack(pady=20)
        self.middle_frame.pack(pady=20)
        self.bottom_frame.pack(pady=20)

        self.status_label=tk.Label(self.bottom_frame, text='', font=('Times', 14))
        self.status_label.pack(pady=20)

        self.drop=tk.OptionMenu(self.bottom_frame,self.drop_var, '')
        self.drop.pack(pady=20)

        self.ask_button=tk.Button(self.bottom_frame, text='Ask', command=self.ask_for_card)
        self.ask_button.pack(pady=20)

        self.reveal_button=tk.Button(self.bottom_frame, text="Show Opponent's Card", command=self.reveal_opponent_cards)
        self.reveal_button.pack(pady=20)

    def updating(self):
        for widget in self.top_frame.winfo_children():
            widget.destroy()

        for widget in self.middle_frame.winfo_children():
            widget.destroy()

        current=self.players[self.turn]
        opponent=self.players[1-self.turn]

        player1_color='blue' if self.turn==0 else 'gray'
        tk.Label(self.top_frame, text=f'{self.players[0].name}-Pairs:{self.players[0].pairs}',fg=player1_color, font=('Times',16,'bold')).pack()
        for card in self.players[0].hand:
            if self.turn==0:
                buton=tk.Button(self.top_frame, text=str(card), command=lambda c=card: self.set_dropdown(c.rank))

            else:
                buton=tk.Button(self.top_frame, text=Hide_card, state='disabled')
            buton.pack(side='left')

        player2_color='blue' if self.turn==1 else 'gray'
        tk.Label(self.middle_frame,text=f'{self.players[1].name}-Pairs:{self.players[1].pairs}',fg=player2_color, font=('Times',16,'bold')).pack()
        for card in self.players[1].hand:
            if self.turn==1:
                buton=tk.Button(self.middle_frame, text=str(card), command=lambda c=card: self.set_dropdown(c.rank))
            else:
                buton=tk.Button(self.middle_frame, text=Hide_card, state='disabled')
            buton.pack(side='left')

        ranks_in_hand=sorted(set(card.rank for card in current.hand))
        self.drop_var.set(ranks_in_hand[0] if ranks_in_hand else '')
        menu=self.drop['menu']
        menu.delete(0,'end')
        for rank in ranks_in_hand:
            menu.add_command(label=rank,command=lambda value=rank: self.drop_var.set(value))

        self.status_label.config(text=f"{current.name}'s turn: Ask for a rank you have. ")

        if not current.hand or not opponent.hand:
            self.game_end()

    def set_dropdown(self, rank):
        self.drop_var.set(rank)

    def ask_for_card(self):
        rank=self.drop_var.get()
        current=self.players[self.turn]
        opponent=self.players[1-self.turn]

        if not current.has_rank(rank):
            self.status_label.config(text="You cannot ask for a rank you do not have")
            return

        if opponent.has_rank(rank):
            cards=opponent.remove_by_rank(rank)
            current.add_cards(cards)
            current.find_pairs()
            self.status_label.config(text=f'{current.name} got cards and continues ')

        else:
            self.status_label.config(text=f"{current.name} must Go Fish")
            if self.deck:
                drawn=self.deck.pop()
                current.hand.append(drawn)
                if drawn.rank==rank:
                    self.status_label.config(text=f'{current.name} fished the card and continue')
                    current.find_pairs()

                else:
                    current.find_pairs()
                    self.turn=1-self.turn
            else:
                self.turn=1-self.turn

        self.updating()

    def reveal_opponent_cards(self):
        opponent=self.players[1-self.turn]
        frame=self.top_frame if self.turn==1 else self.middle_frame
        for widget in frame.winfo_children():
            widget.destroy()

        tk.Label(frame, text=f'{opponent.name}-Pairs: {opponent.pairs}').pack()
        for card in opponent.hand:
            buton=tk.Button(frame, text=str(card), state='disabled')
            buton.pack(side='left')
        self.root.after(3000, self.updating)

    def game_end(self):
        p1=self.players[0].pairs
        p2=self.players[1].pairs
        if p1>p2:
            winner='Player 1 win'
        elif p2>p1:
            winner='Player 2 win'
        else:
            winner='Tie'
        messagebox.showinfo('Game over', f'Game over\nPlayer1:{p1} pairs\nPlayer 2:{p2} pairs\n{winner}')
        self.root.destroy()


if __name__=='__main__':
    root=tk.Tk()
    game=Go_Fish(root)
    root.mainloop()
