keyboard = ["q","w","e","r","t","y","u","i","o","p",
"a","s","d","f","g","h","j","k","l",";",
"z","x","c","v","b","n","m",",",".","/"]
answer = "";
position =0;
direction = input();
sequence= input();
for x in range(len(sequence)):
    if direction == "R":
        position = keyboard.index(sequence[x]);
        answer = answer + keyboard[position-1];
    elif direction == "L":
        position = keyboard.index(sequence[x]);
        answer = answer + keyboard[position+1];

print(answer);
