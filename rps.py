import random

comp = random.choice(['s', 'r', 'p'])

user_input = input('Choose s, r, or p: ').lower() 

print(f'computer chose: {comp}')

if user_input not in ['s', 'r', 'p']:  
    print('You can enter s, r, or p.')
elif user_input == comp:
    print("It's a draw.")
else:
    if (user_input == 's' and comp == 'p') or \
       (user_input == 'r' and comp == 's') or \
       (user_input == 'p' and comp == 'r'):
        print('You win!')
    else:
        print('You lose.')
