# Question 1
# Given an n \times mn×m grid (where n,mn,m are integers),
# you would like to tile it with the minimal number of
# same size squares. Clearly, it can always be tiled with
# nmnm squares of size 1 \times 11×1, but it is not always
# optimal. For example, a 6 \times 106×10 grid can be tiled
# by 15 squares of size 2 \times 22×2:


# Your goal in this problem is to implement a function
# squares(n, m) that returns the minimum number of same size
# squares required to tile a grid of size n \times mn×m. Your
# code should work fast (in less than a second) even for
# n,mn,m up to 10e9.


def squares(n, m):
    f = gcd(n,m);
    l = n//f;
    k = m//f;
    sq = l*k
    print('a ({},{}) rectangle can be divided into {} ({},{}) squares'.format(n,m,sq,f,f));
    return sq

def gcd(a,b):
    assert a>=0 and b>=0 and a+b>0;
    while a>0 and b>0:
        if a>b:
            a = a%b;
        else:
            b = b%a;
    return max(a,b);

squares(10,2);
squares(10,5);
squares(11,10);
squares(100,10);
squares(101,10);
squares(100,90);
squares(13,27);
squares(985324462534,9841234245524);
