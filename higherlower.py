import art
import game_data
import random

def details(info):
    return f"{info['name']}, A {info['description']}, From {info['country']}"
SCORE = 0
B = game_data.data[random.randint(0,len(game_data.data)-1)]

winning = True
while winning:
    A = B
    B = game_data.data[random.randint(0,len(game_data.data)-1)]
    if B == A:
        B = game_data.data[random.randint(1, len(game_data.data))]

    print(art.logo)
    print(f"Compare A : {details(A)}")
    print(art.vs)
    print(f"Against B: {details(B)}")
    print(f'Your score {SCORE}')
    user_choice = input("Who has more followers? Type 'A' or 'B' : ")
    if user_choice.lower() == 'a':
        if A['follower_count'] > B['follower_count']:
            SCORE += 1

        else:
            print(f'Your Final Score {SCORE}')
            print('Wrong GUESS, You Loose')
            winning = False

    elif user_choice.lower() == 'b':
        if B['follower_count'] > A['follower_count']:
            SCORE += 1

        else:
            print(f'Your Final Score {SCORE}')
            print('Wrong GUESS, You Loose')
            winning = False
