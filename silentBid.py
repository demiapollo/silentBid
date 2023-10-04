import os

def clear():
    os.system('clear')


bid_dic = {}
def add_new_bidder(person_name, their_bid):
    bid_dic[person_name] = their_bid


while True:
    name = input("What is your name? ")
    bid_amount = int(input("What's your bid? $"))
    add_new_bidder(name, bid_amount)
    follow_up = input("Are there any other bidders? Type 'yes' or 'no'.")
    clear()
    
    if follow_up == 'no':
        break

print(bid_dic)  
winner_name = max(bid_dic, key=bid_dic.get)
print(f"The winner is {winner_name} with a bid of ${bid_dic[winner_name]}.")