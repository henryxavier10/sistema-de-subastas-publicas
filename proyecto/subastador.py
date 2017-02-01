from pub import *
from sub import *
from settings import r

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
	      print("\n Ingrese un nombre valido") 
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
	      print("\n Ingrese una opcion valida")

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
	   		mensaje="Subasta "+canal_subasta+"creada por"+nombre_subastador+"esta abierta"
	   		r.publish(canal, mensaje)
	   		ver_subastas(canal, mensaje,canal_subasta,nombre_subastador)

def ver_subastas(canal,mensaje,canal_subasta,nombre_subastador):
	print ("*************************************************************")
	print ("*************************************************************")
	print ("***********************MI SUBASTA****************************")
	print ("*************************"+canal_subasta+"*****************")
	print ("*************************************************************")
	print ("Ingrese <terminar> para dar por terminada la subasta")
	
	opcion =True
	while opcion:
		producto=raw_input("Ingrese descripcion del producto\n")
		precio=raw_input("Ingrese precio del producto\n")
		
		if producto =="salir" or precio =="salir":
			menu_principal(nombre_subastador)
		else:
			if producto=="" or precio=="":
				print("\n Ingrese informacion valida")
			else:
		   		canal=canal_subasta
		   		mensaje="Procducto: "+producto+"\nPrecio: "+precio
		   		r.publish(canal, mensaje)

		   		pubsub = r.pubsub()
				pubsub.subscribe("canal_subasta")
				while True:
					for item in pubsub.listen():
						print item['data']

def ver_ofertas(canal,mensaje,canal_subasta,nombre_subastador):
	print ("*************************************************************")
	print ("*************************************************************")
	print ("***********************ESPERANDO PUJAS***********************")
	print ("*************************"+canal_subasta+"*****************")
	print ("*************************************************************")
	print ("Ingrese <salir> para regresar")
	
	opcion =True
	while opcion:
		producto=raw_input("Ingrese descripcion del producto\n")
		precio=raw_input("Ingrese precio del producto\n")
		
		if producto =="salir" or precio =="salir":
			menu_principal(nombre_subastador)
		else:
			if producto=="" or precio=="":
				print("\n Ingrese informacion valida")
			else:
		   		canal=canal_subasta
		   		mensaje="Procducto: "+producto+"\nPrecio: "+precio
		   		r.publish(canal, mensaje)

		   		pubsub = r.pubsub()
				pubsub.subscribe("canal_subasta")
				while True:
					for item in pubsub.listen():
						print item['data']




if __name__ == '__main__':
	menu(nombre_subastador)
