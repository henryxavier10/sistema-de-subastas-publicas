#!/usr/bin/env python
# Este archivo usa el encoding: utf-8


from pub import *
from sub import *
from settings import r
import time 


nombre_subastador=""
canales=[]
nombre_producto=""
precio_producto=""


	
def menu(nombre_subastador):
	print ("*************************************************************")
	print ("*************************************************************")
	print ("***********************BIENVENIDO/A SUBASTAS ON_LINE*********")
	print ("*************************************************************")
	print ("*************************************************************")
	opcion=True
	while opcion:
	   
	    nombre_subastador=raw_input("Ingrese su nombre\n") 
	    if nombre_subastador=="": 
	      print("\n Ingrese un nombre válido") 
	    else:
	      menu_principal(nombre_subastador)

def menu_principal(nombre_subastador):
	print ("***************************************************************")
	print ("***************************************************************")
	print ("**************BIENVENIDO SUBASTADOR "+nombre_subastador+"******")
	print ("***************************************************************")
	print ("***************************************************************")
	opcion=True
	while opcion:
	    print ("""
	    1.Crear una subasta
	    2.Salir
	    """)
	    opcion=raw_input("Ingrese una opcion ") 
	    if opcion=="1": 
	      crear_subasta(nombre_subastador)
	    elif opcion=="2":
	      print("\n Goodbye") 
	      quit()
	    elif opcion!="":
	      print("\n Ingrese una opción válida")

def crear_subasta(nombre_subastador):
	print ("*************************************************************")
	print ("*************************************************************")
	print ("*********************** SUBASTAS*****************************")
	print ("*************************************************************")
	print ("*************************************************************")
	opcion =True
	while opcion:

	   	print ("Ingrese <salir> para regresar")
	   	canal_subasta=raw_input("Ingrese un nombre para la subasta\n")
	   	if canal_subasta=="":
	   		print("\n Ingrese un nombre valido")
	   	elif canal_subasta=="salir":
	   		menu_principal(nombre_subastador)
	   	else:
	   		canal="subastas"
	   		mensaje="Subasta "+canal_subasta+" creada por "+nombre_subastador
	   		r.publish(canal, mensaje)
	   		ver_subastas(canal, mensaje,canal_subasta,nombre_subastador)

def ver_subastas(canal,mensaje,canal_subasta,nombre_subastador):
	print ("*************************************************************")
	print ("*************************************************************")
	print ("***********************MI SUBASTA****************************")
	print ("*************************"+canal_subasta+"*****************")
	print ("*************************************************************")
	print ("Ingrese <salir> para regresar")
	
	opcion =True
	participantes=[]
	pubsub = r.pubsub()
	pubsub.subscribe(canal_subasta+"subasta")
	for item in pubsub.listen():
		if item['data'] == 1:
			print ("Esperando participantes>>>>>")
		else:
			if len(str(item['data'])) > 1:
				print item['data']
				participantes.append(str(item['data']))
		time.sleep( 15 )
		pubsub.unsubscribe()

	if len(participantes)>0:		
		print ("*************************************************************")
		while opcion:
			producto=raw_input("Ingrese descripcion del producto\n")
			
			if producto =="salir":
				menu_principal(nombre_subastador)
			else:
				precio=raw_input("Ingrese precio base del producto\n")
				if producto=="" or precio=="":
					print("\n Ingrese informacion valida")
				else:
			   		mensaje="Producto: "+producto+"\nPrecio base: "+precio
			   		r.publish(canal_subasta, mensaje)
			   		ver_pujas(canal,mensaje,canal_subasta,nombre_subastador,participantes)
	else:
		print ("No hay participantes ")
		menu_principal(nombre_subastador)


def ver_pujas(canal,mensaje,canal_subasta,nombre_subastador,participantes):
	print ("*************************************************************")
	print ("*************************************************************")
	print ("**********************"+canal_subasta+"**********************")
	print ("**************************PUJAS******************************")
	print ("*************************************************************")
	lista_salir=[]
	pubsub = r.pubsub()
	pubsub.subscribe(canal_subasta)
	for item in pubsub.listen():
		if item['data']== "terminar":
			lista_salir.append(str(item['data']))
			if len(lista_salir)==len(participantes):
				pubsub.unsubscribe()
		else:
			if item['data'] ==1:
				print ("Esperando pujas>>>>>")
			elif item['data'] ==0:
				print ("Termino pujas>>>>>")
			else:
				print item['data']
		
		
		

	nombre_ganador=raw_input("Ingrese el nombre del ganador: ")	
	
	if nombre_ganador == "":
		menu_principal(nombre_subastador)
	else:
		canal=canal_subasta+"terminada"
	   	mensaje="El ganador es: "+nombre_ganador
	   	r.publish(canal, mensaje)
	   	menu_principal(nombre_subastador)



if __name__ == '__main__':
	menu(nombre_subastador)
