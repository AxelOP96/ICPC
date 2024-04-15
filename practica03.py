#Ejercicios más sencillos - Operadores y control de flujo (opcionales)
#    1) Leer una variable booleana por consola y escribir "SI" si es verdadera y "NO" si es falsa.
varBooleana = bool(input());
if varBooleana:
    print("SI");
else:
    print("NO");
#2) Leer dos variables booleanas por consola y escribir "SI" si ambas son verdaderas y "NO" en caso contrario.
varBooleana1 = bool(input());
varBooleana2 = bool(input());
if varBooleana1 and varBooleana2:
    print("SI");
else:
    print("NO");
#3) Leer dos variables booleanas por consola y escribir "SI" si al menos una es verdaderas y "NO" en caso contrario.
varBooleana1 = bool(input());
varBooleana2 = bool(input());
if varBooleana1 or varBooleana2:
    print("SI");
else:
    print("NO");
#4) Leer dos variables booleanas por consola y escribir "SI" si al una y solo una es verdaderas y "NO" en caso contrario.
varBooleana1 = bool(input());
varBooleana2 = bool(input());
if varBooleana1 ^ varBooleana2:
    print("SI");
else:
    print("NO");
#5) Leer 3 números enteros a, b, c e indicar si están bien ordenados ( (a<=b) y (b<=c) ) o no.
a = int(input());
b = int(input());
c = int(input());
if a <= b and b <=c:
    print("Estan ordenados");
else:
    print("No estan ordenados");
#6) Leer 3 números enteros a, b, c e indicar si a es un divisor tanto de b como de c o no.
numA = int(input());
numB = int(input());
numC = int(input());
if b % a ==0 and c % a ==0:
    print("A es divisor");
else:
    print("No es divisor");
#7) Leer un carácter y decir si es:
#        - Una letra mayúscula del alfabeto inglés
#        - Una letra minúscula del alfabeto inglés
#        - Un número [0 a 9]
#        - Otro carácter
caracter = input();
if caracter.isupper():
    print("Es mayuscula");
if caracter.islower():
    print("Es minuscula");
if caracter.isdigit():
    print("Es numero");
else:
    print("Es otro caracter");
#8) Leer 3 enteros a, b, c que representan las longitudes de los lados de un triángulo en indicar si es:
#        - Equilátero: Los 3 lados son iguales.
#        - Isósceles: Hay 2 lados iguales y otro distinto.
#        - Escaleno: Los 3 lados tienen distinta longitud.
lado1 = int(input());
lado2 = int(input());
lado3 = int(input());

if lado1 == lado2 and lado2 == lado3:
    print("Es equilatero");
if lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("Es isosceles");
if lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print("Es escaleno");
