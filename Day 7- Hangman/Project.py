from random_word import RandomWords
import hangman_art

print("Welcome to ")
print(hangman_art.logo)

word = RandomWords().get_random_word().lower()
show_word = word
number_of_lives = 6
ans = "_" * len(word)
stages = hangman_art.stages
selected_list = []

while number_of_lives > 0:

    print(stages[number_of_lives])
    user_guess_letter = input("Guess the letter to see if its in a word or not? ").lower()
    if user_guess_letter in selected_list:
        print(f"You have already tried '{user_guess_letter}'. Try any other letter")
        print(f"lives left : {number_of_lives}")
        print(f"Letters which you have tried {selected_list}")
        continue
    selected_list.append(user_guess_letter)
    print(f"Letters which you have tried {selected_list}")

    if user_guess_letter in word:
        count = word.count(user_guess_letter)
        for i in range(0, count):
            index = word.index(user_guess_letter)
            word = word[:index] + "_" + word[index + 1:]
            ans = ans[:index] + user_guess_letter + ans[index + 1:]

        print("You have guess the\033[92m correct\033[0m letter.")
        print(f"lives left : {number_of_lives}")
        print(f"Current Progress : {ans}")

        if "_" not in ans:
            print("You have won the Game")
            break

    else:
        number_of_lives -= 1
        print(f"You have guess the\033[91m wrong!\033[0m letter.")
        print(f"lives left : {number_of_lives}")
        print(f"Current Progress : {ans}")

        if number_of_lives < 1:
            print(stages[0])
            print("Hangman is Dead. You have lose the Game.")
            print(f"The correct word is {show_word}")
