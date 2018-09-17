n = input()
i = 0
away_score = (away_goals * 3) + away_points
home_score = (home_goals * 3) + home_points 
while n < 4:
    n = input()
    if home_score > away_score :
        print "home win"
    elif home_score < away_score :
        print "away win"
    else:
        print "draw"
    i = i + 1
