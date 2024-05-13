lines = int(input());
teamOne = "";
teamTwo= "";
countOne = 0;
countTwo =0;
for x in range(lines):
    team = input();
    if x ==0:
        teamOne = team;
        countOne = countOne +1;
    elif team != teamOne:
        teamTwo = team;
        countTwo = countTwo +1;
    elif team == teamOne:
        countOne = countOne +1;

if countOne < countTwo:
    print(teamTwo);
else:
    print(teamOne);
