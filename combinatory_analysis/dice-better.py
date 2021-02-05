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



def compute_strategy(dices):

	assert all(len(dice) == 6 for dice in dices)

	dice_wins = [0 for i in range(len(dices))];
	wins = [[] for i in range(len(dices))];
	strategy = dict();
	strategy["choose_first"] = True;
	strategy["first_dice"] = 0;

	for i in range(len(dices)):
		strategy[i] = (i + 1) % len(dices);


	for i in range(len(dices)):
		for j in range(i+1, len(dices)):
			versus = count_wins(dices[i], dices[j]);
			if versus[0]>versus[1]:
				dice_wins[i]+=1;
				wins[i].append(j);
				strategy[j]=i;
			if versus[1]>versus[0]:
				dice_wins[j]+=1;
				wins[j].append(i);
				strategy[i]=j;

	if max(dice_wins) == len(dices)-1:
		strategy["choose_first"] = True;
		strategy["first_dice"] = dice_wins.index(max(dice_wins));
		strategy.pop(dice_wins.index(max(dice_wins)));
	else:
		strategy["choose_first"] = False;

	print(wins);
	print(strategy);
	return strategy;


dices = [[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]];
compute_strategy(dices);
dices2 = [[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]];
#compute_strategy(dices2);