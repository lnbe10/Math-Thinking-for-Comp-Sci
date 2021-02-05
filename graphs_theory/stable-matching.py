def stableMatching(n, menPreferences, womenPreferences):
    unmarriedMen = list(range(n));
    manSpouse = [None] * n;
    womanSpouse = [None] * n;
    nextManChoice = [0] * n;
    count=0;
# While there exists at least one unmarried man:
    while unmarriedMen:
        # Pick an arbitrary unmarried man
        he = unmarriedMen[0]                      
        # Store his ranking in this variable for convenience
        hisPreferences = menPreferences[he]       
        # Find a woman to propose to
        she = hisPreferences[nextManChoice[he]] 
        # Store her ranking in this variable for convenience
        herPreferences = womenPreferences[she]
        # Find the present husband of the selected woman (it might be None)
        currentHusband = womanSpouse[she]         
        # Write your code here

        # Now "he" proposes to "she". 
        # Decide whether "she" accepts, and update the following fields
        # 1. manSpouse
        # 2. womanSpouse
        # 3. unmarriedMen
        # 4. nextManChoice
        # print('hispref: ', hisPreferences);
        # print('herpref: ', herPreferences)
        # print('he, currenthus, she: ', he, currentHusband, she);

        if currentHusband == None or herPreferences.index(he) < herPreferences.index(currentHusband):
            manSpouse[he] = she;
            womanSpouse[she] = he;
            if currentHusband != None:
                unmarriedMen.append(currentHusband);
            unmarriedMen.pop(0);
            if nextManChoice[he] < n:
                nextManChoice[he] += 1;
        
        else:
            nextManChoice[he] += 1;

        count+=1;
        # print(manSpouse, womanSpouse)

    print('cycles to stabilish: ', count);
    return manSpouse

assert(stableMatching(1, [ [0] ], [ [0] ]) == [0])
assert(stableMatching(2, [ [0,1], [1,0] ], [ [0,1], [1,0] ]) == [0, 1])

mp = [[2,1,3,0], [3,2,3,0], [1,2,1,0], [0,1,3,2]];
wp = [[3,1,3,0], [2,2,3,0], [0,2,1,0], [1,1,3,2]];
stableMatching(4, mp, wp)