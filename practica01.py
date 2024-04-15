#1) Declarar una variable entera, leerla por consola y luego escribirla por consola.
entera = int(input());
print(entera);
# 2) Declarar 2 variables enteras, leerlas por consola y mostrar por consola los siguientes valores:
#         La suma de ambas variables.
#         El producto de ambas variables.
#         El resultado de la resta entre la primera y la segunda variable.
#         El cociente de dividir la primera variable por la segunda.
#         El resto de dividir a la primera variable por la segunda.
entera1 = int(input());
entera2 = int(input());
print(entera1 + entera2);
print(entera1 * entera2);
print(entera1 - entera2);
print(entera1 / entera2);
print(entera1 % entera2);

#3) Leer 3 variables enteras por consola y mostrar el resultado de sumar las primeras 2 y multiplicar el resultado por la tercera.
num1 = int(input());
num2 = int(input());
num3 = int(input());
print((num1 + num2)*num3)
#4) Leer la longitud de los catetos de un triángulo rectángulo (2 valores enteros) y mostrar por pantalla el cuadrado de la longitud de la hipotenusa.
cateto1 = int(input());
cateto2 = int(input());
print(((cateto1**2) + (cateto2**2))**2);
#5) Leer 4 enteros a, b, c , x, y mostrar el valor de a* x^2 + b*x + c.
a = int(input());
b = int(input());
c = int(input());
x = int(input());
print(a * (x**2) + (b*x) +c);
#6) Inicializar 2 variables u = 10, v = 6, y mostrar por pantalla el resultado de hacer (u* v)/v y de hacer v*(u/v).
u = 10;
v = 6;
operacion = (u*v)/v;
operacion2 = v*(u/v);
print(operacion);
print(operacion2);
#7) Leer un número n y mostrar cuántos números pares hay entre 1 y n (inclusive)
n = int(input());
count =0;
i=1;
for i in range(n):
    if i%2==0:
        count+=1;

print(count);
#8) Leer cuatro números a,b,c,d y mostrar por pantalla el resultado de hacer (a* b)/(c* d) y el de hacer (a/c)*(b/d).
numA = int(input());
numB = int(input());
numC = int(input());
numD = int(input());
print((numA*numB)/(numC*numD));
#9) Leer 3 números a, b, c y escribir el volumen de un prisma de a x b x c (prisma: Una caja donde un lado mide a, otro lado mide b y otro lado mide c)
numeroA = int(input());
numeroB = int(input());
numeroC = int(input());
print(numeroA * numeroB * numeroC);
#10) Guardar en una variable el valor 100000 y luego guardar en otra variable el resultado de multiplicar a la primera por sí misma y mostrar el contenido de esta segunda variable en pantalla.
valor = 10000;
otraVar = valor * valor;
print(otraVar);
