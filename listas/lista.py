# listas

#inicializar un arreglo 
lista=[2,4,67,8,9.04,56] 

print(lista[2])

#Agregar un elemento a la lista: metodo append() 
#una funcion que realiza un objeto, en este caso el objeto lista 

print(lista)
lista.append(8)
print(lista)

#insert(), funcion que agrega un elemto en cualquier lugar del objeto lista 
print(lista)
lista.insert(1,2)
print(lista)

# agregar una lista a otra
lista2=[4,5,6,7]
lista+lista2
print(lista+lista2)
#tuplas: lista inmnutable, es decir, no se puede modificar
mitupla=(1,2,3)
mitupla2=(4,5,6)
print(mitupla+mitupla2)


mituplaE=(1.75,1.80,1.50,1.60,1.40,1.30,1.77,1.96,1.84,1.20)
mituplaP=(68,80,40,55,30,25,71,91,80,20)


print=(mituplaE)