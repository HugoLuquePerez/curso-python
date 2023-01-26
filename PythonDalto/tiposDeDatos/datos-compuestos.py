""" listas y tupla (lista es un cojunto de variables modificales) y (tupla no es modificable) """
lista = ["Hugo Luque","Soy Dalto",True,1.85]
tupla = ("Hugo Luque","Soy Dalto",True,1.85)
print(lista[0])

""" Lista si es modificable """
lista[0] = "Lucas Dalto"
print(lista[0])

""" Tupla no es modificable """
print(tupla[2])
#tupla[2] = False
#print(tupla[2])

""" Conjunto set se puede redefinir la variable pero no se puede modificar, tampoco puede indexear para mostralo pero si puedes mostrarlo entero
(en caso de que se repita algun valor se eliminara automaticamente) """
conjunto = {"Hugo Luque","Soy Dalto",True,1.85}
print(conjunto)

""" creando un diccionario (dict) """
""" El dict para ser indexado no se utilizan numeros si no el nombre que tiene asociado """
diccionario = {
  'nombre' : "Hugo Luque",
  'canal' : "Soy Hugo",
  'esta_emocionado' : "True",
  'altura' : 1.84
}
print(diccionario)
print(diccionario["altura"])

diccionario['nombre'] = 'Rauw Alejadro'
print(diccionario['nombre'])