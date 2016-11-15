import random as ran

def generate_random_number():
    new_sample = ran.sample(range(9),4)
    while(new_sample[0] == 0):
        new_sample = ran.sample(range(9),4)
    number_string = ''    
    for element in new_sample:
        number_string += str(element)
    return int(number_string)

def game(number_to_guess):
    game_running = True
    tries = 7

    while game_running:
        correct_digits_in_position = 0
        correct_digits = 0  
        if tries < 1:
            print("You ran out of tries. Game ended. Number:" + str(number))
            break
        player_input = int(input("Try to guess the number (only 4 digits please): "))
        if player_input != number_to_guess:
            number_to_guess_string = str(number_to_guess)
            player_input_string = str(player_input)    
            for list_index in range(len(number_to_guess_string)):
                if number_to_guess_string[list_index] == player_input_string[list_index]:
                    correct_digits_in_position += 1
                if player_input_string[list_index] in number_to_guess_string:
                    correct_digits += 1               
            print("Cows: " + str(correct_digits) + " Bulls: " + str(correct_digits_in_position))
            tries -= 1
        else:
            print("You won!!!")
            game_running = False
            
number = generate_random_number()
print("Game started")
game(number)
