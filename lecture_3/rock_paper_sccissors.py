keep_playing = True

player_1_score = 0
player_2_score = 0

while keep_playing == True:
    player_1_option = input('Player 1 please enter your option (r for rock, p for paper and s for scissors :')
    player_2_option = input('Player 2 please enter your option (r for rock, p for paper and s for scissors :')
    if player_1_option == player_2_option:
        print('There was a draw')
        player_1_score += 1
        player_2_score += 1
    elif (player_1_option == 'r' and player_2_option == 's') or (player_1_option == 's' and player_2_option == 'p') or (
            player_1_option == 'p' and player_2_option == 'r'):
        print('Player 1 won')
        player_1_score += 3
    else:
        print('Player 2 won')
        player_2_score += 3
    should_we_play_another_round = input('Do you want to play another round? y for yes, n for no: ')
    if should_we_play_another_round == 'y':
        keep_playing = True
    else:
        keep_playing = False

print('The score of player 1 is : {} and the score of player 2 is : {}'.format(player_1_score, player_2_score))
print('Hooray!')
