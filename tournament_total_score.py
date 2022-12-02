#rock paper scissors tourney for tent close to snacks
#given an input encrypted guide to help win.
#Column of input shows what opponent will play; A - Rock, B - Paper, C - Scissors; 
#Second column ? Assumed what should be played  X         Y          Z Respectively
#Winner determined by highest score. 
#Total Score - sum of scores for each round.
#PTS: Rock - 1, Paper - 2, Scissors - 3; Outcome: lost - 0, draw: - 3, win - 6
#unsure if being tricked.
#Find score if everything goes like strategy guide.
#Part 2 - X - lose, Y - draw, Z - win

A, B, C = 1, 2, 3
X, Y, Z = 'lose', 'draw', 'win'
rounds = []
i = 1
template = [1, 2, 3]
lose = [3, 1, 2]
win = [2, 3, 1]

with open('Strategy_guide.txt') as file:
    for line in file.readlines():
        code = line.replace('\n', '').split(' ')

        enemy_elf = eval(code[0])
        me_elf = eval(code[1])

        if me_elf == 'draw':
            rounds.append(enemy_elf + 3)
        elif me_elf == 'lose':            
            for i in range(len(template)):
                if enemy_elf == template[i]:
                    rounds.append(lose[i])
                    break
            
        elif me_elf == 'win':
            for i in range(len(template)):
                if enemy_elf == template[i]:
                    rounds.append(win[i] + 6)
                    break

file.close()

score = sum(rounds)
print(f'Score with strategy guide is: {score}')

