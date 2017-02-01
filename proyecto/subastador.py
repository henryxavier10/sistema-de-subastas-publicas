from pub import *
from sub import *
from settings import r

nombre_subastador=""
canales=[]



	
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
	    2.Ver subastas creadas
	    3.Salir
	    """)
	    opcion=raw_input("Ingrese una opcion ") 
	    if opcion=="1": 
	      crear_subasta(nombre_subastador)
	    elif opcion=="2":
	      ver_subastas()
	    elif opcion=="3":
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
	   		mensaje=canal_subasta
	   		r.publish(canal, mensaje)

def ver_subastas():
	print ("*************************************************************")
	print ("*************************************************************")
	print ("***********************MIS SUBASTAS**************************")
	print ("*************************************************************")
	print ("*************************************************************")
	
	pubsub = r.pubsub()
	pubsub.subscribe("subastas")
	while True:
		for item in pubsub.listen():
			print item['data']




if __name__ == '__main__':
	menu(nombre_subastador)
