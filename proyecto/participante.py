#!/usr/bin/env python
# Este archivo usa el encoding: utf-8

from pub import *
from sub import *
from settings import r
import time


nombre_participante=""
canales=[]
nombre_producto=""
precio_producto=""


	
def menu(nombre_participante):
	print ("*************************************************************")
	print ("*************************************************************")
	print ("***********************BIENVENIDO/A SUBASTAS ON_LINE*********")
	print ("*************************************************************")
	print ("*************************************************************")
	opcion=True
	while opcion:
	   
	    nombre_participante=raw_input("Ingrese su nombre\n") 
	    if nombre_participante=="": 
	      print("\n Ingrese un nombre válido") 
	    else:
	      menu_principal(nombre_participante)

def menu_principal(nombre_participante):
	print ("***************************************************************")
	print ("***************************************************************")
	print ("************BIENVENIDO PARTICIPANTE "+nombre_participante+"****")
	print ("***************************************************************")
	print ("***************************************************************")
	opcion=True
	while opcion:
	    print ("""
	    1.Participar en una subasta
	    2.-Salir
	    """)
	    opcion=raw_input("Ingrese una opción ") 
	    if opcion=="1": 
	      ver_subasta(nombre_participante)
	    elif opcion=="2":
	    	print("\n Goodbye")
	    	quit()
	    elif opcion!="":
	      print("\n Ingrese una opcion válida")

def ver_subasta(nombre_participante):
	print ("*************************************************************")
	print ("*************************************************************")
	print ("***********************SUBASTA*******************************")
	print ("*************************************************************")
	print ("*************************************************************")
	print ("Ingrese <salir> para regresar")
	subastas=[]
	pubsub = r.pubsub()
	pubsub.subscribe("subastas")
	for item in pubsub.listen():
		if item['data'] == 1:
			print ("Esperando la subasta creada>>>>>>>>>>>>>>>>>>>>")
		else:
			if len(str(item['data'])) > 1:
				print item['data']
				subastas.append(str(item['data']))
				pubsub.unsubscribe()

	if len(subastas)>0:
		nombre_subasta=raw_input("Ingrese el nombre de la subasta que desee participar o salir\n") 
		if nombre_participante=="": 
		  print("\n Ingrese un nombre valido") 
		elif nombre_subasta=="salir":
			menu_principal(nombre_participante)
		else:
			mensaje=nombre_participante
	   		r.publish(nombre_subasta+"subasta", mensaje)
	   		crear_puja(nombre_participante,nombre_subasta)
	else:
		print ("No hay subastas creadas")
		menu_principal(nombre_participante)

def crear_puja(nombre_participante,nombre_subasta):
	print ("*************************************************************")
	print ("*************************************************************")
	print ("************************SUBASTA******************************")
	print ("*******************"+nombre_subasta+"************************")
	print ("*************************************************************")
	print ("Ingrese <salir> para regresar")

	pubsub = r.pubsub()
	pubsub.subscribe(nombre_subasta)
	for item in pubsub.listen():
		if item['data'] == 1:
			print ("Esperando que comience la subasta>>>>>>>>>>>>>>>>>>>>")
		elif item['data'] == 0:
			print ("No hay una subasta abierta")
			menu_principal(nombre_participante)
		else:
			print item['data']
			if len(str(item['data'])) > 1:
				comenzar_subasta(nombre_participante,nombre_subasta)

			
		   		#pubsub = r.pubsub()
				#pubsub.subscribe(nombre_subasta)
				#for item in pubsub.listen():
				#	print item['data']
				#time.sleep( 20 )
				#pubsub.unsubscribe()

		   		
def comenzar_subasta(nombre_participante,nombre_subasta):
	print ("**************************************************************")
	print ("***********************Comenzo la subasta*********************")
	print ("**************************************************************")
	print ("Ingrese <terminar> para salir")
	opcion =True
	while opcion:
		puja=raw_input("Ingrese su oferta\n")
		
		if puja =="terminar":
			r.publish(nombre_subasta, "terminar")
			ver_resultado(nombre_participante,nombre_subasta)
		else:
			if puja=="":
				print("\n Ingrese información válida")
			else:
		   		mensaje=nombre_participante+" ofrece: "+puja+"\n"
		   		r.publish(nombre_subasta, mensaje)


def ver_resultado(nombre_participante,nombre_subasta):
	print ("**************************************************************")
	print ("***********************Resultado de la subasta****************")
	print ("**************************************************************")
	print ("Ingrese <salir> para regresar")
	pubsub = r.pubsub()
	nombre_subasta=nombre_subasta+"terminada"
	pubsub.subscribe(nombre_subasta)
	for item in pubsub.listen():
		if item['data'] == 1:
			print ("Esperando resultado de la subasta>>>>>>>>>>>>>>>>>>>>")
		elif item['data'] == 0:
			menu_principal(nombre_participante)
		else:
			if len(str(item['data'])) > 1:
				print item['data']
				time.sleep(4)
				menu_principal(nombre_participante)

		
			


if __name__ == '__main__':
	menu(nombre_participante)
