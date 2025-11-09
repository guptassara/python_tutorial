import random

from _45_2_hangman_word_list import words

# dictionary of key:()


hangman_art = {
    0: ("      ", "     ", "     "),
    1: ("  o  ", "     ", "     "),
    2: ("  o  ", "  |  ", "     "),
    3: ("  o  ", " /|  ", "     "),
    4: ("  o  ", " /|\\ ", "     "),
    5: ("  o  ", " /|\\ ", " /   "),
    6: ("  o  ", " /|\\ ", " / \\ "),
}


def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letter = set()
    is_running = True

    print(r"""
                                                       ___
      /\  /\__ _ _ __   __ _ _ __ ___   __ _ _ __     / _ \__ _ _ __ ___   ___
     / /_/ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \   / /_\/ _` | '_ ` _ \ / _ \
    / __  / (_| | | | | (_| | | | | | | (_| | | | | / /_\\ (_| | | | | | |  __/
    \/ /_/ \__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| \____/\__,_|_| |_| |_|\___|
                       |___/
    """)

    print("⋆｡°✩  WELCOME TO HANGMAN  ✩°｡⋆")
    print("╭───────────────✿───────────────╮")
    print("     Guess the word correctly!    ")
    print("╰───────────────✿───────────────╯")

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input!")
            continue

        if guess in guessed_letter:
            print(f"{guess} is already guessed")
            continue

        guessed_letter.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("╔══════════════════╗")
            print("   🎉 YOU WIN!!! 🎉  ")
            print("╚══════════════════╝")

            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("╔══════════════════╗")
            print("   💀 YOU LOSE 💀   ")
            print("╚══════════════════╝")
            is_running = False
            print("╔═════════════════════════════╗")
            print("   🌸THANKS FOR PLAYING!!🌸   ")
            print("╚═════════════════════════════╝")


if __name__ == "__main__":
    main()
