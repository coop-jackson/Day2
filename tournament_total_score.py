#rock paper scissors tourney for tent close to snacks
#given an input encrypted guide to help win.
#Column of input shows what opponent will play; A - Rock, B - Paper, C - Scissors; 
#Second column ? Assumed what should be played  X         Y          Z Respectively
#Winner determined by highest score. 
#Total Score - sum of scores for each round.
#PTS: Rock - 1, Paper - 2, Scissors - 3; Outcome: lost - 0, draw: - 3, won - 6
#unsure if being tricked.
#Find score if everything goes like strategy guide.
A, X = 1, 1
B, Y = 2, 2
C, Z = 3, 3

draw, win = 3, 6
rounds = []
i = 1
with open('Strategy_guide.txt') as file:
    for line in file.readlines():
        code = line.replace('\n', '').split(' ')

        enemy_elf = eval(code[0])
        me_elf = eval(code[1])

        if enemy_elf == me_elf:
            rounds.append(me_elf + draw)
        elif (enemy_elf - me_elf == 1 or enemy_elf - me_elf == -2):            
            rounds.append(me_elf)
        elif (enemy_elf - me_elf == -1 or enemy_elf - me_elf == 2):
            rounds.append(me_elf + win)        
file.close()

score = sum(rounds)
print(f'Score with strategy guide is: {score}')

