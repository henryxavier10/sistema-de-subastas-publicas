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
	      print("\n Ingrese un nombre valido") 
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
	    2.Salir
	    """)
	    opcion=raw_input("Ingrese una opcion ") 
	    if opcion=="1": 
	      ver_subasta(nombre_participante)
	    elif opcion=="2":
	      print("\n Goodbye") 
	      quit()
	    elif opcion!="":
	      print("\n Ingrese una opcion valida")

def ver_subasta(nombre_participante):
	print ("*************************************************************")
	print ("*************************************************************")
	print ("***********************SUBASTA*******************************")
	print ("*************************************************************")
	print ("*************************************************************")
	
	
	pubsub = r.pubsub()
	pubsub.subscribe("subastas")
	for item in pubsub.listen():
		print item['data']
		time.sleep( 15 )
		pubsub.unsubscribe()

	nombre_subasta=raw_input("Ingrese el nombre de la subasta que desee participar o salir si no desea participar\n") 
	if nombre_participante=="": 
	  print("\n Ingrese un nombre valido") 
	elif nombre_subasta=="salir":
		menu_principal(nombre_participante)
	else:
		mensaje=nombre_participante
   		r.publish(nombre_subasta, mensaje)
   		crear_puja(nombre_participante,nombre_subasta)

def crear_puja(nombre_participante,nombre_subasta):
	print ("*************************************************************")
	print ("*************************************************************")
	print ("***********************SUBASTA****************************")
	print ("*************************"+nombre_subasta+"*****************")
	print ("*************************************************************")
	print ("Ingrese <salir> para regresar")

	pubsub = r.pubsub()
	pubsub.subscribe(nombre_subasta)
	for item in pubsub.listen():
		print item['data']
		time.sleep( 10 )
		pubsub.unsubscribe()
	
	opcion =True
	while opcion:
		puja=raw_input("Ingrese su oferta\n")
		
		if puja =="salir":
			menu_principal(nombre_participante)
		else:
			if puja=="":
				print("\n Ingrese informacion valida")
			else:
		   		mensaje=nombre_participante+" ofrece: "+puja+"\n"
		   		r.publish(nombre_subasta, mensaje)

		   		
		   		#pubsub = r.pubsub()
				#pubsub.subscribe(nombre_subasta)
				#for item in pubsub.listen():
				#	print item['data']
				#time.sleep( 20 )
				#pubsub.unsubscribe()

		   		




if __name__ == '__main__':
	menu(nombre_participante)
