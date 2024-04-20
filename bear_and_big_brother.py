bear_limak, bear_bob = [x for x in map(int,input().split())];
years = 0;
if bear_limak == bear_bob:
    years+=1;
else:
    while bear_limak <= bear_bob:
        bear_limak*=3;
        bear_bob*=2;
        years+=1;

print(years);
