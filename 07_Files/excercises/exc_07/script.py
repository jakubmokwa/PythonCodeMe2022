import random


def check_guess(word, game_word):
    if len(word) == 1 or len(word) == len(game_word):
        return True
    return False


def get_guess(game_word, num_of_rounds, round_num):
    while True:
        word = input(f"Write your letter or guess the word ({num_of_rounds - round_num} guesses left) -> ")
        if check_guess(word, game_word):
            return word
        else:
            print("Error, your guess isn't a single letter or a word with the same amount of letters as required")


def get_random_word(word_list):
    return random.choice(word_list)


def convert_list_to_string(word):
    new = ''
    for letter in word:
        new += letter
    return new


def game_end(player_won, game_word):
    if player_won:
        print(f"Player won, the word was:", end=' ')
    else:
        print(f"Pc won, the word was:", end=' ')
    print(convert_list_to_string(game_word))


def print_previous_letters(past_letter):
    print("Previous letters/words: ", end="")
    print(*past_letter)


def game_round(num_of_rounds, game_word, player_word):
    round_num = 0
    guessed = 0
    print_past_letter_flag = 0
    print(*player_word)
    past_letter = list()
    while round_num < num_of_rounds:
        if print_past_letter_flag != 0:
            print_previous_letters(past_letter)
        if '_' not in player_word:
            player_won = 1
            game_end(player_won, game_word)
            break
        round_guess = get_guess(game_word, num_of_rounds, round_num)
        round_guess = round_guess.lower()
        past_letter.append(round_guess)
        if len(round_guess) == 1:
            for index, letter in enumerate(game_word):
                if letter == round_guess:
                    player_word[index] = round_guess
                    guessed = 1
            if guessed:
                guessed = 0
                print(*player_word)
                print_past_letter_flag = 1
                continue
        else:
            if list(round_guess) == game_word:
                player_won = 1
                game_end(player_won, game_word)
                break
        print(*player_word)
        print_past_letter_flag = 1
        round_num += 1


def print_file_names():
    print("Choose one: ")
    print("- sweets")
    print("- fruits")


def get_list_set():
    while True:
        print_file_names()
        match input():
            case "sweets":
                with open('sweets.txt') as f:
                    content = f.read()
                    content = content.split()
                    return content
            case 'fruits':
                with open('fruits.txt') as f:
                    content = f.read()
                    content = content.split()
                    return content
            case _:
                print("None selected")


def main():
    word_list = get_list_set()
    num_of_rounds = 12
    game_word = list(get_random_word(word_list))
    player_word = list('_' * len(game_word))
    game_round(num_of_rounds, game_word, player_word)


main()
