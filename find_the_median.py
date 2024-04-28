amount= int(input())
array = [];
result =0;

for i in range(amount):
    array.append(int(input()));

array.sort();
for i in range(len(array)):
    result = array[len(array)//2]

print(result);
