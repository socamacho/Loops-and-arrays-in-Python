#Remember import random function here:

import random

my_list = [4,5,734,43,45]

#The magic is here:
for number in range(0,10):
    New_Random_Numbers = random.randint(1,10)
    my_list.append(New_Random_Numbers)
print(my_list)


#SOLUCION: Lo IDEAL es crear un for loop que sea recorrido 10 VECES.
#Luego dentro del scope, iniciado en la linea 9, se crean los numeros random y sea agregan a my_list.