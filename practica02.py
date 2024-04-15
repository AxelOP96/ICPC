#Ejercicios mas sencillos - Condicionales y control de flujo (opcionales)
#1) Leer 2 números enteros por consola y mostrar por consola el mayor de los 2.
entero1 = int(input());
entero2 = int(input());
if entero1 < entero2:
    print(entero2);
else:
    print(entero1);
#2) Leer un número entero por consola en indicar si es par o impar.
esPar = int(input());
if esPar % 2 == 0:
    print("Es par");
else:
    print("Es impar");
#3) Leer 2 números enteros por consola y decir si el primero es múltiplo del segundo.
ent1 = int(input());
ent2= int(input());
if ent1% ent2 ==0:
    print("Es multiplo");
else:
    print("No es multiplo");
#4) Leer un número entero por consola y decir si es positivo, 0 o negativo.
entero = int(input());
if entero ==0:
    print("Es cero");
if entero < 0:
    print("Es negativo");
if 0 < entero:
    print("Es positivo");
#5) Leer dos caracteres y escribir el menor por pantalla.
caracter1 = input();
caracter2 = input();
if caracter1 < caracter2:
    print(caracter1);
else:
    print(caracter2);
#6) Leer dos palabras y escribir la que es lexicográficamente menor.
palabra1 = input();
palabra2 = input();
if palabra1 < palabra2:
    print(palabra1);
else:
    print(palabra2);
#7) Leer 4 enteros, h1, b1, h2, b2 que son la base y altura de dos rectángulos e indicar cuál de los dos tiene mayor área o si tienen la misma área.
h1 = int(input());
b1 = int(input());
h2 = int(input());
b2 = int(input());
area1 = h1 * b1;
area2 = h2 * b2;
if area1 < area2:
    print("El Area del segundo es mayor");
if area1 == area2:
    print("Tienen el mismo area");
if area2 < area1:
    print("El area del primero es mayor");

#8) Si se tienen N niños y M caramelos, leer N y M e indicar si es o no posible dar la misma cantidad de caramelos a cada niño sin que sobre ningún caramelo.
n = int(input());
m = int(input());
if m % n ==0:
    print("Es posible, No sobran caramelos");
else:
    print("No es posible, Sobran caramelos");
#9) Leer dos números x e y, si x es múltiplo de y imprimir por pantalla el valor x/y, sino imprimir por pantalla el valor (x/y)+1.
x = int(input());
y = int(input());
if y % x ==0:
    print(x/y);
else:
    print((x/y)+1);
