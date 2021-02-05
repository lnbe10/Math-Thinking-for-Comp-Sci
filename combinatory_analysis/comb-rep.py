
from itertools import combinations_with_replacement


# Question 1
# Twenty people are voting for one of 5 candidates.
# They have secret ballot, each voter votes for one of 5 candidates.
# The result of an election is the number of votes for each of the candidate.
# How many possible results can this vote have (the result of the vote is
# determined by the number of votes for each candidate)?
# ( 20 + (5-1) )  =  ( 24 )
# (    5-1     )     (  4 )
#
count = 0;
for c in combinations_with_replacement("ABCDE", 20):
	count+=1;

print(count);

#Question 2
#We have 9 identical candies and we want to distribute them between 3 different
#sections of our bag. It does not matter which candies go to which section.
#How many ways do we have to do it?
# ( 9 + (3-1)  )  =  ( 11 )
# (    3-1     )     (  2 )
#


count = 0;
for c in combinations_with_replacement("ABC", 9):
	count+=1;

print(count);


#Question 1
#How many
#four-digit numbers are there such that their digits are non-increasing,
#that is each next digit is not greater than the previous one?
#Three-digit numbers are also four-digit, they just start with 0.

def fun(n):
	count = 0;
	for i in range(n):
	    for j in range(n):
	        for k in range(n):
	        	for l in range(n):
		            if i >= j and j >= k and k >= l:
		                count += 1

	print('for n = %d we have count = %d' %(n,count));
	return

fun(10)