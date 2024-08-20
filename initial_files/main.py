import random
from art import logo


def deal_card():
    """
    Return a random card from the deck. With replacement.
    'A' can be used as 1 or 11. Initially A is used as 11.
    J, Q, K all equal to 10
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """
    Take a list of cards and return the sum of these cards
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # if A in the cards and the sum is over 21, then 1 will be used instead of 11
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, com_score):
    """
    Here the user_score and computer_score will be compared.
    :param user_score: integer
    :param com_score: int
    :return: str
    """
    if user_score < 22 and com_score < 22:
        if com_score == 0:
            return 'You lose, opponent has Blackjack'
        elif user_score == 0:
            return 'You win with a Blackjack!'
        elif com_score > user_score:
            print('You lose!')
        elif com_score == user_score:
            print('Draw')
        else:
            print('You win!')
    elif user_score < 22 and com_score > 21:
        print('You win!')
    elif user_score > 21 and com_score < 22:
        print('You lose!')
    else:
        print('Draw!')


def play_game():
    print(logo)

    your_cards = []
    computer_cards = []
    current_score = -1
    computer_score = -1
    is_game_over = False

    # Initially, you and computer all get 2 cards.
    for i in range(2):
        your_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        current_score = calculate_score(your_cards)
        computer_score = calculate_score(computer_cards)
        print(f'Your cards: {your_cards}, current score: {current_score}')
        print(f'Computer\'s first card: {computer_cards[0]}')

        if current_score == 0 or computer_score == 0 or current_score > 21:
            is_game_over = True
        else:
            user_should_deal = input('Type "y" to get another card, type "n" to pass: ')
            if user_should_deal == 'y':
                your_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f'Your final hand: {your_cards}, final score: {current_score}')
    print(f'Computer\'s final hand: {computer_cards}, final score: {computer_score}')
    compare(current_score, computer_score)


while input('Do you want to play a game of Blackjack? Type "y" or "n": ').lower() == 'y':
    print('\n' * 100)
    play_game()
