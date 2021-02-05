# define if a permutation group is
# odd or even

N = 10;
lst = [i for i in range(N)];
random.shuffle(lst);

def is_even(p):
  count = 0;
  i = 0;
  while (i< len(p)):
    k = i+1;
    while (k < len(p)):
      if (p[k] < p[i]):
        count += 1;
      k+=1;
    i+=1;
  if count == 0 or count % 2 == 0:
    return True;
  else:
    return False

is_even(lst);