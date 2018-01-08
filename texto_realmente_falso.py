import random
#recibir archivo
texto = open('.git\entrada.txt','r')
lista = []
diccionario = {}
anterior = ""
#print texto.read(5)
for linea in texto:
    linea = linea.split(" ")
    lista = lista + linea
#se crea una lista de las palabras del texto en orden
#print lista
#-------------------------------------------------------------------------------
#leer palabra a palabra
for palabra in lista:
#si palabra posee grupo
    if diccionario.has_key(anterior):
        #(true) agregar palabra siguiente
        diccionario[anterior].append(palabra)
        anterior= palabra
    else:
        #(false) crear grupo
        diccionario[anterior]= [palabra]
        anterior= palabra
#print str(diccionario).replace("],","]\n")
#ir a leer palabra siguente
texto.close()
#fin parte uno
#--------------------------------------------------------------------------------
#generar nuevo archivo
resultado= open(".git\salida.txt","a")
#print "holi "  + resultado.read()
#buscar palabra inicial
palabra=""

for i in range(0, 100, 1)  :
    #si existe siguiente palabra
    if len(diccionario[palabra])>0:
        #(true) seleccionar , escribir y eliminar
        suerte = random.randint(0,len(diccionario[palabra])-1)
        resultado.write(diccionario[palabra][suerte] + " ")
        anterior = diccionario[palabra][suerte]
        del diccionario[palabra][suerte]
        palabra = anterior
    else:
        #(false) poner un punto , salto de linea
        resultado.write(".\n")
        del diccionario[palabra]
        #elegir aleatoriamente una palabra
        suerte2 = random.randint(0,len(diccionario.keys()))
        palabra = diccionario.keys()[suerte2]
#termina proceso
resultado.close()
