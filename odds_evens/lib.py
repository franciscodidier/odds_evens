import random

def odds_or_evens():
    number = input("Let's play 'odds or evens'. We both choose one number between 0 and 5 at the same time, and then we sum the result. \n If the result is an even number, I win; else, you're the winner!\n Pick an integer number between 0 and 5:\n>")
    number = int(number)
    if number not in range(6):
        print('YOU SHOULD HAVE CHOSEN A NUMBER BETWEEN 1 AND 5, YOU FOOL!')
        print('\nGoodbye!')
    else:
        my_number = random.randint(1, 5)
        print(f'So you picked {number}, while I chose {my_number}')
        result = number + my_number
        if result in [2, 4, 6, 8, 10]:
            print(f'{number} + {my_number} = {result}.  {result} is even. \n YEAH, I WON! I AM AWESOME')
        else:
             print(f'{number} + {my_number} = {result}. {result} is odd. \n OH NO, YOU WON! DAMN IT!')

if __name__ == "__main__":
    print(odds_or_evens())
