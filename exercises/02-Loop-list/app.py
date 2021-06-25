my_list = [232,32,1,4,55,4,3,32,3,24,5,5,5,34,2,35,5365743,52,34,3,55]

#Your code go here:
#print(my_list[0])

#Solucion incorrecta:
#for each_item in (my_list[0],[-1]):
    #print(my_list)


#SOLUCION 1:
#for each_item in my_list:
    #print(each_item)    

#NOTA: my_list no necesita parametros ni nada. Unicamente el nombre de la lista.    


#SOLUCION 2:
for position in range(0,len(my_list)):
    print(my_list[position])