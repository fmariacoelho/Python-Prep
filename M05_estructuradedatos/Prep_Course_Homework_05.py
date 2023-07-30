#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:

lista=['BuenosAires','Londres','Madrid','lisboa','Roma','Mendoza']
print(lista)


# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:

print(lista[1])


# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:

print(lista[1:4])



# 4) Visualizar el tipo de dato de la lista

# In[12]:

print(type(lista))



# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:


print(lista[2:])


# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:


print(lista[3:])
    


# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:

lista.append('Paris')
lista.append('Mendoza')
print(lista)





# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:


lista.insert(3,'Pekin')
print(lista)

# In[21]:




# 9) Concatenar otra lista a la ya creada

# In[22]:




# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:

print(lista.index('Mendoza'))



# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:

ValueError                                Traceback (most recent call last)
Cell In[24], line 1
----> 1 print(lista.index('nada'))

ValueError: 'nada' is not in list



# 12) Eliminar un elemento de la lista

# In[25]:

lista.remove('Mendoza')
print(lista)



# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:

lista.remove('NoEsta')
print(lista)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[28], line 1
----> 1 lista.remove('NoEsta')
      2 print(lista)

ValueError: list.remove(x): x not in list


# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:


ultimo=lista.pop()
print(ultimo)


# 15) Mostrar la lista multiplicada por 4

# In[29]:
print(lista * 4)


# 16) Crear una tupla que contenga los números enteros del 1 al 20

# In[32]:

mi_tupla=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print(mi_tupla)


# 17) Imprimir desde el índice 10 al 15 de la tupla

# In[35]:
print(mi_tupla[10:16])



# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:

print(20 in mi_tupla)
print(30 in mi_tupla)



# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[48]:

elemento='Roma'
if not elemento in lista:
    print('no se encuentar en la lista')
else:
    print('elemento encontrado')



# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:

print(mi_tupla.count(10))
print(lista.count('Roma'))



# 21) Convertir la tupla en una lista

# In[52]:


lista2=list(mi_tupla)
print(lista2)


# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:

uno=mi_tupla[0]
dos=mi_tupla[1]
tres=mi_tupla[2]
print(uno,dos,tres)



# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

# In[57]:


{  'Ciudad': lista, 
'País': ['Brasil','Paraguay','Ecuador','Uruguay','Chile','Perú','Venezuela','Colombia','Méjico','Uruguay','España','Italia','Francia'], 
'Continente' : ['América','América','América','América','América','América','América','América','América','América','Europa','Europa','Europa']}



# 24) Imprimir las claves del diccionario

# In[59]:
print(dicc.keys())



# 25) Imprimir las ciudades a través de su clave

# In[61]:

print(dicc['Ciudad'])


