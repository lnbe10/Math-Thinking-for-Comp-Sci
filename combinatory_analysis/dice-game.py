# dice game:
# a shady person has various dices in a table
# the dices can have arbitrary values in their
# sides, like:
# [1,1,3,3,6,6]
# [1,2,3,4,5,6]
# [9,9,9,9,9,1]
# The shady person lets you see the dices
# and tell if you want to choose yor dice before
# or after him
# after both of you choose,
# them roll your dices, and see
# who wins (the one with bigger number showing up)

# to maximize the chances of winning, you have to
# do some tasks:
# 1- check if there's a dice better than all others
# 1.1 - if it exists, you choose first and select it
# 1.2 - if it doesn't exist, you let the shady person
#       choose a dice and you choose one wich is better
#       than his one .-.



def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0
    for i in dice1:
        for j in dice2:
            if i>j:
                dice1_wins+=1;
            if j>i:
                dice2_wins+=1;

    return (dice1_wins, dice2_wins)


dice1 = [1, 2, 3, 4, 5, 6];
dice2 = [1, 2, 3, 4, 5, 6];
count_wins(dice1,dice2);

dice3 = [1, 1, 6, 6, 8, 8];
dice4 = [2, 2, 4, 4, 9, 9];
count_wins(dice3,dice4);

def find_the_best_dice(dices):
	assert all(len(dice) == 6 for dice in dices)
	wins = [0 for i in range(len(dices))];
	for i in range(len(dices)):
		for j in range(i+1, len(dices)):
			versus = count_wins(dices[i], dices[j]);
			if versus[0]>versus[1]:
				wins[i]+=1;
			if versus[1]>versus[0]:
				wins[j]+=1;
	
	if max(wins) == len(dices)-1:
		#print('best dice is',  wins.index(max(wins)));
		return wins.index(max(wins));
	#print('no best dice');
	return -1

find_the_best_dice([[1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9], [3, 3, 5, 5, 7, 7]]);
find_the_best_dice([[3, 3, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [4, 4, 4, 4, 0, 0], [5, 5, 5, 1, 1, 1]]);
find_the_best_dice([[1, 1, 2, 4, 5, 7], [1, 2, 2, 3, 4, 7], [1, 2, 3, 4, 5, 6]]);

def compute_strategy(dices):
	assert all(len(dice) == 6 for dice in dices)

	strategy = dict()
	strategy["choose_first"] = True
	strategy["first_dice"] = 0
	for i in range(len(dices)):
		strategy[i] = (i + 1) % len(dices)

	if find_the_best_dice(dices) != -1:
		strategy["choose_first"] = True;
		strategy["first_dice"] = find_the_best_dice(dices);
	else:
		strategy["choose_first"] = False;
		for i in range(len(dices)):
			for j in range(i+1, len(dices)):
				versus = count_wins(dices[i], dices[j]);
				if versus[0]>versus[1]:
					strategy[j]=i;
				if versus[1]>versus[0]:
					strategy[i]=j;
	print(strategy);
	return strategy;

dices = [[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]];
compute_strategy(dices);
dices2 = [[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]];
#compute_strategy(dices2);



















